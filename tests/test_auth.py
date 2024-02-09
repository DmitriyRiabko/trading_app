import pytest
from sqlalchemy import insert, select

from .conftest import client, async_session_maker
from src import Role


@pytest.mark.asyncio
async def test_add_role():
    async with async_session_maker() as session:
       
        session.add(Role(id=8,name='admin',permissions=None))
        await session.commit()

        query = select(Role)
        result = await session.execute(query)
        role = result.scalar_one_or_none()

        # assert role is not None, "Role was not added"
        assert role.id == 8, "ID does not match"
        # assert role.name == "GOD", "Name does not match"
        # assert role.permissions is None, "Permissions do not match"

@pytest.mark.asyncio
def test_register():
    response = client.post(
        "/auth/register",
        json={
            "email": "Z@gmail.com",
            "password": "123",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "string",
            "role_id": 8,
        },
    )

    assert response.status_code == 201
