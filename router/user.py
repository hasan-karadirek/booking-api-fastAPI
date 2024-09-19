from schemas.user import UserIn, UserOut
from sqlalchemy.orm import Session
from crud import user
from auth.oauth2 import get_current_user
from db.database import get_db
from fastapi import Depends, APIRouter

router = APIRouter(tags=["User"], prefix="/user")


@router.post("/create_user", response_model=UserOut)
def create_user(request: UserIn, db: Session = Depends(get_db)):
    return user.create_user(db, request)


@router.get("/{id}", response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user_by_id(db=db, id=id)
