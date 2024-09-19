from pydantic import BaseModel
from fastapi import Form


class HotelIn(BaseModel):
    name: str
    address: str
    city: str
    tel: str
    email: str
