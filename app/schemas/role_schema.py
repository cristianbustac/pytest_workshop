from app.schemas.user_schema import *


class RoleSchemaOut(BaseModel):
    id: int
    name_role: str
    description: str


class RoleSchemaIn(BaseModel):
    name_role: str
    description: str


class RoleId (UserInSchema):
    role_id: int
