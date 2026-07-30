from database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hash_password = Column(String, index=False)