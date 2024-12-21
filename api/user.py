from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import services.user as service

from auth.auth import get_authorized_user, get_role_from_token
from database.session import get_db
from schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/user", response_model=UserResponse)
def get_user_auth(user=Depends(get_authorized_user), db: Session = Depends(get_db)):
    """
    Fetch the currently authenticated user based on their bearer token.
    """
    return service.get_user(db=db, user_id=user.id)


@router.get("/all", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    """
    Fetch all users from the database.
    """
    return service.get_all_users(db=db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), role=Depends(get_role_from_token)):
    """
    Fetch a user by their ID. Access depends on the user's role.
    """
    if role not in ["LECTURER", "STUDENT"]:
        raise HTTPException(status_code=403, detail="Unauthorized role")
    user = service.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the database.
    """
    existing_user = service.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered!"
        )
    return service.create_user(db, user)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db), role=Depends(get_role_from_token)):
    """
    Update a user's details. Only authorized roles can perform this action.
    """
    if role not in ["LECTURER"]:
        raise HTTPException(status_code=403, detail="Only lecturers can update users")
    updated_user = service.update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db), role=Depends(get_role_from_token)):
    """
    Delete a user by their ID. Only authorized roles can perform this action.
    """
    if role not in ["LECTURER"]:
        raise HTTPException(status_code=403, detail="Only lecturers can delete users")
    deleted_user = service.delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user