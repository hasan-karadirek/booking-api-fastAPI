from sqlalchemy.orm.session import Session
from sqlalchemy.orm import joinedload
from schemas.booking import BookingIn
from schemas.user import UserIn
from models.hotel import DbHotel, DbRoom
from models.booking import DbBooking, DbBookedRooms
from fastapi import HTTPException, status

def create_booking(db : Session, request : BookingIn, current_user : UserIn):
    hotel = db.query(DbHotel).filter(DbHotel.id == request.hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no such a hotel associated with this id.!")
    booking = DbBooking(
        user_id = current_user.id
    )
    db.add(booking)
    db.commit()
    booked_rooms = []
    total_cost = 0.00
    night_count = (request.check_out - request.check_in).days
    for room_id in request.room_ids:
        room = db.query(DbRoom).filter(DbRoom.id == room_id, DbRoom.hotel_id == hotel.id).first()
        if not room:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no such a room associated with provided room_id or hotel!")
        
        total_room_cost = night_count * room.price
        booked_room = DbBookedRooms(
            booking_id=booking.id,
            room_id = room_id,
            check_in = request.check_in,
            check_out = request.check_out,
            total_room_cost=total_room_cost
          )
        booked_rooms.append(booked_room)

        total_cost += float(total_room_cost)
    db.add_all(booked_rooms)
    booking.total_cost = total_cost

    db.commit()
    
    booking = db.query(DbBooking).options(joinedload(DbBooking.booked_rooms)).filter(DbBooking.id == booking.id).first()

    return booking