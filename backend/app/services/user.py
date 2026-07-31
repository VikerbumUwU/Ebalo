from sqlalchemy.orm import Session
from models.user import UserModel

from repositories.user_repository import UserRepository
from schemas.user import UserMeResponse, UserCreate


class UserService():
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        