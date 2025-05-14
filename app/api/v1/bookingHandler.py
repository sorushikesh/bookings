from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import logging

from app.bookings.schemas import BookingCreate, BookingOut
from app.db.database import get_db
import app.bookings.service as bookingservice

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/v1/bookings", tags=["Bookings"])


class BookingHandler:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_booking(self, booking: BookingCreate) -> BookingOut:
        logger.info(
            f"Creating booking for user: {booking.username}, hotel: {booking.hotel_name}"
        )
        return bookingservice.create_booking(self.db, booking)


@router.post("/", response_model=BookingOut)
def create_booking(booking: BookingCreate, handler: BookingHandler = Depends()):
    return handler.create_booking(booking)
