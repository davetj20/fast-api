from datetime import UTC, datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app import database, models, schemas
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_token(data:dict):
    to_encode = data.copy() 

    expire = datetime.now(UTC) + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({ "exp" : expire})

    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , ALGORITHM)

    return encoded_jwt

def verify_token(token : str , credentials_exception):
    try:
        decoded_token = jwt.decode(token , SECRET_KEY , [ALGORITHM])
        id = decoded_token.get("user_id")
        if id is None :
            raise  credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError :
        raise credentials_exception
    return token_data


def get_current_user(token:str = Depends(oauth2_scheme) , db: Session = Depends(database.get_db)):  # noqa: B008
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="could not validate " , headers={"WWW-AUthenticate" : "Bearer"} )


    token= verify_token( token , credentials_exception = credentials_exception)
    user = db.query(models.Users).filter(models.Users.id == token.id ).first()

    return user

