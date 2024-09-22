from db.database import Base
from sqlalchemy.sql.sqltypes import Integer, String, DECIMAL, Date
from sqlalchemy import Column, ForeignKey, Enum as sqlEnum
from sqlalchemy.orm import relationship
from enum import Enum
from sqlalchemy.orm.session import Session
from models.hotel import DbRoom

class StatusType(str, Enum):
    OPEN = "open"
    PENDING = "pending"
    APPROVED = "approved"
class PaymentStatusType(str, Enum):
    OPEN = "open"
    PENDING = "pending"
    PAID = "paid"

class DbBooking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("DBUser", back_populates="bookings")
    total_cost = Column(DECIMAL, nullable=False, default=0.00)
    payment_status = Column(sqlEnum(PaymentStatusType), nullable=False, default="OPEN")
    status = Column(sqlEnum(StatusType), nullable=False, default="OPEN")
    booked_rooms = relationship("DbBookedRooms", back_populates="booking")
class DbBookedRooms(Base):
    __tablename__ = "booked_rooms"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    room = relationship("DbRoom", back_populates="bookings")
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    booking = relationship("DbBooking", back_populates="booked_rooms")
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    total_room_cost = Column(DECIMAL, nullable=False)

    