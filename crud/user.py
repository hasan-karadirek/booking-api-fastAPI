from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status,Depends
from models.user import DBUser
from schemas.user import UserIn
from core.hash import Hash
from sqlalchemy.exc import IntegrityError
from db.database import get_db
from models.user import DBUser

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
def get_user_by_email(db:Session = Depends(get_db), email : str = None):
    user = db.query(DBUser).filter(DBUser.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )
    return user