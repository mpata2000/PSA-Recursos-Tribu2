import json
import logging
import requests

from datetime import date
from logging import config
from typing import Iterator, List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.orm.session import Session
from starlette.middleware.cors import CORSMiddleware

from app.domain.hours import (
    HoursDayAlreadyExistsError,
    HoursNotFoundError,
    HoursRepository,
)
from app.infrastructure.database import create_tables, SessionLocal

from app.infrastructure.hours import (
    HoursCommandUseCaseUnitOfWorkImpl,
    HoursQueryServiceImpl,
    HoursRepositoryImpl,
)

from app.presentation.schema.hours.hours_error_message import (
    ErrorMessageHoursDayAlreadyExists,
    ErrorMessageHoursNotFound, ErrorMessageHoursNotValidDate,
)
from app.presentation.schema.resources.resources_error_message import ErrorMessageResourcesNotFound
from app.usecase.hours import (
    HoursCommandUseCase,
    HoursCommandUseCaseImpl,
    HoursCommandUseCaseUnitOfWork,
    HoursCreateModel,
    HoursQueryService,
    HoursQueryUseCase,
    HoursQueryUseCaseImpl,
    HoursReadModel,
    HoursPutModel,
)
from app.usecase.hours.hours_query_model import PaginatedHoursReadModel
from app.usecase.resources.resources_query_model import PaginatedResourcesReadModel

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

description = """
API de recursos de PSA para la Tribu 2 por el Squad 11

## Hours

- Date in requests and responses will be represented as a `str` in `ISO 8601` format, like: `2008-09-15`.
- You can not create a new hour by the same user in the same day at the same task twice, you have to update it
- On put tou can only change the date,minutes and note of the Hours created

"""

app = FastAPI(
    title="PSA Recursos",
    version="1.0.0",
    description=description,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def hours_query_usecase(session: Session = Depends(get_session)) -> HoursQueryUseCase:
    hours_query_service: HoursQueryService = HoursQueryServiceImpl(session)
    return HoursQueryUseCaseImpl(hours_query_service)


def hours_command_usecase(
        session: Session = Depends(get_session),
) -> HoursCommandUseCase:
    hours_repository: HoursRepository = HoursRepositoryImpl(session)
    uow: HoursCommandUseCaseUnitOfWork = HoursCommandUseCaseUnitOfWorkImpl(
        session, hours_repository=hours_repository
    )
    return HoursCommandUseCaseImpl(uow)


@app.post(
    "/hours",
    response_model=HoursReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "model": ErrorMessageHoursDayAlreadyExists,
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": ErrorMessageHoursNotValidDate,
        },
    },
    tags=["hours"],
)
async def create_hours(
        data: HoursCreateModel,
        hours_command_usecase: HoursCommandUseCase = Depends(hours_command_usecase),
):
    try:
        hours = hours_command_usecase.create_hours(data)
    except HoursDayAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return hours


@app.get(
    "/hours",
    response_model=PaginatedHoursReadModel,
    status_code=status.HTTP_200_OK,
    tags=["hours"],
)
async def get_hours(
        ids: Optional[List[str]] = Query(None),
        day: Optional[date] = None,
        user_id: Optional[str] = None,
        task_id: Optional[str] = None,
        minutes: Optional[int] = None,
        limit: int = 50,
        offset: int = 0,
        hours_query_usecase: HoursQueryUseCase = Depends(hours_query_usecase),
):
    try:
        hours, count = hours_query_usecase.fetch_hours_by_filters(
            ids=ids,
            day=day,
            user_id=user_id,
            task_id=task_id,
            minutes=minutes,
            limit=limit,
            offset=offset,
        )

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if hours is None or len(hours) == 0:
        logger.info(HoursNotFoundError.message)

    return PaginatedHoursReadModel(hours=hours, count=count)


@app.put(
    "/hours/{id}",
    response_model=HoursReadModel,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageHoursNotFound,
        },
    },
    tags=["hours"],
)
async def put_hours(
        id: str,
        data: HoursPutModel,
        hours_command_usecase: HoursCommandUseCase = Depends(hours_command_usecase),
):
    try:
        updated_hours = hours_command_usecase.put_hours(id, data)
    except HoursNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return updated_hours


@app.delete(
    "/hours/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=HoursReadModel,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageHoursNotFound,
        },
    },
    tags=["hours"],
)
async def delete_hours(
        id: str,
        hours_command_usecase: HoursCommandUseCase = Depends(hours_command_usecase),
):
    try:
        deleted_hour = hours_command_usecase.delete_hours_by_id(id)
    except HoursNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return deleted_hour


@app.get(
    "/resources",
    response_model=PaginatedResourcesReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageResourcesNotFound,
        },
    },
    tags=["resources"],
)
async def get_resources():
    data = json.loads(
        requests.get(
            "https://anypoint.mulesoft.com/"
            "mocking/api/v1/sources/exchange/assets/"
            "754f50e8-20d8-4223-bbdc-56d50131d0ae/"
            "recursos-psa/1.0.0/m/api/recursos"
        ).text
    )

    return PaginatedResourcesReadModel(resources=data, count=len(data))
