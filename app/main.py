
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import auth, posts, users, vote

#models.Base.metadata.create_all(bind=engine)



app = FastAPI()

orgins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_orgins=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.routers)
app.include_router(users.routers)
app.include_router(auth.routers)
app.include_router(vote.routers)




