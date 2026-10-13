from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# request data model
class User(BaseModel):
    name: str
    age: int


@app.get('/')
def home():
    return {'message': 'FastAPI server is running!'}

@app.post('/user')
def create_user(user: User):
    return {
        'message': "user received successfully!",
        'name': user.name,
        'age': user.age
    }