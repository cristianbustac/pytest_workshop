from fastapi import APIRouter
from app.api.routers import users
from app.api.routers import roles
from app.api.routers import projects

router = APIRouter()

router.include_router(users.router)
router.include_router(roles.router)
router.include_router(projects.router)