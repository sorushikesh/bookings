from app.bookings.models import Booking
from sqlalchemy.orm import Session
import logging

from app.bookings.schemas import BookingCreate

logger = logging.getLogger(__name__)


def create_booking(db: Session, booking: BookingCreate):
    db_booking = Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    logger.info(f"Booking created with ID: {db_booking.id}")
    return db_booking
