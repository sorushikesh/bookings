from sqlalchemy.orm import Session
from app.bookings.models import Booking
from app.bookings.schemas import BookingCreate, BookingUpdate
import logging

logger = logging.getLogger(__name__)


def create_booking(db: Session, booking: BookingCreate):
    db_booking = Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    logger.info(f"Booking created with ID: {db_booking.id}")
    return db_booking


def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()


def get_bookings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Booking).offset(skip).limit(limit).all()


def update_booking(db: Session, booking_id: int, booking: BookingUpdate):
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        logger.warning(f"Booking ID {booking_id} not found for update")
        return None
    for key, value in booking.dict(exclude_unset=True).items():
        setattr(db_booking, key, value)
    db.commit()
    db.refresh(db_booking)
    logger.info(f"Booking ID {booking_id} updated")
    return db_booking


def delete_booking(db: Session, booking_id: int):
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        logger.warning(f"Booking ID {booking_id} not found for deletion")
        return None
    db.delete(db_booking)
    db.commit()
    logger.info(f"Booking ID {booking_id} deleted")
    return db_booking
