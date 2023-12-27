import unittest
from klm_booking_system.itinerary import Itinerary


class TestItinerary(unittest.TestCase):
    def setUp(self):
        self.itinerary = Itinerary(["AMS", "CDG", "LHR"])

    def test_valid_initialization(self):
        self.assertEqual(self.itinerary.stops, ["AMS", "CDG", "LHR"])

    def test_invalid_stop_type(self):
        with self.assertRaises(ValueError):
            Itinerary(["AMS", 123, "LHR"])

    def test_invalid_stop_length(self):
        with self.assertRaises(ValueError):
            Itinerary(["AMS", "CD", "LHR"])

    def test_includes_sequence(self):
        self.assertTrue(self.itinerary.includes_sequence("AMS", "CDG"))
        self.assertTrue(self.itinerary.includes_sequence("CDG", "LHR"))
        self.assertFalse(self.itinerary.includes_sequence("AMS", "LHR"))
        self.assertFalse(self.itinerary.includes_sequence("CDG", "AMS"))

    def test_includes_sequence_invalid_origin(self):
        self.assertFalse(self.itinerary.includes_sequence("XYZ", "CDG"))

    def test_includes_sequence_invalid_destination(self):
        self.assertFalse(self.itinerary.includes_sequence("AMS", "XYZ"))

    def test_includes_sequence_empty_itinerary(self):
        empty_itinerary = Itinerary([])
        self.assertFalse(empty_itinerary.includes_sequence("AMS", "CDG"))

    def test_repr(self):
        self.assertEqual(repr(self.itinerary), "AMS->CDG->LHR")


if __name__ == "__main__":
    unittest.main()
