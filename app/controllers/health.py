from fastapi import APIRouter,Request
from fastapi.responses import JSONResponse


health_router = APIRouter()

@health_router.get("/health")
async def healthcheck():
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "detail": "ok"
        }
    )
