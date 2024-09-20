from pydantic import BaseModel
from fastapi import Form


class HotelIn(BaseModel):
    name: str
    address: str
    city: str
    tel: str
    email: str


class RoomIn(BaseModel):
    room_no: str
    bed_count: int
    price: float
    hotel_id: int
