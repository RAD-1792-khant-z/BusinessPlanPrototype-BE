from sqlmodel import Session
from models.user import User, RegistrationForm
from core.db import engine
import uuid

def register_user(form: RegistrationForm):
    id = str(uuid.uuid4())
    user = User(id=id, first_name=form.firstName, last_name=form.lastName, phone=form.phone, email=form.email, password=form.password)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user.id