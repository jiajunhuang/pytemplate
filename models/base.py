import datetime
import contextlib

from sqlalchemy import (
    create_engine,
    Column,
    DateTime,
    Integer,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config

engine = create_engine(config.SQLALCHEMY_DB_URI, echo=config.SQLALCHEMY_ECHO)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class BaseMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    deleted_at = Column(DateTime, nullable=True, index=True)


@contextlib.contextmanager
def get_session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception:
        s.rollback()
        raise
    finally:
        s.close()
