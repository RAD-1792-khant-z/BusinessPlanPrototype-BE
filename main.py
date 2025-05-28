from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.user import RegistrationForm
from models.admin import FacilityRegistrationForm
import services.user
import services.admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/users")
def register_user(form: RegistrationForm):
    id = services.user.register_user(form)
    return {"status": 200, "message": "success", "data": {"id": id}}

@app.post("/admin/facilities")
def register_facility(form: FacilityRegistrationForm):
    id = services.admin.register_facility(form)
    return {"status": 200, "message": "success", "data": {"id": id}}

@app.get("/admin/facilities")
def get_facilities():
    data = services.admin.get_facilities()
    return {"status": 200, "message": "success", "data": {"facilities": data}}

@app.get("/admin/facilities/{id}")
def get_facility_by_id(id: str):
    data = services.admin.get_facility_by_id(id)
    return {"status": 200, "message": "success", "data": data}