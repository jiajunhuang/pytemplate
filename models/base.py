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

    @classmethod
    def get_by_id(cls, session, item_id):
        """session should be SQLAlchemy Session object"""
        return session.query(cls).filter(
            cls.id == item_id,
            cls.deleted_at == None,  # noqa
        ).first()

    @classmethod
    def get_by_id_list(cls, session, item_id_list):
        return session.query(cls).filter(
            cls.id.in_(item_id_list),
            cls.deleted_at == None,  # noqa
        ).all()


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
