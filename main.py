import ast
import json
import logging
import os
from logging import config
from typing import Iterator, List, Optional

import requests
from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.orm.session import Session
from starlette.requests import Request

from app.domain.hours import (
    HoursDayAlreadyExistsError,
    HoursNotFoundError,
    HoursRepository,
    HoursNotFoundError,
)

from app.infrastructure.hours import (
    HoursCommandUseCaseUnitOfWorkImpl,
    HoursQueryServiceImpl,
    HoursRepositoryImpl,
)
from app.infrastructure.database import SessionLocal, create_tables
from app.presentation.schema.hours.hours_error_message import (
    ErrorMessageHoursDayAlreadyExists,
    ErrorMessageHoursNotFound,
)
from app.usecase.hours import (
    HoursCommandUseCase,
    HoursCommandUseCaseImpl,
    HoursCommandUseCaseUnitOfWork,
    HoursCreateModel,
    HoursQueryService,
    HoursQueryUseCase,
    HoursQueryUseCaseImpl,
    HoursReadModel,
    HoursUpdateModel,
)
from app.usecase.hours.hours_query_model import PaginatedHoursReadModel

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(title="hours")

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
    },
    tags=["hours"],
)
async def create_hours(
    creator_id: str,
    data: HoursCreateModel,
    hours_command_usecase: HoursCommandUseCase = Depends(hours_command_usecase),
):
    try:
        hours = hours_command_usecase.create_hours(data, creator_id)
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
    limit: int = 50,
    offset: int = 0,
    hours_query_usecase: HoursQueryUseCase = Depends(hours_query_usecase),
):
    try:
        hours, count = hours_query_usecase.fetch_hours(limit=limit, offset=offset)
    except HoursNotFoundError as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if len(hours) == 0:
        logger.info(HoursNotFoundError.message)

    return PaginatedHoursReadModel(hours=hours, count=count)


@app.get(
    "/hours/",
    response_model=PaginatedHoursReadModel,
    status_code=status.HTTP_200_OK,
    tags=["hours"],
)
async def get_hours_filtering(
    ids: Optional[List[str]] = Query(None),
    day: Optional[str] = None,
    user_id: Optional[str] = None,
    time: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    hours_query_usecase: HoursQueryUseCase = Depends(hours_query_usecase),
):

    try:
        hours, count = hours_query_usecase.fetch_hours_by_filters(
            ids=ids,
            day=day,
            user_id=user_id,
            time=time,
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


@app.get(
    "/hours/{id}",
    response_model=HoursReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageHoursNotFound,
        },
    },
    tags=["hours"],
)
async def get_hours(
    id: str,
    hours_query_usecase: HoursQueryUseCase = Depends(hours_query_usecase),
):
    try:
        hours = hours_query_usecase.fetch_hours_by_id(id)

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

    return hours


@app.patch(
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
async def update_hours(
    id: str,
    uid: str,
    data: HoursUpdateModel,
    hours_command_usecase: HoursCommandUseCase = Depends(hours_command_usecase),
    query_usecase: HoursQueryUseCase = Depends(hours_query_usecase),
):
    try:
        updated_hours = hours_command_usecase.update_hours(id, data)
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
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageHoursNotFound,
        },
    },
    tags=["hours"],
)
async def delete_hours(
    id: str,
    uid: str,
    hours_command_usecase: HoursCommandUseCase = Depends(hours_command_usecase),
    query_usecase: HoursQueryUseCase = Depends(hours_query_usecase),
):
    try:
        hours_command_usecase.delete_hours_by_id(id)
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
