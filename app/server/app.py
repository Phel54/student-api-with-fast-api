from fastapi import FastAPI

app = FastAPI()

from server.routes.student import router as StudentRouter

app.include_router(StudentRouter, tags=["Student"], prefix="/student")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}