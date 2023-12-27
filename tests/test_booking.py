import unittest
from datetime import datetime
from klm_booking_system import Booking, Itinerary

class TestBooking(unittest.TestCase):
    def test_valid_booking(self):
        # Create a valid booking
        departure_time = datetime(2025, 9, 1, 10, 0)
        itinerary = Itinerary(["AMS", "CDG"])
        booking = Booking(departure_time, itinerary)

        # Check if the booking attributes are set correctly
        self.assertEqual(booking.flight_departure_time, departure_time)
        self.assertEqual(booking.itinerary, itinerary)

    def test_invalid_booking_departure_time(self):
        # Create a booking with a past departure time
        departure_time = datetime(2020, 1, 1, 10, 0)
        itinerary = Itinerary(["AMS", "CDG"])

        # Check if ValueError is raised
        with self.assertRaises(ValueError):
            Booking(departure_time, itinerary)

    def test_invalid_booking_itinerary(self):
        # Create a booking with an invalid itinerary
        departure_time = datetime(2025, 9, 1, 10, 0)
        itinerary = "AMS-CDG"  # Invalid itinerary format

        # Check if TypeError is raised
        with self.assertRaises(TypeError):
            Booking(departure_time, itinerary)

if __name__ == "__main__":
    unittest.main()