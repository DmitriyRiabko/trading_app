from fastapi import  FastAPI
import fastapi_users
from contextlib import asynccontextmanager
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend


from operations.router import router as router_operation
from auth.base_config import auth_backend
from tasks.router import router as tasks_router
from auth.schemas import UserCreate, UserRead
from auth.base_config import fastapi_users

async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")



@asynccontextmanager
async def lifespan(app:FastAPI):
    await startup()
    yield








app = FastAPI(
    title="Trading App",
    lifespan=lifespan
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)




app.include_router(tasks_router
)