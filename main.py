from fastapi import FastAPI
from routes.student_route import stu

app = FastAPI()

app.include_router(stu)
