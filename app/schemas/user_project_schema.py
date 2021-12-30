from pydantic.main import BaseModel
from app.schemas.user_schema import UserOutSchema
from app.schemas.project_schema import ProjectOut

class ProjectUserOut(BaseModel):
    id : int
    user: UserOutSchema
    project: ProjectOut
    
    class config:
        orm_mode = True


class ProjectUserIn(BaseModel):
    user_id: int 
    project_id: int