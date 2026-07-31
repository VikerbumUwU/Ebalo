from fastapi import APIRouter, Depends
from schemas.user import UserCreate
from database import get_db
from services.auth import AuthService

route = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@route.post("/register")
def register(user: UserCreate, db = Depends(get_db)):
    return AuthService(db).Register(user)