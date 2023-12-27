from datetime import datetime
from klm_booking_system.itinerary import Itinerary


class Booking:
    """
    Represents a flight booking, including departure time and itinerary.

    Attributes:
        flight_departure_time (datetime): The departure time of the flight.
        itinerary (Itinerary): The itinerary of the flight.
    """

    def __init__(self, flight_departure_time: datetime, itinerary: Itinerary):
        """
        Initialize a new booking instance with a departure time and itinerary.

        :param flight_departure_time: The departure time of the flight.
        :param itinerary: The Itinerary object representing the sequence of airport stops.
        :raises TypeError: If flight_departure_time is not a datetime object or if itinerary is not an Itinerary object.
        :raises ValueError: If flight_departure_time is in the past.
        """
        self._validate_flight_departure_time(flight_departure_time)
        self._validate_itinerary(itinerary)

        self._flight_departure_time = flight_departure_time
        self._itinerary = itinerary

    @property
    def flight_departure_time(self) -> datetime:
        """Return the flight departure time."""
        return self._flight_departure_time

    @property
    def itinerary(self) -> Itinerary:
        """Return the flight's itinerary."""
        return self._itinerary

    def _validate_flight_departure_time(self, flight_departure_time: datetime):
        if not isinstance(flight_departure_time, datetime):
            raise TypeError("flight_departure_time must be a datetime object.")
        if flight_departure_time < datetime.now():
            raise ValueError("flight_departure_time cannot be in the past.")

    def _validate_itinerary(self, itinerary: Itinerary):
        if not isinstance(itinerary, Itinerary):
            raise TypeError("itinerary must be an instance of Itinerary.")

    def __repr__(self):
        """Return a string representation of the booking."""
        return f"Booking({self.itinerary}, {self.flight_departure_time})"
