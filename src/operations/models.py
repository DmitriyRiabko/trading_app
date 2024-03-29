from sqlalchemy import Table,Column,Integer,String,TIMESTAMP

from database import Base

class Operation(Base):
    __tablename__ = 'operation'

    id = Column(Integer, primary_key=True)
    quantity = Column(String)
    figi = Column(String)
    instrument_type = Column(String, nullable=False)
    date = Column(TIMESTAMP(timezone=True))
    type = Column(String)