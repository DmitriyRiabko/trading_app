from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,insert

from operations.models import operation
from operations.schemas import OperationCreate
from database import get_async_session

router = APIRouter(
    prefix="/operations",
    tags=['Operation']
)


@router.get('/')
async def get_specific_operation(
    operation_type:str,
    session:AsyncSession = Depends(get_async_session)
):
    stmt = select(operation).where(operation.c.type == operation_type)
    res = await session.execute(stmt)
    return {'message' :str(stmt)}


@router.post('/')
async def add_specific_operations(
    new_operation:OperationCreate,
    session:AsyncSession =Depends(get_async_session)
    
):
    
    print(new_operation.model_dump())
    stmt = insert(operation).values(new_operation.model_dump())
    await session.execute(stmt)
    return {'status':'success'}