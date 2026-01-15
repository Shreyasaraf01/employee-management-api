from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import auth

app = FastAPI(title="Employee Management API")

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Employee Management API is running"}
