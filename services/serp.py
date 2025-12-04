from models.model import TravelRequest, Flight, FlightTrip
from helpers.helper import serp_flight_params
from typing import List
from fastapi import HTTPException
from serpapi import GoogleSearch
import logging
import os
import asyncio

from data.serpData import serp_flight_data # cut-and-paste SERP API response data for testing

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

class SerpAPIService:
    def __init__(self):
        self.api_key = os.getenv("SERP_API_KEY")

    async def serp_flight_request(self, params: dict) -> dict:
        try:
            # For testing with static data use:
            # return await asyncio.to_thread(serp_flight_data)
            # For real API calls use:
            return await asyncio.to_thread(lambda: GoogleSearch(params).get_dict())
        except Exception as e:
            logger.error("Error during SERP API flight request: %s", e)
            raise HTTPException(status_code=500, detail=str(e))


    async def search_flights(self, travel_request: TravelRequest) -> List[Flight]:
        # Use SERP API to search for flights
        # Query SERP (or test fixture) and convert the results into Flight models
        flight_results = await self.serp_flight_request(serp_flight_params(self.api_key, travel_request))

        if not isinstance(flight_results, dict):
            logger.error("Unexpected SERP response type: %s", type(flight_results))
            return []
        if flight_results.get("error"):
            logger.error("SERP API returned an error: %s", flight_results.get("error"))
            return []

        parsed_flights: List[FlightTrip] = []
        
        def _parse_individual_flight(flight: dict) -> Flight:
            return Flight(
                airline=flight.get("airline", ""),
                flight_number=flight.get("flight_number", ""),
                departure_airport=flight.get("departure_airport", {}),
                arrival_airport=flight.get("arrival_airport", {}),
                overnight=flight.get("overnight", False),
                duration=flight.get("duration", 0),
                travel_class=flight.get("travel_class")
            )

        def _parse_flight_entry(entry: dict, search_params: dict) -> FlightTrip | None:
            try:
                flights: List[Flight] = []
                for flight in entry.get("flights", []):
                    trip = _parse_individual_flight(flight)
                    if trip:
                        flights.append(trip)


                return FlightTrip(
                    flights = flights,
                    total_duration = entry.get("total_duration"),
                    price = entry.get("price"),
                    currency = search_params.get("currency"),
                    gl = search_params.get("gl"),
                    layovers = entry.get("layovers", [])
                )

            except Exception as e:
                logger.warning("Failed to parse flight entry: %s", e)
                return []

        # Parse 'best_flights' then 'other_flights' if present
        if isinstance(flight_results, dict):
            
            for key in ("best_flights", "other_flights"):
                print(f"Processing flight results key: {key}")
                for entry in flight_results.get(key, []):
                    f = _parse_flight_entry(entry, flight_results.get("search_parameters"))
                    if f:
                        parsed_flights.append(f)

        return parsed_flights
