from datetime import datetime
from pydantic.main import BaseModel


class ProjectIn(BaseModel):
    name_project : str
    start_date : datetime
    end_date : datetime
    backend_leader : str
    frontend_leader : str

class ProjectOut(ProjectIn):
    id : int
