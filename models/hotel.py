from db.database import Base
from enum import Enum
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

class DbHotel(Base):
    __tablename__="hotels"
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String, nullable=False)
    address=Column(String,nullable=False)
    city=Column(String,nullable=False)
    tel=Column(String,nullable=False)
    email=Column(String,nullable=False)
    image=Column(String,nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("DbUser", back_populates="hotels")