from fastapi import APIRouter, HTTPException
from models.user import UserCreate, User
from store.memory import users_seed, users, users_id, add_user

router = APIRouter()


@router.post("/addusers")
def add_job(job: UserCreate):
    job=add_job()
    return job["id"]

@router.get("/users")
def get_all_users():
    user=users()
    return user

@router.get("/users/{id}")
def get_id(id: User):
    user=users_id(id)
    return user
