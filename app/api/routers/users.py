from app.schemas.role_user_schema import RoleUserIn, RoleUserOut
from app.schemas.user_project_schema import ProjectUserIn, ProjectUserOut
from app.schemas.role_schema import RoleId
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from tortoise.contrib.fastapi import HTTPNotFoundError
from app.schemas.user_schema import Token, UserOutSchema
from app.infra.services.user_service import user_service
from app.infra.services.role_user_service import role_user_service
from app.infra.services.user_project_service import user_project_service
from app.infra.postgres.models.users import *
from app.services.functions import *
from typing import List

router = APIRouter(
    prefix="/users",
    tags={"users"},
    responses={404: {"description": "not found"}}
)

#current_user = get_current_active_user

@router.post('', response_model=UserOutSchema)
async def user(user: RoleId):#, authorized=Depends(current_user)):
    role = await verify_role(user.role_id)
    if role is True :
        Passwd = pwd_encrip(user.password)
        user.password = Passwd
        if user.role_id == 1 :
            user.permission= True
        user_new = await user_service.create(user)
        relation = RoleUserIn(user_id=user_new.id, role_id=user.role_id)
        await role_user_service.create(obj_in=relation)
        return user_new
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="the role does not exist ",
        )

@router.put("/{user_id}/roles/{role_id}",response_model=List[RoleUserOut])
async def add_rol_to_user(user_id:int, role_id:int):#,authenticate=Depends(current_user)):
    relation = RoleUserIn(user_id=user_id, role_id=role_id)
    await role_user_service.create(obj_in=relation)
    rol_new = await role_user_service.get_relation_by_user(user_id)
    return rol_new


# @router.post("/login", response_model=Token)
# async def login(form_data: OAuth2PasswordRequestForm=Depends()):
#     email = form_data.username
    
#     user = await authenticate_user(
#         UserIn,
#         email,
#         form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={'WWW-Authenticate': "Bearer"}
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.email},
#         expires_delta=access_token_expires
#         )
#     return {"access_token": access_token, "token_type": "bearer"}


@router.get('', response_model=List[UserOutSchema])
async def users():#(authorized=Depends(current_user)):
    user_obj = await user_service.get_all(payload={}, skip=0, limit=30)
    return user_obj


@router.get('/{user_id}/Roles',
            responses={404: {"model": HTTPNotFoundError}},
            response_model=List[RoleUserOut]
            )
async def get_roles_user(user_id: int):#,authorized=Depends(current_user)):
    user = await user_service.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"user {user_id} not found")
    user_rol = await role_user_service.get_relation_by_user(user_id)
    return user_rol


@router.get('/{user_id}/Projects',
            responses={404: {"model": HTTPNotFoundError}},
            response_model=List[ProjectUserOut]
            )
async def get_projects_user(user_id: int):#,authorized=Depends(current_user)):
    user = await user_service.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"user {user_id} not found")
    user_project = await user_project_service.get_relation_by_user(user_id)
    return user_project


@router.put('')
async def update_user(
    user: UserOutSchema,
    user_id: int,
    #authorized=Depends(current_user)
                    ):
    user_obj = await user_service.update(user_id, user)
    return user_obj


@router.delete('')
async def delete_user(
    user_id: int,
    #authorized=Depends(current_user)
                    ):
    delete_user = await user_service.delete(user_id)
    if not delete_user:
        raise HTTPException(
            status_code=400,
            detail=f"user {user_id} not found"
                            )
    return (f"delete user {user_id}")

@router.delete('/{user_id}/roles/{role_id}')
async def delete_rol_user(role_id: int,user_id:int,
                        #authenticate=Depends(current_user)
                        ):
    relation = await role_user_service.get_one_relation(role_id, user_id)
    obj_relation = relation[0]
    await role_user_service.delete(obj_relation.id)
    return (f"the role {role_id} was delete from the user {user_id}")

@router.get("/time")
async def delayed ():
    api_call = Expensive()
    call = await api_call.expensive_api_call()
    return call