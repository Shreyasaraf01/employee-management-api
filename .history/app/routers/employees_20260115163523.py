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

@router.get("/", response_model=List[schemas.EmployeeResponse])
def list_employees(
    page: int = 1,
    department: str | None = None,
    role: str | None = None,
    db: Session = Depends(get_db)
):
    if page < 1:
        raise HTTPException(status_code=400, detail="Page must be >= 1")

    skip = (page - 1) * 10
    return crud.get_employees(
        db,
        skip=skip,
        limit=10,
        department=department,
        role=role
    )
@router.get("/{employee_id}", response_model=schemas.EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )
    return employee

@router.put("/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    employee_id: int,
    data: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):
    employee = crud.update_employee(db, employee_id, data)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )
    return employee

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    success = crud.delete_employee(db, employee_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )
