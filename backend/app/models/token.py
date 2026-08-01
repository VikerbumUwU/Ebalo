from database import Base
from sqlalchemy import Column, String, Integer, DateTime

class RefreshTokenModel(Base):

    id = Column(Integer, primary_key= True, index=True),
    user_id = Column(Integer, index=True),
    token_hash = Column(String),
    created_at = Column(DateTime),
    expires_at = Column(DateTime)