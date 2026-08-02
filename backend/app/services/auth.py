from sqlalchemy.orm import Session
from schemas.token import AccessTokenPayload
from argon2 import PasswordHasher
from schemas.user import UserCreate, UserMeResponse
from schemas.auth import LoginRequest, LoginResponse, LoginErrorResponse
from models.user import UserModel
from repositories.user_repository import UserRepository
import jwt
from config import settings
from services.token import TokenService
from services.user import UserService

class AuthService():
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

        self.user_service = UserService(db)
        self.token_service = TokenService(db)

        self.ph = PasswordHasher(
            time_cost=3,
            memory_cost=8192,
            parallelism=1
        )

    def register(self, user: UserCreate) -> str:
        user_model = UserModel(
            hash_password = self.ph.hash(user.password),
            name = user.name,
            email = user.email
        )

        id = self.repository.create_user(user_model).id

        return self.token_service.create_access_token(AccessTokenPayload(sub = id))

    def login(self, login: LoginRequest) -> LoginResponse | LoginErrorResponse:
        user = self.repository.get_user_by_email(login.email)

        if user.hash_password == self.ph.hash(login.password):
            token = self.token_service.create_access_token(AccessTokenPayload(sub = user.id))
            return LoginResponse(user = UserMeResponse(user), token=token)
        else:
            return LoginErrorResponse(code=401, message="Invalid password")


    




