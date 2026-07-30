from fastapi import APIRouter, Depends
from services import PriceService
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter()

@router.get("/")
def get_responce(db: Session = Depends(get_db)):
    return PriceService(db).get_all_prices()

@router.post("/")
def create_price(db: Session = Depends(get_db)):
    PriceService(db).create_price()