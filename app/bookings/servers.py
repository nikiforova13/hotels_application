from app.dao.base import BaseDAO
from app.bookings.models import Bookings


class BookingsDao(BaseDAO):
    model = Bookings
