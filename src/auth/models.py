from datetime import datetime
from sqlalchemy import MetaData, Table,Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from datetime import datetime
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase


from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

metadata= Base.metadata

role = Table (
    "role", metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions',JSON)
)





class User(SQLAlchemyBaseUserTable[int], Base):
    id:int = Column( Integer, primary_key=True)
    email:str = Column(String,nullable=False)
    username:str = Column(String, nullable=False)
    registered_at:str = Column(TIMESTAMP, default=datetime.utcnow)
    role_id:int = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)   
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)