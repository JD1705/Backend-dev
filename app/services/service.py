from ..schemas.user_schema import UserInModel
from ..repositories.user_repository import UserRepository
from fastapi import status, HTTPException

# En app/main.py
def create_user_logic(new_user: UserInModel, db):  # 👈 Función pura
    repo = UserRepository(db)
    
    if repo.email_exists(new_user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User email already registered. Try another one'
        )
        
    data = repo.create_user(new_user.model_dump())
    
    return {
        'message':'User created successfully',
        'status_code':status.HTTP_201_CREATED,
        'insertion_id':str(data)
    }