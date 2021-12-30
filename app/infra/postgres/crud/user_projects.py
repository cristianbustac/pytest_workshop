from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.user_projects import UserProjects
from app.schemas.user_project_schema import ProjectUserIn


class UserProjectRelation (CRUDBase[UserProjects, ProjectUserIn, ProjectUserIn]):
    async def get_relation(self):
        obj_role = await self.model.all().prefetch_related('project', 'user')
        if obj_role is None:
            return None
        return obj_role
    
    async def get_relation_by_user(self, user_id: int):
        obj_user_id = await self.model.filter(user_id=user_id).prefetch_related('project', 'user')
        if obj_user_id is None:
            return None
        return obj_user_id
    
    async def get_relation_by_role(self, project_id:int):
        obj_role_id = await self.model.filter(project_id=project_id).prefetch_related('project', 'user')
        if obj_role_id is None:
            return None
        return obj_role_id

    async def get_one_relation(self, project_id:int,user_id:int):
        obj_relation = await self.model.filter(project_id=project_id, user_id=user_id).prefetch_related('project', 'user')
        if obj_relation is None:
            return None
        return obj_relation



crud_users_Projects = UserProjectRelation(model=UserProjects)
