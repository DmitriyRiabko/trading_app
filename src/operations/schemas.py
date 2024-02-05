from pydantic import BaseModel
from datetime import datetime







class OperationCreate(BaseModel):
    

    id:int
    quantity:str
    figi:str
    instrument_type:str
    date:datetime
    type:str
    
    class Config:
        arbitrary_types_allowed=True
  