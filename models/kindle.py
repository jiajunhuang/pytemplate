import datetime

from sqlalchemy import (
    Column,
    String,
    Text,
)

from models.base import (
    Base,
    BaseMixin,
)


class Kindle(Base, BaseMixin):
    __tablename__ = "kindle"

    sender = Column(String(128), nullable=False, index=True)
    content = Column(Text)

    @classmethod
    def get_by_email(cls, session, email, minutes=10):
        current_time = datetime.datetime.utcnow()
        serveral_minutes_ago = current_time - datetime.timedelta(minutes=minutes)

        return session.query(cls).filter(
            cls.sender == email,
            cls.created_at > serveral_minutes_ago,
            cls.deleted_at.is_(None),
        ).order_by(
            cls.id.desc(),
        ).first()
