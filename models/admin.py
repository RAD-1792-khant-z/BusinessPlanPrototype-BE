from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import List, Optional

class FacilityDayStatus(BaseModel):
    day: str
    open: bool
    openTime: Optional[str]
    closeTime: Optional[str]

class FacilityRegistrationForm(BaseModel):
    name: str
    imageUrl: str
    lat: float
    lng: float
    description: str
    days: List[FacilityDayStatus]

class Facility(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    image_url: str
    lat: float
    lng: float
    description: str

class OperatingDay(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    facility_id: str = Field(foreign_key="facility.id")
    day: str
    open: bool
    open_time: Optional[str]
    close_time: Optional[str]

class OperatingDayData(BaseModel):
    day: str
    open: bool
    open_time: Optional[str]
    close_time: Optional[str]

class FacilityData(BaseModel):
    id: str
    name: str
    image_url: str
    description: str
    operating_days: List[OperatingDayData]



