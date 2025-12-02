from models.model import FlightTrip
from typing import List

def serp_flight_params(api_key, travel_request):
        return {
            "api_key": api_key,
            "engine": "google_flights",
            "currency": "CAD",
            "gl": "ca",
            "hl": "en",
            "departure_id": travel_request.departure_city,
            "arrival_id": travel_request.arrival_city,
            "outbound_date": travel_request.departure_date,
            "return_date": travel_request.return_date,
            "adults": travel_request.passengers
        }

def format_data_for_ai(flight_trips: List[FlightTrip] ) -> str:
    """Return a readable text summary for a list of FlightTrip objects."""

    if not flight_trips:
        return "No flight options available."

    formatted = ["**Flight Options Available**:", ""]
    for idx, trip in enumerate(flight_trips, start=1):
        formatted.append(f"--- Flight Option {idx} ---\n") 
        
        if trip.layovers:
            formatted.append(f"Priced at ${trip.price} {trip.currency} with a total duration of {trip.total_duration} minutes. This option includes {len(trip.layovers)} layover(s).\n")
        else:
            formatted.append(f"Priced at ${trip.price} {trip.currency} with a total duration of {trip.total_duration} minutes. This is a direct flight option.\n")

        formatted.append("-- Flight Details --\n")
        for i, flight in enumerate(trip.flights, start=1):
            formatted.append(
                f"Flight {i if trip.layovers else ''} {flight.airline} {flight.flight_number} from {flight.departure_airport.name} to {flight.arrival_airport.name}, "
                f"Duration: {flight.duration} minutes\n"
                f"Departure Time: {flight.departure_airport.time}, "
                f"Arrival Time: {flight.arrival_airport.time}, "
                f"Overnight: {'Yes' if flight.overnight else 'No'}\n"
                f"Class: {flight.travel_class}\n"
            )

        if trip.layovers:
            formatted.append("  Layovers:\n")
            for layover in trip.layovers:
                formatted.append(f"  - {layover.name} ({layover.duration} minutes)\n")

        formatted.append("")  # blank line between trips
        
    return "\n".join(formatted)