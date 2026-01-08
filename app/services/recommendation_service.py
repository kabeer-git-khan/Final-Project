from fastapi import APIRouter, HTTPException
from models.user import User
from store.memory import users_id
from services.job_service import rank_job


router = APIRouter()

@router.get('users/{uid}/recommendation')
def user_recommendation(uid:User):
    user=users_id(uid)
    job=rank_job(user)
    return {
        "user_id":uid,
        "recommended_jobs": job
    }