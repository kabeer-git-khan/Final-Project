from fastapi import APIRouter, HTTPException
from models.job import JobCreate, Job
from store.memory import jobs_seed, jobs, add_job, jobs_id

router = APIRouter()


@router.post("/addjobs")
def add_job(job: JobCreate):
    job=add_job()
    return job["id"]

@router.get("/jobs")
def get_all_jobs():
    return jobs()

@router.get("/job/{id}")
def get_id(id: Job):
    job=jobs_id(id)
    return job
