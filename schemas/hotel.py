from pydantic import BaseModel
from fastapi import Form
from typing import List


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


class GroupedRoomWithNos(BaseModel):
    room_ids: List[str]  
    price: float
    bed_count: int
    room_count: int
    hotel_id: int

    class Config:
        orm_mode = True

class HotelWithRoomsOut(BaseModel):
    id: int
    name: str
    address: str
    city: str
    tel: str
    email: str
    image: str
    grouped_rooms: List[GroupedRoomWithNos] 
    class Config:
        orm_mode = True