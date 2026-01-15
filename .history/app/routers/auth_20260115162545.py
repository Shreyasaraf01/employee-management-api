from fastapi import APIRouter, HTTPException, status
from datetime import timedelta
from app.auth import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

# Dummy user
FAKE_USER = {
    "username": "admin",
    "hashed_password": hash_password("admin123")
}


@router.post("/login")
def login(username: str, password: str):
    if username != FAKE_USER["username"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    if not verify_password(password, FAKE_USER["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token(
        data={"sub": username},
        expires_delta=timedelta(minutes=60)
    )

    return {"access_token": access_token, "token_type": "bearer"}
