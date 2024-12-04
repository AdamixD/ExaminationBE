from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from api.auth import router as auth_router
from api.user import router as user_router
from api.course import router as course_router
from api.course_realization import router as course_realization_router
from api.exam import router as exam_router
from api.question import router as question_router
from api.question_item import router as question_item_router
from api.exam_student import router as exam_student_router
from api.question_result import router as question_result_router

from database.session import init_db

# Lifespan management for FastAPI (recommended for compatibility)
app = FastAPI()

ORIGINS: List[str] = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# CORS Middleware for handling cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all API routers
app.include_router(auth_router, prefix="/app")
app.include_router(user_router, prefix="/app")
app.include_router(course_router, prefix="/app")
app.include_router(course_realization_router, prefix="/app")
app.include_router(exam_router, prefix="/app")
app.include_router(question_router, prefix="/app")
app.include_router(question_item_router, prefix="/app")
app.include_router(exam_student_router, prefix="/app")
app.include_router(question_result_router, prefix="/app")


# Startup event for database initialization
@app.on_event("startup")
async def startup_event():
    init_db()


# Root endpoint
@app.get("/app")
async def root():
    return {"Examination": "Start"}


# from datetime import timedelta
# from typing import List
#
# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import OAuth2PasswordRequestForm
# from jose import jwt, JWTError
# from sqlalchemy.orm import Session
#
# from auth import auth
# from auth.auth import oauth2_scheme, SECRET_KEY, ALGORITHM
#
# from database.session import get_db, init_db
# from models import User
# from schemas import UserCreate, UserDisplay
#
#
# app = FastAPI()
#
#
# origins: List[str] = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]
#
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
#
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#
#
# @app.on_event("startup")
# async def startup_event():
#     init_db()
#
#
# @app.get("/app")
# async def root():
#     return {"Examination": "Start"}
#
#
# @app.post("/app/users/", response_model=UserDisplay)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered!")
#     password = auth.get_password_hash(user.password)
#     user.password = password
#     new_user = User(**user.dict())
#     print(user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
#
# @app.post("/app/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = auth.authenticate_user(db=db, email=form_data.username, password=form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password!",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = auth.create_access_token(
#         data={"sub": user.email}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
#
#
# def get_authorized_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials!",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = db.query(User).filter(User.email == email).first()
#     if user is None:
#         raise credentials_exception
#     return user
#
#
# def require_role(allowed_roles: List[str]):
#     def role_checker(user: UserDisplay = Depends(get_authorized_user)):
#         if user.role.value not in allowed_roles:
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail="You do not have permission to access this resource!"
#             )
#         return user
#     return role_checker
#
#
# @app.get("/app/protected")
# async def protected_route(user: UserDisplay = Depends(get_authorized_user)):
#     return {"message": f"Access granted: {user.name} {user.surname}."}
#
#
# @app.get("/app/student_access")
# async def student_access(user: UserDisplay = Depends(require_role(["STUDENT"]))):
#     return {"message": f"Access granted to student: {user.name} {user.surname}."}
#
#
# @app.get("/app/lecturer_access")
# async def lecturer_access(user: UserDisplay = Depends(require_role(["LECTURER"]))):
#     return {"message": f"Access granted to lecturer: {user.name} {user.surname}."}
#
#
# @app.get("/app/student_or_lecturer_access")
# async def student_or_lecturer_access(user: UserDisplay = Depends(require_role(["STUDENT", "LECTURER"]))):
#     return {"message": f"Access granted to student or lecturer: {user.name} {user.surname}."}
