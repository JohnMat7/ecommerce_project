from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    user_name: str
    mobile_number: str
    email_verified: bool = False
    mobile_number_verified: bool = False

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    email_verified: bool
    mobile_number_verified: bool

    class Config:
        orm_mode = True

class User(UserInDB):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_name: str | None = None
