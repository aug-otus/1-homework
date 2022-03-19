"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr, relationship, scoped_session

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/postgres"

Base = None
Session = None


# class Base:
#
#     @declared_attr
#     def __tablename__(cls):
#         return f"blog_{cls.__name__.lower()}s"
#
#     id = Column(Integer, primary_key=True)
#
#     def __repr__(self):
#         return str(self)


engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(engine, class_=AsyncSession)



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user = Column(String(32), nullable=False)
    username = Column(String(32),  nullable=False)
    email = Column(String(32),  default=False, nullable=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"user={self.user!r}, "
            f"username={self.username}, "
            f"email={self.email!r})"
        )

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String(64), nullable=False)
    body = Column(Text, default=False, nullable=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"user_id={self.user_id!r}, "
            f"title={self.title}, "
            f"body={self.body!r})"
        )

    user = relationship("User", back_populates="posts")

