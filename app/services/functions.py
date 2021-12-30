from app.infra.postgres.models.users import UserIn
from app.schemas.user_schema import TokenData
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
#from jose import JWTError, jwt
from datetime import datetime, timedelta
import time
from app.infra.postgres.models import *
from app.schemas import *
from typing import Optional
from app.infra.services.role_service import role_service


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/login")
SECRET_KEY = "91ee5632dd2e2f8066709f419184b7376f9bc84b38901118142f42bec9d45067"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# async def get_current_user(token: str=Depends(oauth2_scheme)):
#     credentials_exceptions = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"})
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exceptions
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exceptions
#     user = await get_user(UserIn, username=token_data.username)
#     if user is None:
#         raise credentials_exceptions
#     return user


# async def get_current_active_user(
#     current_user: UserIn=Depends(get_current_user)
#                                 ):
#     if current_user.permission:
#         return current_user
#     raise HTTPException(
#         status_code=400,
#         detail="the user does not have permissions"
#                         )


async def get_user(DB, username: str):
    user_in = await DB.get(email=username)
    if not user_in:
        raise HTTPException(status_code=400, detail="user is not in DB")
    return user_in


# def create_access_token(data: dict, expires_delta: Optional[timedelta]=None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encode_jwt

async def authenticate_user(DB, username: str, password: str):
    user = await get_user(DB, username)
    if not user:
        return False
    if not Verify_Pwd(password, user.password):
        return False
    return user


def pwd_encrip(password):
    return pwd_context.hash(password)


def Verify_Pwd(password, password_encrip):
    return pwd_context.verify(password, password_encrip)

async def verify_role(role_id):
    role = await role_service.get_by_id(role_id)
    if not role :
        return False
    return True

class Expensive():
    def expensive_api_call(self):
        time.sleep(1000) # takes 1,000 seconds
        return "hello_world"