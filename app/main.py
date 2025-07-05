from fastapi import FastAPI, HTTPException,status,Query
from typing import Annotated
from .databases.mongo_db import get_db_connection
from .schemas.user_schema import UserInModel, Email
from .services.service import create_user_logic, search_user_email

app = FastAPI()

@app.get('/')
def root():
    return {"message":"Hello World!"}

# basic CRUD functions

@app.post('/sum/')
async def sum_endpoint(a: Annotated[int,None] = Query(None), b: Annotated[int,None] = Query(None)):
    if a == None or b == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='all parameters must be passed to'
        )
    return {
        'result':a + b,
        'status_code':status.HTTP_200_OK
    }
    
    
@app.post('/sign-up/')
def create_user(new_user: UserInModel):
    db = get_db_connection()
    return create_user_logic(new_user, db)


@app.get('/user/')
def search_user_by_email(user_email: Email):
    db = get_db_connection()
    return search_user_email(user_email.email, db)