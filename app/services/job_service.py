from store.memory import users_seed, jobs_seed
from store.memory import users, users_id

jobs=[]

def rank_job(user: int):
        for job in jobs_seed:
            if user["industry"]==job["industry"]:
                job.append(jobs_seed["id"])
        return jobs