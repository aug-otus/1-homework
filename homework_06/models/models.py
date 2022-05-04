from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Text

from .database import db


class Users(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    email = Column(String(64), default=False, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"


class Posts(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    body = Column(Text, default=False, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    #    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
