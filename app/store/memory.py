from models.job import JobCreate
from models.user import UserCreate
jobs_seed = [
    {
        "id": 1,
        "name": "Backend Python Engineer",
        "description": "Build and maintain backend services using Python, FastAPI, and REST APIs.",
        "industry": "Software",
        "keywords": ["python", "fastapi", "api", "backend", "sql"]
    },
    {
        "id": 2,
        "name": "Machine Learning Engineer",
        "description": "Develop machine learning models and deploy them into production systems.",
        "industry": "Software",
        "keywords": ["machine learning", "python", "modeling", "data", "deployment"]
    },
    {
        "id": 3,
        "name": "Frontend Engineer",
        "description": "Create responsive web interfaces using modern JavaScript frameworks.",
        "industry": "Software",
        "keywords": ["javascript", "react", "frontend", "ui"]
    },
    {
        "id": 4,
        "name": "Data Analyst",
        "description": "Analyze business data and generate insights using SQL and visualization tools.",
        "industry": "Analytics",
        "keywords": ["sql", "analytics", "data", "visualization"]
    },
    {
        "id": 5,
        "name": "DevOps Engineer",
        "description": "Automate infrastructure, CI/CD pipelines, and cloud deployments.",
        "industry": "Cloud",
        "keywords": ["docker", "kubernetes", "aws", "ci/cd", "cloud"]
    },
    {
        "id": 6,
        "name": "AI Research Intern",
        "description": "Assist in AI research projects involving NLP and deep learning techniques.",
        "industry": "Research",
        "keywords": ["nlp", "deep learning", "python", "research"]
    },
    {
        "id": 7,
        "name": "Product Manager",
        "description": "Define product requirements and collaborate with engineering teams.",
        "industry": "Product",
        "keywords": ["product", "roadmap", "stakeholders", "requirements"]
    },
    {
        "id": 8,
        "name": "QA Automation Engineer",
        "description": "Build automated test frameworks and ensure software quality.",
        "industry": "Software",
        "keywords": ["testing", "automation", "python", "selenium"]
    },
    {
        "id": 9,
        "name": "Cloud Solutions Architect",
        "description": "Design scalable cloud architectures and guide engineering teams.",
        "industry": "Cloud",
        "keywords": ["aws", "architecture", "cloud", "scalability"]
    },
    {
        "id": 10,
        "name": "Business Intelligence Engineer",
        "description": "Build dashboards and reporting pipelines for business stakeholders.",
        "industry": "Analytics",
        "keywords": ["bi", "dashboards", "sql", "data"]
    }
]

users_seed = [
    {
        "id": 1,
        "name": "Alice",
        "description": "Python developer experienced in building REST APIs and backend services.",
        "industry": "Software",
        "keywords": ["python", "backend", "api", "fastapi"]
    },
    {
        "id": 2,
        "name": "Bob",
        "description": "Aspiring machine learning engineer with strong data and modeling background.",
        "industry": "Software",
        "keywords": ["machine learning", "python", "data", "models"]
    },
    {
        "id": 3,
        "name": "Charlie",
        "description": "Frontend developer focused on creating intuitive user interfaces.",
        "industry": "Software",
        "keywords": ["javascript", "react", "ui", "frontend"]
    },
    {
        "id": 4,
        "name": "Diana",
        "description": "Data professional skilled in analytics, SQL, and business reporting.",
        "industry": "Analytics",
        "keywords": ["sql", "analytics", "data", "reporting"]
    },
    {
        "id": 5,
        "name": "Ethan",
        "description": "Cloud engineer with experience in AWS and containerized deployments.",
        "industry": "Cloud",
        "keywords": ["aws", "docker", "cloud", "kubernetes"]
    },
    {
        "id": 6,
        "name": "Fiona",
        "description": "AI researcher interested in NLP and deep learning applications.",
        "industry": "Research",
        "keywords": ["nlp", "deep learning", "research", "python"]
    },
    {
        "id": 7,
        "name": "George",
        "description": "Product-oriented professional bridging business and engineering teams.",
        "industry": "Product",
        "keywords": ["product", "requirements", "stakeholders"]
    },
    {
        "id": 8,
        "name": "Hannah",
        "description": "QA engineer specializing in automated testing frameworks.",
        "industry": "Software",
        "keywords": ["testing", "automation", "selenium", "python"]
    },
    {
        "id": 9,
        "name": "Ian",
        "description": "Architect focused on designing scalable cloud systems.",
        "industry": "Cloud",
        "keywords": ["architecture", "cloud", "scalability", "aws"]
    },
    {
        "id": 10,
        "name": "Julia",
        "description": "Business intelligence analyst building dashboards and reports.",
        "industry": "Analytics",
        "keywords": ["bi", "dashboards", "sql", "data"]
    }
]


def add_job(job: JobCreate):
    
    job_id=jobs_seed.get(id).max()+1
    
    jobs_seed{
        "id":job_id,
        "name":job.name,
        "description":job.description,
        "industry": job.industry,
        "keyword":job.keywords
    }
    return job["id"]

def jobs():
    return jobs_seed["name"]

def jobs_id(id: int):
    if id not in jobs_seed.get(id):
        HTTPExceptipn(status_code=404, detail="Not Found")
    return jobs_seed.get(id)



def users():
    return users_seed["name"]

def users_id(id: int):
    if id not in users_seed.get(id):
        HTTPExceptipn(status_code=404, detail="Not Found")
    return users_seed.get(id)

def add_user(user: UserCreate):
   user_id=users_seed.get(id).max()+1
   users_seed {
        "id":user_id,
        "name":user.name,
        "description":user.description,
        "industry": user.industry,
        "keyword":user.keywords
    }
   return users_seed["id"]