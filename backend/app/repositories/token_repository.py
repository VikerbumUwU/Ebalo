from sqlalchemy.orm import Session
from models.token import RefreshTokenModel

class TokerRepository():
    def __init__(self, db: Session):
        self.db: Session

    def create_token(self, token: RefreshTokenModel) -> RefreshTokenModel:
        self.db.add(token)

        self.db.commit()
        self.db.refresh(token)

        return token

    def get_token_by_id(self, id: int):
        self.db.get(RefreshTokenModel, id)

    def get_token_by_user_id(self, id: int) -> list[RefreshTokenModel]:
            self.db.query(RefreshTokenModel).filter(RefreshTokenModel.user_id == id).all()