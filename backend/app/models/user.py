from database import Base
from sqlalchemy import Column, String, Integer


class UserModel(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    hash_password = Column(String, index=False)