from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from threading import Thread

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
from database.exam_status_updater import run_update_exam_status_job

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


# New: Start the scheduler in a background thread
def start_exam_status_updater():
    thread = Thread(target=run_update_exam_status_job, daemon=True)
    thread.start()
    print("Exam status updater started in background thread.")


# Startup event for FastAPI to initialize both the database and the scheduler
@app.on_event("startup")
async def startup_event():
    init_db()
    start_exam_status_updater()


# Root endpoint
@app.get("/app")
async def root():
    return {"Examination": "Start"}
