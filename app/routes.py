from fastapi import APIRouter
from app.controllers.health import health_router
from app.controllers.auth import auth_router

api_router = APIRouter()
api_router.include_router(health_router,prefix="", tags=["Healthcheck"])
api_router.include_router(auth_router,prefix="", tags=["Authentication"])