from fastapi import FastAPI,Depends
from schemas.user import UserIn,UserOut
from db.database import engine,Base,get_db
from sqlalchemy.orm import Session
from crud import user
from auth import authentication
from auth.oauth2 import get_current_user

app=FastAPI()

app.include_router(authentication.router)

@app.post("/create_user", response_model=UserOut)
def create_user(request:UserIn, db : Session = Depends(get_db), current_user : UserIn = Depends(get_current_user)):
    return user.create_user(db,request)
Base.metadata.create_all(engine)
