from db.database import Base
from enum import Enum
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Column,Enum as sqlEnum

class UserType(str, Enum):
    CUSTOMER = "customer"
    HOTEL_ADMIN = "hotel admin"
    SYSTEM_ADMIN = "system admin"


class DBUser(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String, nullable=False)
    lastname=Column(String, nullable=False)
    email=Column(String, nullable=False,unique=True)
    password=Column(String, nullable=False)
    type=Column(sqlEnum(UserType), nullable=False, default="CUSTOMER")
   
