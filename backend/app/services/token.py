from sqlalchemy.orm import Session
from repositories.token_repository import TokerRepository
from schemas.token import AccessTokenPayload
import jwt
from config import settings


class TokenService():
    def __init__(self, db: Session):
        self.repository = TokerRepository(db)

    def create_access_token(self, payload: AccessTokenPayload) -> str:
        return jwt.encode(payload.model_dump(), settings.jwt_key, algorithms=["HS256"])

    def check_access_token(self, token: str) -> int | None:
        try: return jwt.decode(token, settings.jwt_key, algorithms=["HS256"])["sub"]
        except: return None

    def create_refresh_token(self):
        ...

    def check_refresh_token(self):
        ...