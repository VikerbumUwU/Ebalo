from sqlalchemy.orm import Session
from repositories import PriceRepository


class PriceService():
    def __init__(self, db: Session):
        self.repository = PriceRepository(db)

    def get_all_prices(self) -> str: #!!!!!!!!!!!!!Это фейк не все!!!!!!!!!!!!!!!
        return self.repository.get_all_prices()[0].name

    def create_price(self):
        self.repository.create_price()