class Itinerary:
    def __init__(self, stops: list[str]):
        """
        Initialize an itinerary with a list of stops (airport IATA codes).

        :param stops: A list of strings representing the IATA codes of the airports in the itinerary.
        :raises ValueError: If any stop is not a valid 3-letter IATA code.
        """
        if not all(isinstance(stop, str) and len(stop) == 3 for stop in stops):
            raise ValueError("All stops must be valid 3-letter IATA codes.")
        self.stops = stops

    def includes_sequence(self, origin: str, destination: str) -> bool:
        """
        Check if the itinerary includes a specific origin-destination sequence.

        :param origin: The IATA code of the origin airport.
        :param destination: The IATA code of the destination airport.
        :return: True if the sequence is in the itinerary, False otherwise.
        """
        if origin not in self.stops or destination not in self.stops:
            return False
        origin_index = self.stops.index(origin)
        return (
            origin_index < len(self.stops) - 1
            and self.stops[origin_index + 1] == destination
        )

    def __repr__(self):
        return "->".join(self.stops)
