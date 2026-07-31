from pydantic import BaseModel, EmailStr
from schemas.user import UserMeResponse
from schemas.token import AccessTokenPayload


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    token: AccessTokenPayload
    user: UserMeResponse

class LoginErrorResponse(BaseModel):
    code: str
    message: str