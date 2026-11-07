
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas
from ..database import get_db

routers = APIRouter(prefix="/vote" , tags= ["Votes"])

@routers.post("/", status_code = status.HTTP_201_CREATED)
def post_vote(vote : schemas.Vote ,user:schemas.Users = Depends(oauth2.get_current_user), db: Session = Depends(get_db) ):  # noqa: B008
    if db.query(models.Post).filter(models.Post.id == vote.post_id).first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="post does not exist")
    q_obj= db.query(models.Votes).filter(models.Votes.post_id == vote.post_id , models.Votes.user_id == user.id)
    v_obj = q_obj.first()
    if v_obj :
        if vote.diff == 1:
            raise HTTPException(status_code = status.HTTP_403_FORBIDDEN , detail="Post Cant be Liked Twice")
        else :
            db.delete(v_obj)
            db.commit()
    else :
        if vote.diff == 1 :
            v_obj=models.Votes(post_id =vote.post_id, user_id = user.id)
            db.add(v_obj)
            db.commit()
        else:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail="user has not liked on this post")


