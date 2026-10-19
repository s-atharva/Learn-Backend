from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'hello world'}


@app.get('/about')
def about():
    return {'message': 'This is Fastapi Application'}
