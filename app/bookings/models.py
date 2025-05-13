from sqlalchemy import Column, Integer, String, DateTime, Date
from datetime import datetime
from app.db.base_class import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    hotel_name = Column(String, nullable=False)
    hotel_city = Column(String, nullable=False)
    hotel_country = Column(String, nullable=False)
    booking_date = Column(Date, nullable=False)
    checkin_date = Column(Date, nullable=False)
    checkout_date = Column(Date, nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
