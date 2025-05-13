from fastapi import FastAPI
import logging
from app.api.v1 import booking
from app.db.database import engine, Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hotel Booking API")
app.include_router(booking.router, prefix="/api/v1/bookings", tags=["Bookings"])

logger.info("Application startup complete")
