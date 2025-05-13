from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional


class BookingBase(BaseModel):
    username: str
    email: EmailStr
    city: str
    country: str
    hotel_name: str
    hotel_city: str
    hotel_country: str
    booking_date: date
    checkin_date: date
    checkout_date: date
    status: Optional[str] = "pending"


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BaseModel):
    status: Optional[str]


class BookingOut(BookingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
