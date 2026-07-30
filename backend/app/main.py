from fastapi import FastAPI, Depends
from database import init_db, get_db
import uvicorn
from schemas.user import UserResponce, UserCreate
from sqlalchemy.orm import Session
from services.user import UserService


app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def home():
    return {"Hello": "world"}

@app.post("/user", response_model=UserResponce)# потестить, потом в роутер
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)