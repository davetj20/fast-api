

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from .database import Base


class Users (Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key= True , nullable=False)
    time = Column(TIMESTAMP(timezone=True),nullable=False , server_default=text('now()'))
    email = Column(String , nullable= False , unique= True)
    password = Column(String , nullable= False)     


class Post (Base):
    __tablename__ = "posts"
    id = Column(Integer , primary_key= True , nullable=False)
    title = Column(String , nullable= False)
    content = Column(String , nullable= False)
    published = Column(Boolean , nullable= True , server_default= 'True')
    like = Column(Integer , nullable= True , server_default= '0' )
    time = Column(TIMESTAMP(timezone=True),nullable=False , server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    user = relationship(Users)


class Votes (Base):
    __tablename__ ="votes" 
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, nullable=False)
