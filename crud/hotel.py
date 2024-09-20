from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status, Depends, UploadFile, File
from models.hotel import DbHotel, DbRoom
from schemas.user import UserIn
from schemas.hotel import HotelIn, RoomIn
import shutil


def create_hotel(
    db: Session,
    request: HotelIn,
    current_hotel_admin: UserIn,
    image: UploadFile = File(...),
):
    file_location = f"uploaded_images/{image.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    hotel = DbHotel(
        name=request.name,
        address=request.address,
        city=request.city,
        tel=request.tel,
        email=request.email,
        image=file_location,
        user_id=current_hotel_admin.id,
    )
    db.add(hotel)
    db.commit()
    db.refresh(hotel)

    return hotel

def get_hotel(id: int, db: Session):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no such a hotel associated with this id.!")
    return hotel


def create_room(db: Session, request: RoomIn, image: UploadFile = File(...)):
    file_location = f"uploaded_images/{image.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    room = DbRoom(
        room_no=request.room_no,
        bed_count=request.bed_count,
        price=request.price,
        image=file_location,
        hotel_id=request.hotel_id,
    )
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def get_room(id: int, db: Session):
    room = db.query(DbRoom).filter(DbRoom.id == id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no such a room associated with this id!")
    return room
