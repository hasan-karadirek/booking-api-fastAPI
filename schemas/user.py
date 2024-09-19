from pydantic import BaseModel, EmailStr
from enum import Enum

class UserType(str, Enum):
    CUSTOMER = "customer"
    HOTEL_ADMIN = "hotel_admin"
    SYSTEM_ADMIN = "system_admin"

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