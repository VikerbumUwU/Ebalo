from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin, UserResponce
from models.user import UserModel
from argon2 import PasswordHasher
from repositories.user_repository import UserRepository

class UserService():
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        self.ph = PasswordHasher(
            time_cost=3,
            memory_cost=16384,
            parallelism=1
        )

    def create_user(self, user_scheme: UserCreate) -> UserResponce:

        user_model = UserModel(
            name = user_scheme.name,
            email = user_scheme.email,
            hash_password = user_scheme.password
        )

        return UserResponce.model_validate(self.repository.create_user(user_model))