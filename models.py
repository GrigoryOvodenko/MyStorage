from pydantic import BaseModel
from typing import List





class SaveDataClass(BaseModel):
    key: str
    value:object
    flag:bool
class GetDataClass(BaseModel):
    key:str
class DelDataClass(BaseModel):
    key:str
    flag:bool

#find keys
class ValDataClass(BaseModel):
    value:str

class OpenTransDataClass(BaseModel):
    task:str
    data:dict