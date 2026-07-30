from sqlalchemy.orm import Session
from models import Price
from typing import List

class PriceRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_all_prices(self) -> List[Price]:
        return self.db.query(Price).all()
    
    def create_price(self) -> None:
        price = Price(
            name = "Бургер",
            price = 1000
        )
        self.db.add(price)
        self.db.commit()
