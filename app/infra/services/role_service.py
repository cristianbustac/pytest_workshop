from app.infra.services.base_service import BaseService
from app.infra.postgres.crud.role import crud_role


class RoleService (BaseService):
    ...

role_service = RoleService(crud=crud_role)