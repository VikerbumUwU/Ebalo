from fastapi import FastAPI
from routes import tests_router

app = FastAPI()

app.include_router(
    tests_router,
    prefix="/tests",
    tags=["users"]
)

@app.get("/")
def home():
    return {"Hello": "world"}