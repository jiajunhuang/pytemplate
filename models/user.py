from sqlalchemy import (
    Column,
    String,
)

from models.base import (
    Base,
    BaseMixin,
)


class User(Base, BaseMixin):
    __tablename__ = "user"

    name = Column(String(256), nullable=False)
