

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text

from .database import Base


class Post (Base):
    __tablename__ = "posts"
    id = Column(Integer , primary_key= True , nullable=False)
    title = Column(String , nullable= False)
    content = Column(String , nullable= False)
    published = Column(Boolean , nullable= True , server_default= 'True')
    like = Column(Integer , nullable= True , server_default= '0' )
    time = Column(TIMESTAMP(timezone=True),nullable=False , server_default=text('now()'))


class Users (Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key= True , nullable=False)
    time = Column(TIMESTAMP(timezone=True),nullable=False , server_default=text('now()'))
    email = Column(String , nullable= False , unique= True)
    password = Column(String , nullable= False)     
    