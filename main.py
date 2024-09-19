from fastapi import FastAPI
from db.database import engine,Base
from auth import authentication
from router import user

app=FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)

Base.metadata.create_all(engine)
