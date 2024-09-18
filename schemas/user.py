from pydantic import BaseModel, EmailStr
from enum import Enum

class UserType(str, Enum):
    CUSTOMER = "customer"
    HOTEL_ADMIN = "hotel admin"
    SYSTEM_ADMIN = "system admin"

class UserIn(BaseModel):
    name:str
    lastname:str
    email:EmailStr
    password:str
    type:UserType
class UserOut(BaseModel):
    name:str
    lastname:str
    email:str