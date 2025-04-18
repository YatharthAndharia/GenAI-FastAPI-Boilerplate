import os
import time
import jwt
from typing import Optional
from app.utils.constants import StaticMessages


class AuthService:
    def __init__(
        self,
        secret: Optional[str] = None,
        algorithm: Optional[str] = None,
        expiry_seconds: int = 600
    ):
        self.secret = secret or os.getenv("JWT_SECRET")
        self.algorithm = algorithm or os.getenv("JWT_ALGORITHM")
        self.expiry_seconds = expiry_seconds

    def sign_jwt(self, user_id: int) -> str:
        try:
            payload = {
                "user_id": user_id,
                "expires": time.time() + self.expiry_seconds
            }
            token = jwt.encode(payload, self.secret, algorithm=self.algorithm)
            return token
        except Exception as e:
            raise Exception(f"JWT Signing Error: {str(e)}")

    def decode_jwt(self, token: str) -> Optional[dict]:
        try:
            decoded_token = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            if decoded_token["expires"] >= time.time():
                return decoded_token
        except jwt.ExpiredSignatureError:
            raise Exception(StaticMessages.JWT_TOKEN_EXPIRED_MESSAGE)
        except jwt.InvalidTokenError:
            raise Exception(StaticMessages.INVALID_JWT_TOKEN_MESSAGE)
        except Exception as e:
            raise Exception(f"JWT Decoding Error: {str(e)}")
