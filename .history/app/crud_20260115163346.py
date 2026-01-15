from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from app import models, schemas


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        role=employee.role,
    )
    db.add(db_employee)
    try:
        db.commit()
        db.refresh(db_employee)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee with this email already exists",
        )
    return db_employee


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employees(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    department: str | None = None,
    role: str | None = None,
):
    query = db.query(models.Employee)

    if department:
        query = query.filter(models.Employee.department == department)
    if role:
        query = query.filter(models.Employee.role == role)

    return query.offset(skip).limit(limit).all()


def update_employee(db: Session, employee_id: int, data: schemas.EmployeeUpdate):
    employee = get_employee(db, employee_id)
    if not employee:
        return None

    if data.name is not None:
        employee.name = data.name
    if data.department is not None:
        employee.department = data.department
    if data.role is not None:
        employee.role = data.role

    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: int):
    employee = get_employee(db, employee_id)
    if not employee:
        return None
    db.delete(employee)
    db.commit()
    return True
