from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import generate_plan

app = FastAPI(title='Personal Fitness Assistant NLP')

class Request(BaseModel):
    age: int
    level: str
    goal: str
    time: int

@app.post('/plan')
async def plan(req: Request):
    out = generate_plan(req.age, req.level, req.goal, req.time)
    return {'input': {'age': req.age, 'level': req.level, 'goal': req.goal, 'time': req.time}, 'plan': out}

@app.get('/')
async def root():
    return {'message': 'Personal Fitness Assistant NLP API. POST /plan with {age, level, goal, time}.'}
