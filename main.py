from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.user import RegistrationForm
import services.user

app = FastAPI()

@app.post("/users")
def register_user(form: RegistrationForm):
    id = services.user.register_user(form)
    return {"id": id}
