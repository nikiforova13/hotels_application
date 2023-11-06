from fastapi import APIRouter
from app.bookings.servers import BookingsDao
from app.bookings.shemas import SBooking

router = APIRouter(prefix="/bookings", tags=["Бронирования"])


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingsDao.find_all()
