from fastapi.exceptions import HTTPException
from app.schemas.user_project_schema import ProjectUserIn, ProjectUserOut
from app.schemas.project_schema import ProjectIn,ProjectOut
from app.infra.postgres.models.projects import Project
from app.infra.services.project_service import project_service
from app.infra.services.user_project_service import user_project_service
from app.services.functions import *
from fastapi import APIRouter
from typing import List

router = APIRouter(
    prefix="/projects",
    tags={"projects"},
    responses={404: {"description": "not found"}}
)

#current_user = get_current_active_user

@router.post("", response_model=ProjectOut)
async def project_create(project:ProjectIn):
    project_obj = await project_service.create(project)
    return project_obj

@router.get('')
async def get_projects():
    projects = await project_service.get_all(payload={}, skip=0, limit=30)
    return projects

@router.get('/{project_id}/users',response_model=List[ProjectUserOut])
async def get_users_project(project_id: int):#,authenticate=Depends(current_user)):
    project = await project_service.get_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail=f"project {project_id} not found")
    project_users= await user_project_service.get_relation_by_project(project_id)
    return project_users

@router.get('/relation', response_model=List[ProjectUserOut])
async def get_project_relation():
    obj_relation = await user_project_service.get_relation()
    return obj_relation


@router.put('/{project_id}')
async def update_project(project_id:int,project:ProjectIn):
    project_obj = await project_service.update(id=project_id,obj_in=project)
    return project_obj

@router.put('/{project_id}/users/{user_id}',response_model=List[ProjectUserOut])
async def add_user_to_project(project_id:int, user_id:int):#,authenticate=Depends(current_user)):
    relation = await user_project_service.get_one_relation(project_id,user_id)
    await user_project_service.create(obj_in=relation)
    user_new = await user_project_service.get_relation_by_project(project_id)
    return user_new

@router.delete('/{project_id}')
async def delete_role(project_id:int):
    project_obj = await project_service.delete(id=project_id)
    if not project_obj:
        raise HTTPException(
            status_code=400,
            detail=f"project {project_id} not found"
                            )
    return (f"delete project {project_id}")


@router.delete('/{project_id}/users/{user_id}')
async def delete_project_user(project_id: int,user_id:int,
                        #authenticate=Depends(current_user)
                        ):
    relation = await user_project_service.get_one_relation(project_id, user_id)
    obj_relation = relation[0]
    await user_project_service.delete(obj_relation.id)
    return (f"the user {user_id} was delete from the role {project_id}")
