from fastapi import APIRouter, HTTPException
from models.job import JobCreate
from store.memory import jobs_seed

router = APIRouter()


@router.post("/jobs")
def add_job(job: JobCreate):
    
    jobs_seed{
        "id":job.id,
        "name":job.name,
        "description":job.description,
        "industry": job.industry,
        "keyword":job.keywords
    }
    return job["id"]


@router.get("/jobs")
def get_all_jobs():
    return jobs_seed

@router.get("/job/{id}")
def get_id(id: int):
    if id not in jobs_seed.get(id):
        HTTPExceptipn(status_code=404, detail="Not Found")
        
    return jobs_seed.get(id)

@router.post()