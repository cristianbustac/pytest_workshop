from pydantic.main import BaseModel
from app.schemas.role_schema import RoleSchemaIn
from app.schemas.user_schema import UserOutSchema


class RoleUserOut (BaseModel):
    id: int
    user: UserOutSchema 
    role:  RoleSchemaIn
    
    class Config:
        orm_mode = True


class RoleUserIn (BaseModel):
    user_id: int 
    role_id: int