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
