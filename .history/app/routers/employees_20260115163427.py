from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.database import get_db
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"],
    dependencies=[Depends(get_current_user)]
)
@router.post("/", response_model=schemas.EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    if not employee.name.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Name cannot be empty",
        )
    return crud.create_employee(db, employee)
