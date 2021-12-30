from app.infra.services.base_service import BaseService
from app.infra.postgres.crud.user_projects import crud_users_Projects

class UserProjectsService (BaseService):
    async def get_relation(self):
        object_relation = await self._queries.get_relation()
        return object_relation
    
    async def get_relation_by_user(self,user_id):
        relation_by_user = await self._queries.get_relation_by_user(user_id)
        return relation_by_user
    
    async def get_relation_by_project(self,project_id):
        relation_by_project = await self._queries.get_relation_by_project(project_id)
        return relation_by_project
    
    async def get_one_relation(self,project_id,user_id):
        one_relation = await self._queries.get_one_relation(project_id,user_id)
        return one_relation

user_project_service = UserProjectsService(crud=crud_users_Projects)
