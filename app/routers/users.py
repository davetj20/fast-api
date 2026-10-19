import typing

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import models, schemas, utils
from ..database import get_db

routers = APIRouter(prefix="/users" , tags= ["Users"])

@routers.get("/{id}", response_model= schemas.Respsonse_Users)
def get_user(id:int , db:Session= Depends(get_db)):  # noqa: B008
    user_temp = db.query(models.Users).filter(models.Users.id==id).first()
    return user_temp

@routers.get("/", response_model= typing.List[schemas.Respsonse_Users])  # noqa: UP006
def get_all_users(db:Session=Depends(get_db)):  # noqa: B008
    return db.query(models.Users).all()

@routers.post("/", response_model= schemas.Respsonse_Users)
def create_user(user:schemas.Users, db:Session=Depends(get_db)):  # noqa: B008
    user.password = utils.phash(user.password)
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@routers.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user( id:int , db:Session=Depends(get_db)):  # noqa: B008
    user = db.query(models.Users).filter(models.Users.id==id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Post with{id} not found ")
    db.delete(user)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@routers.put("/", response_model= schemas.Respsonse_Users)
def update_users( id: int , users: schemas.Users , db:Session=Depends(get_db)):  # noqa: B008
    u_query = db.query(models.Users).filter(models.Users.id == id)
    u = u_query.first()
    if u is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Post with{id} not found ")
    u_query.update(users.dict(), synchronize_session= False)
    db.commit()
    db.refresh(u)
    return u 

