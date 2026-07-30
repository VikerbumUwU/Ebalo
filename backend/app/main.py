from fastapi import FastAPI
from routes import tests_router, prices_router

import uvicorn

app = FastAPI()

app.include_router(
    tests_router,
    prefix="/tests",
    tags=["users"]
)

app.include_router(
    prices_router,
    prefix="/prices",
    tags=["prices"]
)

@app.get("/")
def home():
    return {"Hello": "world"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)