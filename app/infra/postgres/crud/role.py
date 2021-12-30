from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.roles import Role
from app.schemas.role_schema import RoleSchemaIn


class RoleCB(CRUDBase[Role, RoleSchemaIn, RoleSchemaIn]):
    ...

crud_role = RoleCB(model=Role)
