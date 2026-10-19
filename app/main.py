
from fastapi import FastAPI

from app.routers import auth

from . import models
from .database import engine
from .routers import posts, users

models.Base.metadata.create_all(bind=engine)



app = FastAPI()

app.include_router(posts.routers)
app.include_router(users.routers)
app.include_router(auth.routers)




