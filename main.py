from fastapi import FastAPI,Depends
from schemas.user import UserIn,UserOut
from db.database import engine,Base,get_db
from sqlalchemy.orm import Session
from crud import user

app=FastAPI()

@app.post("/create_user", response_model=UserOut)
def create_user(request:UserIn, db : Session = Depends(get_db)):
    return user.create_user(db,request)
Base.metadata.create_all(engine)
