"""
Example usage with multiple itineraries
"""

from datetime import datetime
from klm_booking_system import Booking, BookingManager, Itinerary

# Create itineraries
itinerary1 = Itinerary(["HAM", "AMS", "LHR"])
itinerary2 = Itinerary(["AMS", "LHR"])
itinerary3 = Itinerary(["AAL", "AMS", "LHR", "JFK", "SFO"])
itinerary4 = Itinerary(["LHR", "AMS"])
itinerary5 = Itinerary(["GVA", "AMS", "LHR"])
itinerary6 = Itinerary(["ATL", "AMS", "AAL"])
itinerary7 = Itinerary(["AMS", "CDG", "LHR"])

# Create bookings for these itineraries
booking1 = Booking(datetime(2025, 6, 4, 11, 4), itinerary1)
booking2 = Booking(datetime(2025, 6, 6, 10, 0), itinerary2)
booking3 = Booking(datetime(2025, 6, 12, 8, 9), itinerary3)
booking4 = Booking(datetime(2025, 5, 26, 6, 45), itinerary4)
booking5 = Booking(datetime(2025, 6, 13, 20, 40), itinerary5)
booking6 = Booking(datetime(2025, 6, 14, 9, 10), itinerary6)
booking7 = Booking(datetime(2025, 7, 15, 14, 30), itinerary7)

# Add bookings to the BookingManager
manager = BookingManager()
manager.add_booking(booking1)
manager.add_booking(booking2)
manager.add_booking(booking3)
manager.add_booking(booking4)
manager.add_booking(booking5)
manager.add_booking(booking6)
manager.add_booking(booking7)

# Retrieve and print bookings for a specific route (AMS to LHR)
bookings_amslhr = manager.bookings_for_route("AMS", "LHR")
for booking in bookings_amslhr:
    print(booking)