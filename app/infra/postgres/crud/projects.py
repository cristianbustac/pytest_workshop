from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.projects import Project
from app.schemas.project_schema import ProjectIn


class ProjectCB(CRUDBase[Project, ProjectIn, ProjectIn]):
    ...

crud_project = ProjectCB(model=Project)
