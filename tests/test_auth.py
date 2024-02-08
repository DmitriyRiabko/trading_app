import pytest
from sqlalchemy import insert, select

from .conftest import client, async_session_maker
from src import Role

@pytest.mark.asyncio
async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(Role).values(id=2, name="GOD",permissions = None)
        await session.execute(stmt)
        await session.commit()
        
        query = select(Role)
        result = await session.execute(query)
        role = result.scalar_one_or_none()
        
        # Проверяем, что роль добавлена корректно
        assert role is not None, 'Role was not added'
        assert role.id == 2, 'ID does not match'
        assert role.name == "GOD", 'Name does not match'
        assert role.permissions is None, 'Permissions do not match'

# def test_register():
#     client.post(
#         "/auth/register",
#         json={
#             "email": "Zmix@gmail.com",
#             "password": "123",
#             "is_active": True,
#             "is_superuser": False,
#             "is_verified": False,
#             "username": "string",
#             "role_id": 1,
#         },
#     )
