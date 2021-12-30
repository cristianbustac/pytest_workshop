from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.users import UserIn 
from app.schemas.user_schema import UserInSchema


class User(CRUDBase[UserIn, UserInSchema, UserInSchema]):
    ... 

crud_user = User(model=UserIn)
