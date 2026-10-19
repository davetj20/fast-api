from datetime import datetime, timedelta

from jose import JWTError, jwt  # noqa: F401

SECRET_KEY = "heLLO"
ALGORITHIM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_token(data:dict):
    to_encode = data.copy() 

    expire = datetime.now() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({ "exp" : expire})

    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , ALGORITHIM )

    return encoded_jwt




