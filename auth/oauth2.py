from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt,JWTError
from sqlalchemy.orm.session import Session
from fastapi import Depends, HTTPException,status
from db.database import get_db
from crud.user import get_user_by_email
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
SECRET_KEY = '77407c7339a6c00544e51af1101c4abb4aea2a31157ca5f7dfd87da02a628107'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_current_user(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
  credentials_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Could nor validate credentials",
    headers={"WWW-Authenticate" : "Bearer"}
    )
  
  try:
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    email=payload.get("sub")
    if email is None:
      raise credentials_exception
  except JWTError:
    raise credentials_exception
  
  user = get_user_by_email(db,email=email)
  if user is None:
    raise credentials_exception

  return user