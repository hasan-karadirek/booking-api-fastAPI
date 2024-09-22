from pydantic import BaseModel
from typing import List
from datetime import date

class BookingIn(BaseModel):
    hotel_id : int
    room_ids : List[str]
    check_in : date
    check_out : date