import typing

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas
from ..database import get_db

routers = APIRouter(prefix="/posts" , tags=["Posts"])


@routers.get("/" , response_model= typing.List[schemas.Respsonse_Post])  # noqa: UP006
def total_posts(db:Session= Depends(get_db) , current_user: models.Users = Depends(oauth2.get_current_user)):  # noqa: B008
    print(current_user)
    post = db.query(models.Post).all()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="NO posts exist")
    return post




@routers.get("/{id}",status_code=status.HTTP_200_OK , response_model=schemas.Respsonse_Post )
def get_post(id:int , db:Session= Depends(get_db), user : int = Depends(oauth2.get_current_user)):  # noqa: B008
    print(user)
    p = db.query(models.Post).filter(models.Post.id== id).first()
    if p is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post not found with {id}")
    return p 



@routers.post("/" , status_code=status.HTTP_201_CREATED , response_model= schemas.Respsonse_Post )
def create_post(post:schemas.Post, db:Session= Depends(get_db), user : int = Depends(oauth2.get_current_user)):  # noqa: B008
    # cur.execute("""INSERT INTO posts(name,age,likes) VALUES (%s,%s,%s) RETURNING * """, (post.name,post.age,post.likes))
    # p= cur.fetchone()
    # conn.commit()
    p = models.Post(user_id = user.id ,**post.dict() )
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


@routers.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int , db:Session= Depends(get_db), user : int = Depends(oauth2.get_current_user)):  # noqa: B008
    # cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id)))
    # p = cur.fetchone()
    print(user)
    post = db.query(models.Post).filter(models.Post.id == id)
    p = post.first()
    if  p is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Post with{id} not found ")
    if p.user_id != user.id :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Invalid Credi=entials")
    db.delete(p)
    db.commit()
    return  Response(status_code=status.HTTP_204_NO_CONTENT)

@routers.put("/{id}", response_model= schemas.Respsonse_Post)
def update_post(id:int , post: schemas.Post, db:Session= Depends(get_db), user : int = Depends(oauth2.get_current_user)):  # noqa: B008
    p_query= db.query(models.Post).filter(models.Post.id == id)
    p = p_query.first()

    if  p  is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Post with{id} not found ")
    if p.user_id != user.id :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Invalid Credi=entials")
    p_query.update(post.dict(), synchronize_session= False)
    db.commit()
    db.refresh(p)
    return p 