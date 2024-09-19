from schemas.user import UserIn,UserType
from sqlalchemy.orm import Session
from crud import hotel
from auth.oauth2 import get_current_user
from db.database import get_db
from fastapi import Depends, APIRouter, UploadFile, File,HTTPException,status,Form
from schemas.hotel import HotelIn

router=APIRouter(
    prefix="/hotel",
    tags=["hotel"]
)

@router.post("/create_hotel")
def create_hotel(name: str = Form(...),
    address: str = Form(...),
    city: str = Form(...),
    tel: str = Form(...),
    email: str = Form(...), image: UploadFile = File(...),db : Session = Depends(get_db),current_user:UserIn=Depends(get_current_user)):
    if current_user.type != UserType.HOTEL_ADMIN:
        print(current_user.type,"hasan")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You do not have authorization to create a hotel.")
    return hotel.create_hotel(db=db,request=HotelIn(name=name, address=address,city=city,tel=tel,email=email),current_hotel_admin=current_user,image=image)