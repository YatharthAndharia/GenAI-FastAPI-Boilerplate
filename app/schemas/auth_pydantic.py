from pydantic import BaseModel

class AuthRequest(BaseModel):
    """Request schema for auth API"""
    email:str
    password:str

class AuthResponse(BaseModel):
    """Request schema for auth API"""
    status_code:int
    message:str