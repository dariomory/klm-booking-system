from typing import List
from datetime import datetime
from klm_booking_system.booking import Booking


class BookingManager:
    """
    A class that manages bookings for a flight booking system.

    Attributes:
        bookings (list): A list of Booking objects representing the bookings made.

    Methods:
        add_booking(booking: Booking): Adds a new booking to the system.
        bookings_before(time: datetime) -> List[Booking]: Retrieves bookings before a given time.
        bookings_for_route(origin: str, destination: str) -> List[Booking]: Retrieves bookings for a specific route.
    """

    def __init__(self):
        self.bookings = []

    def add_booking(self, booking: Booking):
        """
        Adds a new booking to the system.

        :param booking: The Booking object to be added.
        :raises ValueError: If the booking has a past departure date.
        """
        if booking.flight_departure_time > datetime.now():
            self.bookings.append(booking)
        else:
            raise ValueError("Cannot add booking with a past date.")

    def bookings_before(self, time: datetime) -> List[Booking]:
        """
        Retrieves bookings before a given time.

        :param time: The datetime object representing the time.
        :return: A list of Booking objects that were made before the given time.
        """
        return [
            booking for booking in self.bookings if booking.flight_departure_time < time
        ]

    def bookings_for_route(self, origin: str, destination: str) -> List[Booking]:
        """
        Retrieves bookings for a specific route.

        :param origin: The IATA code of the origin airport in the sequence.
        :param destination: The IATA code of the destination airport in the sequence.
        :return: A list of Booking objects that match the route sequence.
        """
        matching_bookings = []
        for booking in self.bookings:
            if booking.itinerary.includes_sequence(origin, destination):
                matching_bookings.append(booking)
        return matching_bookings
