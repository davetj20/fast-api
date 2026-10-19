from passlib.context import CryptContext

pwd_hash = CryptContext(schemes=["bcrypt"] , deprecated = "auto")

def phash(password):
    return pwd_hash.hash(password)

def pverify(lpass, hpass):
    return pwd_hash.verify(lpass,hpass)