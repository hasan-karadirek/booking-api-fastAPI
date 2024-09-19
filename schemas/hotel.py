from pydantic import BaseModel

class HotelIn(BaseModel):
    name:str
    address:str
    city:str
    tel:str
    email:str