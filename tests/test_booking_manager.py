import unittest
from datetime import datetime
from klm_booking_system.booking_manager import BookingManager
from klm_booking_system.booking import Booking
from klm_booking_system.itinerary import Itinerary

class TestBookingManager(unittest.TestCase):
    def setUp(self):
        self.booking_manager = BookingManager()

    def test_add_booking(self):
        itinerary = Itinerary(["AMS", "CDG"])
        booking = Booking(datetime(2025, 9, 1, 10, 0), itinerary)
        self.booking_manager.add_booking(booking)
        self.assertEqual(len(self.booking_manager.bookings), 1)
        self.assertEqual(self.booking_manager.bookings[0], booking)

    def test_bookings_before(self):
        itinerary1 = Itinerary(["AMS", "CDG"])
        itinerary2 = Itinerary(["LHR", "CDG"])
        itinerary3 = Itinerary(["AMS", "LHR"])
        booking1 = Booking(datetime(2025, 9, 1, 10, 0), itinerary1)
        booking2 = Booking(datetime(2025, 9, 2, 12, 0), itinerary2)
        booking3 = Booking(datetime(2025, 9, 3, 14, 0), itinerary3)
        self.booking_manager.add_booking(booking1)
        self.booking_manager.add_booking(booking2)
        self.booking_manager.add_booking(booking3)
        time = datetime(2025, 9, 2, 0, 0)
        bookings = self.booking_manager.bookings_before(time)
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0], booking1)

        time = datetime(2025, 9, 4, 0, 0)
        bookings = self.booking_manager.bookings_before(time)
        self.assertEqual(len(bookings), 3)
        self.assertEqual(bookings, [booking1, booking2, booking3])

        time = datetime(2025, 8, 31, 0, 0)
        bookings = self.booking_manager.bookings_before(time)
        self.assertEqual(len(bookings), 0)

    def test_bookings_for_route(self):
        itinerary1 = Itinerary(["AMS", "CDG"])
        itinerary2 = Itinerary(["LHR", "CDG"])
        itinerary3 = Itinerary(["AMS", "LHR"])
        booking1 = Booking(datetime(2025, 9, 1, 10, 0), itinerary1)
        booking2 = Booking(datetime(2025, 9, 2, 12, 0), itinerary2)
        booking3 = Booking(datetime(2025, 9, 3, 14, 0), itinerary3)
        self.booking_manager.add_booking(booking1)
        self.booking_manager.add_booking(booking2)
        self.booking_manager.add_booking(booking3)
        bookings = self.booking_manager.bookings_for_route("AMS", "CDG")
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0], booking1)

        bookings = self.booking_manager.bookings_for_route("LHR", "CDG")
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0], booking2)

        bookings = self.booking_manager.bookings_for_route("AMS", "LHR")
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0], booking3)

        bookings = self.booking_manager.bookings_for_route("CDG", "AMS")
        self.assertEqual(len(bookings), 0)

        bookings = self.booking_manager.bookings_for_route("AMS", "AMS")
        self.assertEqual(len(bookings), 0)

        bookings = self.booking_manager.bookings_for_route("LHR", "LHR")
        self.assertEqual(len(bookings), 0)

    def test_bookings_for_route_with_multiple_codes(self):
        itinerary1 = Itinerary(["AMS", "CDG", "LHR"])
        itinerary2 = Itinerary(["LHR", "CDG", "AMS"])
        itinerary3 = Itinerary(["AMS", "LHR", "CDG"])
        booking1 = Booking(datetime(2025, 9, 1, 10, 0), itinerary1)
        booking2 = Booking(datetime(2025, 9, 2, 12, 0), itinerary2)
        booking3 = Booking(datetime(2025, 9, 3, 14, 0), itinerary3)
        self.booking_manager.add_booking(booking1)
        self.booking_manager.add_booking(booking2)
        self.booking_manager.add_booking(booking3)
        bookings = self.booking_manager.bookings_for_route("AMS", "CDG")
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0], booking1)

        bookings = self.booking_manager.bookings_for_route("LHR", "CDG")
        self.assertEqual(len(bookings), 2)
        self.assertEqual(bookings[0], booking2)
        self.assertEqual(bookings[1], booking3)

        bookings = self.booking_manager.bookings_for_route("AMS", "LHR")
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0], booking3)

        bookings = self.booking_manager.bookings_for_route("CDG", "AMS")
        self.assertEqual(len(bookings), 1)

        bookings = self.booking_manager.bookings_for_route("AMS", "AMS")
        self.assertEqual(len(bookings), 0)

        bookings = self.booking_manager.bookings_for_route("LHR", "LHR")
        self.assertEqual(len(bookings), 0)

    def test_bookings_for_route_with_invalid_route(self):
        itinerary1 = Itinerary(["AMS", "CDG"])
        itinerary2 = Itinerary(["LHR", "CDG"])
        booking1 = Booking(datetime(2025, 9, 1, 10, 0), itinerary1)
        booking2 = Booking(datetime(2025, 9, 2, 12, 0), itinerary2)
        self.booking_manager.add_booking(booking1)
        self.booking_manager.add_booking(booking2)
        bookings = self.booking_manager.bookings_for_route("CDG", "LHR")
        self.assertEqual(len(bookings), 0)

    def test_bookings_for_route_with_no_bookings(self):
        bookings = self.booking_manager.bookings_for_route("AMS", "CDG")
        self.assertEqual(len(bookings), 0)

    def test_bookings_for_route_with_same_origin_and_destination(self):
        itinerary1 = Itinerary(["AMS", "CDG"])
        itinerary2 = Itinerary(["LHR", "CDG"])
        booking1 = Booking(datetime(2025, 9, 1, 10, 0), itinerary1)
        booking2 = Booking(datetime(2025, 9, 2, 12, 0), itinerary2)
        self.booking_manager.add_booking(booking1)
        self.booking_manager.add_booking(booking2)
        bookings = self.booking_manager.bookings_for_route("CDG", "CDG")
        self.assertEqual(len(bookings), 0)

    def test_bookings_for_route_with_invalid_origin(self):
        itinerary1 = Itinerary(["AMS", "CDG"])
        itinerary2 = Itinerary(["LHR", "CDG"])
        booking1 = Booking(datetime(2025, 9, 1, 10, 0), itinerary1)
        booking2 = Booking(datetime(2025, 9, 2, 12, 0), itinerary2)
        self.booking_manager.add_booking(booking1)
        self.booking_manager.add_booking(booking2)
        bookings = self.booking_manager.bookings_for_route("JFK", "CDG")
        self.assertEqual(len(bookings), 0)


if __name__ == "__main__":
    unittest.main()
