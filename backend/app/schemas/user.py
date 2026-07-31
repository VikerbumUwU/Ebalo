from pydantic import BaseModel, EmailStr, ConfigDict

class User(BaseModel):
    name: str

class UserCreate(User):
    email: EmailStr
    password: str

class UserMeResponse(User):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class UserPublicResponse(User):
    id: int
    model_config = ConfigDict(from_attributes=True)