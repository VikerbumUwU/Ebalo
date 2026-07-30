from sqlalchemy.orm import Session
from models.user import UserModel


class UserRepository():
    def __init__(self, db:Session):
        self.db: Session = db

    def create_user(self, user: UserModel) -> UserModel:
        self.db.add(user)

        self.db.commit()
        self.db.refresh(user)

        return user

    def get_user_by_id(self, id: int) -> UserModel:
        return self.db.get(UserModel, id)

    def get_user_by_email(self, name: str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.name == name).first()