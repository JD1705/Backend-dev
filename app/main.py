from fastapi import FastAPI, HTTPException,status,Query
from typing import Annotated

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