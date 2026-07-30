from sqlalchemy import Column, Integer, String
from database import Base

class Price(Base):
    __tablename__ = "Prices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)

