from app.infra.services.base_service import BaseService
from app.infra.postgres.crud.user import crud_user

class UserService (BaseService):
    ...

user_service = UserService(crud=crud_user)
