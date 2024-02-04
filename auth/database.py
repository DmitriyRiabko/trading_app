import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from config import DB_USER, DB_HOST, DB_NAME, DB_PASS, DB_PORT
from models.models import role


from sqlalchemy import TIMESTAMP, Column, Boolean, ForeignKey, Integer, String

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    id:int = Column( Integer, primary_key=True),
    email:str = Column(String,nullable=False),
    username:str = Column(String, nullable=False),
    password:str = Column(String,nullable=False),
    registered_at:str = Column(TIMESTAMP, default=datetime.utcnow),
    role_id:str = Column(Integer, ForeignKey(role.c.id)),
    hashed_password: str = Column(String(length=1024), nullable=False)    
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, echo=True)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)