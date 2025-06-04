from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.models import BaseUserDB
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"
SECRET = "YOUR_SECRET_KEY"

engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base: DeclarativeMeta = declarative_base()


async def get_db():
    async with SessionLocal() as session:
        yield session


class UserTable(Base, BaseUserDB):
    pass


# 创建数据库模型
user_db = SQLAlchemyUserDatabase(UserTable, get_db)

auth_backend = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

fastapi_users = FastAPIUsers(
    user_db,
    [auth_backend],
    UserTable,
)

auth_router = fastapi_users.get_auth_router(auth_backend)
users_router = fastapi_users.get_users_router()
