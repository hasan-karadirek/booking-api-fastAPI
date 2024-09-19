from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status,Depends, UploadFile, File
from models.hotel import DbHotel
from schemas.user import UserIn
from schemas.hotel import HotelIn
import shutil


def create_hotel(db:Session,request:HotelIn, current_hotel_admin: UserIn, image: UploadFile = File(...)):
    file_location = f"uploaded_images/{image.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    hotel=DbHotel(name = request.name,address=request.address,city=request.city, tel=request.tel, email=request.email, image=file_location,user_id=current_hotel_admin.id)
    db.add(hotel)
    db.commit()
    db.refresh(hotel)
    
    return hotel