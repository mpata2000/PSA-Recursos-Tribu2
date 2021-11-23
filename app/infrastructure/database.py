import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    engine = create_engine(
        DATABASE_URL,
    )
    SessionLocal = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
    )

except KeyError as e:
    pass
except Exception as e:
    print("EL ERROR ESTA ACA", e)

Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)