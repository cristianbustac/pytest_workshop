from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.role_users import RoleUsers
from app.schemas.role_user_schema import RoleUserIn


class RoleUserRelation (CRUDBase[RoleUsers, RoleUserIn, RoleUserIn]):
    async def get_relation(self):
        obj_role = await self.model.all().prefetch_related('role', 'user')
        if obj_role is None:
            return None
        return obj_role
    
    async def get_relation_by_user(self, user_id: int):
        obj_user_id = await self.model.filter(user_id=user_id).prefetch_related('role', 'user')
        if obj_user_id is None:
            return None
        return obj_user_id
    
    async def get_relation_by_role(self, role_id:int):
        obj_role_id = await self.model.filter(role_id=role_id).prefetch_related('role', 'user')
        if obj_role_id is None:
            return None
        return obj_role_id

    async def get_one_relation(self, role_id:int,user_id:int):
        obj_relation = await self.model.filter(role_id=role_id, user_id=user_id).prefetch_related('role', 'user')
        if obj_relation is None:
            return None
        return obj_relation



crud_role_users = RoleUserRelation(model=RoleUsers)
