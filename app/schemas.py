from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class Post(BaseModel):
    title: Optional[str]= None  # noqa: UP045
    content: str | None = None
    like: int | None=None
    published:bool | None= None 



class Users(BaseModel):
    email: Optional[EmailStr]= None  # noqa: UP045
    password: str | None = None


class Respsonse_Users(BaseModel):
    email: EmailStr | None= None
    id:int
    time:datetime
    class Config:
        orm= True
        arbitrary_types_allowed=True  



class Respsonse_Post(Post):
    id:int
    time:datetime
    user_id: int
    user : Respsonse_Users
    class Config:
        orm= True
        arbitrary_types_allowed=True



class Token(BaseModel):
    access_token :str 
    token_type:str


class TokenData(BaseModel):
    id: int|None = None
    


class Vote(BaseModel):
    post_id:int
    diff:conint(ge=-1,le=1) # type: ignore


class RPost_With_Vote(BaseModel):
    Post:Respsonse_Post
    vote:int
    class Config:
        orm= True
        arbitrary_types_allowed=True

