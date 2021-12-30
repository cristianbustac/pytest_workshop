from app.infra.services.base_service import BaseService
from app.infra.postgres.crud.role_users import crud_role_users

class RoleUsersService (BaseService):
    async def get_relation(self):
        object_relation = await self._queries.get_relation()
        return object_relation
    
    async def get_relation_by_user(self,user_id):
        relation_by_user = await self._queries.get_relation_by_user(user_id)
        return relation_by_user
    
    async def get_relation_by_role(self,role_id):
        relation_by_role = await self._queries.get_relation_by_role(role_id)
        return relation_by_role
    
    async def get_one_relation(self,role_id,user_id):
        one_relation = await self._queries.get_one_relation(role_id,user_id)
        return one_relation

role_user_service = RoleUsersService(crud=crud_role_users)
