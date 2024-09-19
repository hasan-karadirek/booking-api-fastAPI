from pydantic import BaseModel
from fastapi import Form

class HotelIn(BaseModel):
    name:str = Form(...)
    address:str = Form(...)
    city:str = Form(...)
    tel:str = Form(...)
    email:str = Form(...)