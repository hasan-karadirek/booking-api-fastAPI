from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from models.user import DBUser
from schemas.user import UserIn
from core.hash import Hash
from sqlalchemy.exc import IntegrityError

def create_user(db:Session,request:UserIn):
    try:
        user=DBUser(name = request.name,lastname=request.lastname,email=request.email,password=Hash.bcrypt(request.password),type=request.type)
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )
    return user