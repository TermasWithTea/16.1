from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return{'message':'Главная страница'}

@app.get('/user/admin')
async def ad_user() :
    return{'message':'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def user_id(user_id:int) -> dict:
    return{'message':f'Вы вошли как пользователь под номером {user_id}'}

@app.get('/id')
async def end(username: str = 'alex', age: int = 24) -> dict:
    return{'message':'Информация о пользователе.','Name':username, 'Age': age}

