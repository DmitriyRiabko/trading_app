from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,insert
import time

from operations.models import operation
from operations.schemas import OperationCreate
from database import get_async_session
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/operations",
    tags=['Operation']
)


@router.get('/long_operation')
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return 'to much data'





@router.get('/')
async def get_specific_operation(
    operation_type:str,
    session:AsyncSession = Depends(get_async_session)
):
    stmt = select(operation).where(operation.c.type == operation_type)
    res = await session.execute(stmt)
    return {'message':res}


@router.post('/')
async def add_specific_operations(
    new_operation:OperationCreate,
    session:AsyncSession =Depends(get_async_session)
    
):
    
    stmt = insert(operation).values(new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {'status':'success'}