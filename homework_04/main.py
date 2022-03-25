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
import sys
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_session

from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from homework_04.models import engine, Base, User, Post, Session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, user_data):
    for data in user_data:
        users = User(id=data["id"], user=data["name"], username=data["username"], email=data["email"])
    session.add(users)
    await session.commit()


async def create_post(session: AsyncSession, post_data):
    for data in post_data:
        posts = Post(id=data["id"], user_id=data["userId"], title=data["title"], body=data["body"])
    session.add(posts)
    await session.commit()


async def async_main():
    # users_data: List[dict]
    # posts_data: List[dict]

    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with Session() as session:
        await create_user(session, users_data)
        await create_post(session, posts_data)


def main():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
