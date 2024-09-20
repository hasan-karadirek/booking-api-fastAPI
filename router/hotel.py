from schemas.user import UserIn
from sqlalchemy.orm import Session
from crud import hotel as hotel_crud
from auth.oauth2 import get_current_hotel_admin, get_create_room_permission
from db.database import get_db
from fastapi import Depends, APIRouter, UploadFile, File, Form
from schemas.hotel import HotelIn, RoomIn

router = APIRouter(prefix="/hotel", tags=["hotel"])


@router.post("/create_hotel")
def create_hotel(
    name: str = Form(...),
    address: str = Form(...),
    city: str = Form(...),
    tel: str = Form(...),
    email: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_hotel_admin: UserIn = Depends(get_current_hotel_admin),
):

    return hotel_crud.create_hotel(
        db=db,
        request=HotelIn(name=name, address=address, city=city, tel=tel, email=email),
        current_hotel_admin=current_hotel_admin,
        image=image,
    )

@router.get("/{id}")
def get_hotel(id : int, db: Session = Depends(get_db)):
    return hotel_crud.get_hotel(id=id,db=db)

@router.post("/create_room")
def create_room(
    room_no: str = Form(...),
    bed_count: int = Form(...),
    price: float = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    hotel: HotelIn = Depends(get_create_room_permission),
):
    return hotel_crud.create_room(
        db=db,
        request=RoomIn(
            room_no=room_no, bed_count=bed_count, price=price, hotel_id=hotel.id
        ),
        image=image,
    )
@router.get("/room/{id}")
def get_room(id : int, db: Session = Depends(get_db)):
    return hotel_crud.get_room(id=id,db=db)
