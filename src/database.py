from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from config import DB_USER, DB_HOST, DB_NAME, DB_PASS, DB_PORT
from sqlalchemy.ext.declarative import  declarative_base

Base = declarative_base()


DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'



engine = create_async_engine(DATABASE_URL,echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False,)



async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


