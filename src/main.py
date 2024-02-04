from fastapi import  FastAPI
import fastapi_users
from auth.base_config import auth_backend
from auth.schemas import UserCreate, UserRead
from auth.base_config import fastapi_users

app = FastAPI(
    title="Trading App"
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

