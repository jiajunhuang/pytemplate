from sqlalchemy import (
    Column,
    String,
)

from models.base import (
    Base,
    BaseMixin,
)


class HelloLog(Base, BaseMixin):
    __tablename__ = "hello_log"

    name = Column(String(256), nullable=False)
