"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession,  create_async_engine

from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from homework_04.models import engine, Base, User, Post, Session, async_session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, user_data: List[dict]):
    for data in user_data:
        users = User(name=data["name"], username=data["username"], email=data["email"])

    session.add(users)
    await session.commit()


async def create_post(session: AsyncSession, post_data: List[dict]):
    for data in post_data:
        posts = Post(user_id=data["user_id"], title=data["title"], body=data["body"])

    session.add(posts)
    await session.commit()


async def async_main():
    users_data: List[dict]
    posts_data: List[dict]

    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with async_session() as session:  # type: AsyncSession
        await create_user(users_data)
        await create_post(posts_data)



def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
