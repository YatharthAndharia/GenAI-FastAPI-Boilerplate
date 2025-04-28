from fastapi import APIRouter,Request,status,Response,Depends
from fastapi.responses import JSONResponse
from app.utils.jwt_auth import AuthService
from app.schemas.auth_pydantic import AuthRequest,AuthResponse
from app.session import SessionDep
from sqlalchemy import text


auth_service=AuthService()


auth_router=APIRouter()
@auth_router.post("/sign-in",response_model=AuthResponse)
async def sign_in(
    request_params:AuthRequest,
    response:Response,
    session:SessionDep
):
    try:
        sql=text("SELECT * FROM public.user")
        result=session.exec(sql)
        users=result.all()
        print(users)
        email=request_params.email
        password=request_params.password
        jwt_token=auth_service.sign_jwt(email=email)
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
    