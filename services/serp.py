from models.model import TravelRequest, Flight, FlightTrip, HotelTrip, HotelReviews, NearbyPlace
from helpers.helper import serp_flight_params, serp_hotel_params
from typing import List, Union
from fastapi import HTTPException
from serpapi import GoogleSearch
import logging
import os
import asyncio

from data.serpData import serp_flight_data, serp_hotel_data

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

class SerpAPIService:
    def __init__(self):
        self.api_key = os.getenv("SERP_API_KEY")

    async def serp_request(self, params: dict) -> dict:
        try:
            # For testing with static data use:
            # return await asyncio.to_thread(serp_flight_data)
            # return await asyncio.to_thread(serp_hotel_data)

            # For real API calls use:
            return await asyncio.to_thread(lambda: GoogleSearch(params).get_dict())
        except Exception as e:
            logger.error("Error during SERP API flight request: %s", e)
            raise HTTPException(status_code=500, detail=str(e))


    async def search_flights(self, travel_request: TravelRequest) -> Union[List[FlightTrip], str]:
        # Use SERP API to search for flights
        flight_results = await self.serp_request(serp_flight_params(self.api_key, travel_request))

        if not isinstance(flight_results, dict):
            logger.error("Unexpected SERP response type: %s", type(flight_results))
            return []
        if flight_results.get("error"):
            logger.error("SERP API returned an error: %s", flight_results.get("error"))
            return []

        parsed_flights: List[FlightTrip] = []
        
        def _parse_individual_flight(flight: dict) -> Flight:
            return Flight(
                airline = flight.get("airline", "Unknown Airline"),
                flight_number = flight.get("flight_number", "N/A"),
                departure_airport = flight.get("departure_airport", {}),
                arrival_airport = flight.get("arrival_airport", {}),
                overnight = flight.get("overnight", False),
                duration = flight.get("duration", 0),
                travel_class = flight.get("travel_class", "Economy")
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
                for entry in flight_results.get(key, []):
                    f = _parse_flight_entry(entry, flight_results.get("search_parameters", {}))
                    if f:
                        parsed_flights.append(f)

        return parsed_flights
    
    async def search_hotels(self, travel_request: TravelRequest):
        hotel_results = await self.serp_request(serp_hotel_params(self.api_key, travel_request))

        if not isinstance(hotel_results, dict):
            logger.error("Unexpected SERP response type: %s", type(hotel_results))
            return []
        if hotel_results.get("error"):
            logger.error("SERP API returned an error: %s", hotel_results.get("error"))
            return []
        
        parsed_hotels: List[HotelTrip] = []

        def _parse_hotel_reviews(reviews: List[dict]) -> List[HotelReviews]:
            parsed_reviews: List[HotelReviews] = []
            for review in reviews:
                try:
                    parsed_reviews.append(
                        HotelReviews(
                            name = review.get("name", "Unnamed Review"),
                            description = review.get("description", ""),
                            total_mentioned = review.get("total_mentioned", 0),
                            positive = review.get("positive", 0),
                            negative = review.get("negative", 0),
                            neutral = review.get("neutral", 0)
                        )
                    )
                except Exception as e:
                    logger.warning("Failed to parse hotel review entry: %s", e)
                    continue
            return parsed_reviews
        
        def _parse_nearby_places(places: List[dict]) -> List[NearbyPlace]:
            parsed_places: List[NearbyPlace] = []
            for place in places:
                try:
                    parsed_places.append(
                        NearbyPlace(
                            name = place.get("name", "Unnamed Place"),
                            transportations = place.get("transportations", [])
                        )
                    )
                except Exception as e:
                    logger.warning("Failed to parse nearby place entry: %s", e)
                    continue
            return parsed_places


        if isinstance(hotel_results, dict): 
            for hotel in hotel_results.get("properties", []):
                try:
                    parsed_hotels.append(
                        HotelTrip(
                            type = hotel.get("type", "Unknown Type"),
                            name = hotel.get("name", "Unnamed Hotel"),
                            description = hotel.get("description", ""),
                            check_in_time = hotel.get("check_in_time", ""),
                            check_out_time = hotel.get("check_out_time", ""),
                            rate_per_night = hotel.get("rate_per_night", {}).get("lowest", 'N/A'),
                            total_rate = hotel.get("total_rate", {}).get("lowest", 'N/A'),
                            nearby_places = _parse_nearby_places(hotel.get("nearby_places", [])),
                            hotel_class = hotel.get("extracted_hotel_class", 0.0),
                            overall_rating = hotel.get("overall_rating", 0.0),
                            location_rating = hotel.get("location_rating", 0.0),
                            reviews_breakdown = _parse_hotel_reviews(hotel.get("reviews_breakdown", [])),
                            property_token = hotel.get("property_token", "")
                        )
                    )
                except Exception as e:
                    logger.warning("Failed to parse hotel entry: %s", e)
                    continue

        return parsed_hotels
