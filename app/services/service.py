from ..schemas.user_schema import UserInModel, UserOutModel
from ..repositories.user_repository import UserRepository
from fastapi import status, HTTPException

# in app/main.py
def create_user_logic(new_user: UserInModel, db):
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
    
def search_user_email(user_email: str, db):
    repo = UserRepository(db)
    
    if not repo.email_exists(user_email):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User Not Found'
        )
    
    user_data = repo.search_email(user_email)
    return UserOutModel(**user_data).model_dump()