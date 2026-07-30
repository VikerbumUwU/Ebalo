from pydantic import BaseModel, EmailStr, ConfigDict

class User(BaseModel):
    name: str

class UserCreate(User):
    email: EmailStr
    password: str

class UserLogin(User):
    email: EmailStr
    password: str

class UserResponce(User):
    model_config = ConfigDict(from_attributes=True)