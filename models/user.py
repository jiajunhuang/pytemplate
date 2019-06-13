import uuid
import bcrypt

from sqlalchemy import (
    Column,
    String,
    Boolean,
)

from models.base import (
    Base,
    BaseMixin,
)


class User(Base, BaseMixin):
    __tablename__ = "user"

    name = Column(String(256), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    verified = Column(Boolean, nullable=False, default=False)
    token = Column(String(64), nullable=False, unique=True)
    addr = Column(String(256), index=True)

    @classmethod
    def register(cls, session, name, email, password):
        user = User(
            name=name,
            email=email,
            password=cls.gen_password(password),
            token=str(uuid.uuid4()).replace("-", ""),
        )
        session.add(user)
        session.commit()

        return user

    @classmethod
    def login(cls, session, email, password):
        user = cls.get_by_email(session, email)
        if user and user.check_password(password):
            return user

    @classmethod
    def get_by_email(cls, session, email):
        return session.query(cls).filter(
            cls.email == email,
            cls.deleted_at.is_(None),
        ).first()

    @classmethod
    def get_by_token(cls, session, token):
        return session.query(cls).filter(
            cls.token == token,
            cls.deleted_at.is_(None),
        ).first()

    @classmethod
    def get_by_addr(cls, session, addr):
        return session.query(cls).filter(
            cls.addr == addr,
            cls.deleted_at.is_(None),
        ).first()

    @staticmethod
    def gen_password(password):
        return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt()).decode("utf8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf8"), self.password.encode("utf8"))
