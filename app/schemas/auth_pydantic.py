from pydantic import BaseModel

class AuthRequest(BaseModel):
    """Request schema for auth API"""
    user_id:int

class AuthResponse(BaseModel):
    """Request schema for auth API"""
    status_code:int
    message:str