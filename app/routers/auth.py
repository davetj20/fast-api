from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import oauth2

from .. import database, models, schemas, utils  # noqa: F401

routers = APIRouter(tags=["Authentication"])

@routers.post("/login")
def login(user:OAuth2PasswordRequestForm = Depends() , db:Session= Depends (database.get_db)):  # noqa: B008
    user_obj = db.query(models.Users).filter(models.Users.email == user.username).first()
    if user_obj is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="INVALID CREDENTIALS")
    if not (utils.pverify(user.password , user_obj.password) ):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="INVALID CREDENTIALS")
    else :
        token = oauth2.create_token( {"user_id" :user_obj.id})
        return {"access_token": token, "token_type": "bearer"}


