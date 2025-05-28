from fastapi import HTTPException
from sqlmodel import Session, select
from models.admin import FacilityRegistrationForm, Facility, FacilityDayStatus, OperatingDay, FacilityData, OperatingDayData
from core.db import engine
from typing import List
import uuid

def register_facility(form: FacilityRegistrationForm):
    id = str(uuid.uuid4())
    facility = Facility(id=id, name=form.name, description=form.description, image_url=form.imageUrl, lat=form.lat, lng=form.lng)
    with Session(engine) as session:
        session.add(facility)
        session.commit()
        session.refresh(facility)
        register_facility_operating_days(form.days, session, id)
    return id
    
def register_facility_operating_days(forms: List[FacilityDayStatus], session, facility_id):
    for form in forms:
        id = str(uuid.uuid4())
        operating_day = OperatingDay(id=id, facility_id=facility_id, day=form.day, open=form.open, open_time=form.openTime, close_time=form.closeTime)
        session.add(operating_day)
    session.commit()

def get_facilities():
    with Session(engine) as session:
        facilities = session.exec(select(Facility)).all()
        result = []
        for facility in facilities:
            days = session.exec(select(OperatingDay).where(OperatingDay.facility_id == facility.id)).all()
            operating_days = []
            for d in days:
                od = OperatingDayData(day=d.day, open=d.open, open_time=d.open_time, close_time=d.close_time)
                operating_days.append(od)
            data = FacilityData(id=facility.id, name=facility.name, image_url=facility.image_url, description=facility.description, operating_days=operating_days)
            result.append(data)
        return result
    
def get_facility_by_id(id):
    with Session(engine) as session:
        facility = session.get(Facility, id)
        if not facility:
            raise HTTPException(status_code=404, detail="Facility not found")
        days = session.exec(select(OperatingDay).where(OperatingDay.facility_id == facility.id)).all()
        facility_dict = FacilityData(
            id=facility.id,
            name=facility.name,
            image_url=facility.image_url,
            description=facility.description,
            operating_days=[OperatingDayData(day=d.day, open=d.open, open_time=d.open_time, close_time=d.close_time) for d in days]
        )
        return facility_dict