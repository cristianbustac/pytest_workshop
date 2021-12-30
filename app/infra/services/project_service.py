from app.infra.services.base_service import BaseService
from app.infra.postgres.crud.projects import crud_project

class ProjectService(BaseService):
    ... 

project_service = ProjectService(crud=crud_project)