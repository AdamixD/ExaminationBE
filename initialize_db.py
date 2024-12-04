import requests

# Base URL for API
BASE_URL = "http://127.0.0.1:8000"

# Endpoints
USERS_ENDPOINT = f"{BASE_URL}/app/users/"
COURSES_ENDPOINT = f"{BASE_URL}/app/courses/"
COURSE_REALIZATIONS_ENDPOINT = f"{BASE_URL}/app/course_realizations/"

# Sample data
USERS = [
    {"name": "Tomasz", "surname": "Złomiarz", "role": "STUDENT", "index": 310035, "email": "student@gmail.com", "password": "student"},
    {"name": "Jurek", "surname": "Ogórek", "role": "LECTURER", "email": "lecturer@gmail.com", "password": "lecturer"},
    {"name": "Karolina", "surname": "Malina", "role": "LECTURER", "email": "malina@gmail.com", "password": "malina"}
]

COURSES = [
    {"title": "Algorytmy i struktury danych", "shortcut": "AISDI"},
    {"title": "Analiza i projektowanie systemów informacyjnych", "shortcut": "APSI"},
    {"title": "Bazy danych 2", "shortcut": "BD2"},
    {"title": "Sieci komputerowe", "shortcut": "SKM"},
    {"title": "Nanotechnologie", "shortcut": "NAN"},
    {"title": "Programowanie obiektowe", "shortcut": "PROI"},
    {"title": "Podstawy automatyki", "shortcut": "PODA"}
]

COURSE_REALIZATIONS = [
    {"semester": "24L", "course_id": 3, "lecturer_id": 2},
    {"semester": "24Z", "course_id": 1, "lecturer_id": 2},
    {"semester": "24Z", "course_id": 2, "lecturer_id": 3},
    {"semester": "23Z", "course_id": 5, "lecturer_id": 3},
    {"semester": "23Z", "course_id": 6, "lecturer_id": 3},
    {"semester": "22Z", "course_id": 7, "lecturer_id": 3}
]

def create_users():
    print("Creating users...")
    for user in USERS:
        response = requests.post(USERS_ENDPOINT, json=user)
        print(f"Status: {response.status_code}, Response: {response.json()}")

def create_courses():
    print("Creating courses...")
    for course in COURSES:
        response = requests.post(COURSES_ENDPOINT, json=course)
        print(f"Status: {response.status_code}, Response: {response.json()}")

def create_course_realizations():
    print("Creating course realizations...")
    for realization in COURSE_REALIZATIONS:
        response = requests.post(COURSE_REALIZATIONS_ENDPOINT, json=realization)
        print(f"Status: {response.status_code}, Response: {response.json()}")

if __name__ == "__main__":
    create_users()
    create_courses()
    create_course_realizations()
    print("Database initialization complete.")