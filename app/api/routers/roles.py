from app.schemas.role_user_schema import RoleUserIn, RoleUserOut
from app.schemas.role_schema import RoleSchemaOut, RoleSchemaIn
from app.services.functions import *
from app.infra.postgres.models.roles import *
from app.infra.services.role_user_service import role_user_service
from app.infra.services.role_service import role_service
from fastapi import APIRouter
from typing import List


router = APIRouter(
    prefix="/roles",
    tags={"roles"},
    responses={404: {"description": "not found"}}
)

#current_user = get_current_active_user


@router.post("", response_model=RoleSchemaOut)
async def role_create(rol: RoleSchemaIn):#, authenticate=Depends(current_user)):
    role_object = await role_service.create(rol)
    return role_object


@router.get('')
async def get_roles():
    Roles = await role_service.get_all(payload=None, skip=0, limit=30)
    return Roles


@router.get('/{role_id}/users',response_model=List[RoleUserOut])
async def get_users_rol(role_id: int):#,authenticate=Depends(current_user)):
    role = await role_service.get_by_id(role_id)
    if role is None:
        raise HTTPException(status_code=404, detail=f"role {role_id} not found")
    role_users= await role_user_service.get_relation_by_role(role_id)
    return role_users

@router.get('/relation', response_model=List[RoleUserOut])
async def get_role_relation():#authenticate=Depends(current_user)):
    obj_relation = await role_user_service.get_relation()
    return obj_relation


@router.put('/{role_id}')
async def update_role(
        role: RoleSchemaIn, role_id: int):#, authenticate=Depends(current_user)):
    role_obj = await Role.filter(id=role_id).update(**role.dict(
        exclude_unset=True
        ))
    return role_obj


@router.put('/{role_id}/users/{user_id}',response_model=List[RoleUserOut])
async def add_user_to_role(role_id:int, user_id:int):#,authenticate=Depends(current_user)):
    relation = RoleUserIn(user_id=user_id, role_id=role_id)
    await role_user_service.create(obj_in=relation)
    user_new = await role_user_service.get_relation_by_role(role_id)
    return user_new


@router.delete('/{role_id}')
async def delete_role(role_id: int):#, authenticate=Depends(current_user)):
    delete_roleid = await Role.filter(id=role_id).delete()
    if not delete_roleid:
        raise HTTPException(status_code=400,
                            detail=f"role {role_id} not found"
                            )
    return (f"delete role {role_id}")


@router.delete('/{role_id}/users/{user_id}')
async def delete_rol_user(role_id: int,user_id:int,
                        #authenticate=Depends(current_user)
                        ):
    relation = await role_user_service.get_one_relation(role_id, user_id)
    obj_relation = relation[0]
    await role_user_service.delete(obj_relation.id)
    return (f"the user {user_id} was delete from the role {role_id}")
