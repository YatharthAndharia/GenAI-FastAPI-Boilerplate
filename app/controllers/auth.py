from fastapi import APIRouter,Request,status,Response
from fastapi.responses import JSONResponse
from app.middlewares.jwt_auth import AuthService
from app.schemas.auth_pydantic import AuthRequest,AuthResponse

auth_service=AuthService()

auth_router=APIRouter()
@auth_router.post("/get-token",response_model=AuthResponse)
async def sign_token(
    request:Request,
    request_params:AuthRequest,
    response:Response
):
    try:
        user_id=request_params.user_id
        jwt_token=auth_service.sign_jwt(user_id=user_id)
        return AuthResponse(
            status_code=status.HTTP_200_OK,
            message=jwt_token
        )
    except Exception as e:
        response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        return AuthResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e)
        )
    