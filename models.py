from pydantic import BaseModel
from typing import List





class SaveDataClass(BaseModel):
    key: str
    value:object
class GetDataClass(BaseModel):
    key:str
class DelDataClass(BaseModel):
    key:str

