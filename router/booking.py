from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.user import UserIn
from models.user import DBUser
from db.database import get_db
from auth.oauth2 import get_current_user
from schemas.booking import BookingIn
from crud import booking
router = APIRouter(
    prefix="/booking",
    tags=["booking"]
)

@router.post("/")
def create_booking(request : BookingIn, db: Session = Depends(get_db), current_user : DBUser = Depends(get_current_user)):
    return booking.create_booking(request=request,db=db,current_user=current_user)