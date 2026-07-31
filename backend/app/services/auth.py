from sqlalchemy.orm import Session
from schemas.token import AccessTokenPayload
from argon2 import PasswordHasher
from schemas.user import UserCreate
from schemas.token import AccessTokenPayload
from models.user import UserModel
from repositories.user_repository import UserRepository
import jwt
from config import settings

class AuthService():
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        self.ph = PasswordHasher(
            time_cost=3,
            memory_cost=8192,
            parallelism=1
        )

    def Register(self, user: UserCreate) -> str: # не очень красиво я хз
        user_model = UserModel(
            hash_password = self.ph.hash(user.password),
            name = user.name,
            email = user.email
        )

        id = self.repository.create_user(user_model).id

        return jwt.encode(AccessTokenPayload(sub=id).model_dump(), settings.jwt_key, algorithm="HS256")




