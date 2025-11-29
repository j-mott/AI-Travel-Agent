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