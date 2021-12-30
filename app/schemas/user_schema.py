from pydantic.main import BaseModel
from typing import Optional


class UserOutSchema(BaseModel):
    id: int
    name: str
    lastname: str
    document_id : int
    address : str
    email : str
    role_id: int
    permission: bool = False
    
    class Config: 
        orm_mode = True


class UserInSchema(BaseModel):
    name: str
    lastname: str
    document_id :int
    address: str
    password: str
    email: str
    permission: bool = False


class TokenData(BaseModel):
    username: Optional[str]=None


class Token(BaseModel):
    access_token : str
    token_type : str