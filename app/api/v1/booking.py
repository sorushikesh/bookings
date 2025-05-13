from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import logging

from app.bookings.schemas import BookingCreate, BookingUpdate, BookingOut
from app.db.database import get_db
import app.bookings.service as bookingservice

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_model=BookingOut)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    logger.info(
        f"Creating booking for user: {booking.username}, hotel: {booking.hotel_name}"
    )
    return bookingservice.create_booking(db, booking)


@router.get("/", response_model=List[BookingOut])
def read_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.info(f"Fetching bookings with skip={skip} and limit={limit}")
    return bookingservice.get_bookings(db, skip, limit)


@router.get("/{booking_id}", response_model=BookingOut)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching booking with ID: {booking_id}")
    db_booking = bookingservice.get_booking(db, booking_id)
    if db_booking is None:
        logger.warning(f"Booking ID {booking_id} not found")
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking


@router.put("/{booking_id}", response_model=BookingOut)
def update_booking(
    booking_id: int, booking: BookingUpdate, db: Session = Depends(get_db)
):
    logger.info(f"Updating booking ID: {booking_id} with status: {booking.status}")
    return bookingservice.update_booking(db, booking_id, booking)


@router.delete("/{booking_id}", response_model=BookingOut)
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting booking with ID: {booking_id}")
    return bookingservice.delete_booking(db, booking_id)
