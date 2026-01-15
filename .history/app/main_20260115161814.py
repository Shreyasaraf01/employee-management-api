from fastapi import FastAPI

app = FastAPI(title="Employee Management API")

@app.get("/")
def root():
    return {"message": "Employee Management API is running"}
