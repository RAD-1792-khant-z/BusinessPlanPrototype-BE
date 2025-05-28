from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class RegistrationForm(BaseModel):
    firstName: str
    lastName: str
    phone: str
    email: str
    password: str

class User(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str