from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.auth import authenticate_user, create_access_token, get_authorized_user, require_role
from database.session import get_db
from schemas.user import UserResponse


router = APIRouter(prefix="/auth", tags=["auth"])

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected")
async def protected_route(user: UserResponse = Depends(get_authorized_user)):
    return {"message": f"Access granted: {user.name} {user.surname}."}


@router.get("/student_access")
async def student_access(user: UserResponse = Depends(require_role(["STUDENT"]))):
    return {"message": f"Access granted to student: {user.name} {user.surname}."}


@router.get("/lecturer_access")
async def lecturer_access(user: UserResponse = Depends(require_role(["LECTURER"]))):
    return {"message": f"Access granted to lecturer: {user.name} {user.surname}."}


@router.get("/student_or_lecturer_access")
async def student_or_lecturer_access(user: UserResponse = Depends(require_role(["STUDENT", "LECTURER"]))):
    return {"message": f"Access granted to student or lecturer: {user.name} {user.surname}."}
