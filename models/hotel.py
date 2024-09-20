from db.database import Base
from enum import Enum
from sqlalchemy.sql.sqltypes import Integer, String, DECIMAL
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship


class DbHotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    tel = Column(String, nullable=False)
    email = Column(String, nullable=False)
    image = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("DBUser", back_populates="hotels")
    rooms = relationship("DbRoom", back_populates="hotel")


class DbRoom(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    room_no = Column(String, nullable=False)
    bed_count = Column(Integer, nullable=False)
    price = Column(DECIMAL, nullable=False)
    image = Column(String, nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    hotel = relationship("DbHotel", back_populates="rooms")
