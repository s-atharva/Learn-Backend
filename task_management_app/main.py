from fastapi import FastAPI
from src.utils.db import Base, engine

Base.metadata.create_all(engine)
app = FastAPI(title="This is Task Manager")


@app.get('/')
def say_hello():
    return {'message': 'Welcome to Task Management System'}
