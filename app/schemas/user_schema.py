from pydantic import BaseModel, EmailStr
from typing import Annotated, Union

class UserOutModel(BaseModel):
    username: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    
class UserInModel(UserOutModel):
    password: str
    
class Email(BaseModel):
    email: EmailStr