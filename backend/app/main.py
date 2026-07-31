from fastapi import FastAPI
from database import init_db
import uvicorn
from routes.auth import route as auth_route

app = FastAPI()

app.include_router(
    auth_route
)


@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def home():
    return {"Hello": "world"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


