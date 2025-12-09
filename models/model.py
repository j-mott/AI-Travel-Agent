from typing import Any, List, Optional
from pydantic import BaseModel, Field

class TravelRequest(BaseModel):
    departure_city: str = Field(default="YYZ")
    arrival_city: str = Field(default="JFK")
    departure_date: str = Field(default="2026-02-05")
    return_date: str = Field(default="2026-02-13")
    passengers: int = Field(default=1)

class Airport(BaseModel):
    name: str
    id: str
    time: str

class Flight(BaseModel):
    airline: str
    flight_number: str
    departure_airport: Airport
    arrival_airport: Airport
    overnight: bool
    duration: int
    travel_class: str

class Layover(BaseModel):
    name: str
    id: str
    duration: int

class FlightTrip(BaseModel):
    flights: List[Flight]
    total_duration: int
    price: float
    currency: str
    gl: str
    layovers: Optional[List[Layover]]

class HotelReviews(BaseModel):
    name: str
    description: str
    total_mentioned: int
    positive: int
    negative: int
    neutral: int

class Transportation(BaseModel):
    type: str
    duration: str


class NearbyPlace(BaseModel):
    name: str
    transportations: List[Transportation]
class HotelTrip(BaseModel):
    type: str
    name: str
    description: str
    check_in_time: str
    check_out_time: str
    rate_per_night: str
    total_rate: str
    nearby_places: List[NearbyPlace]
    hotel_class: float
    overall_rating: float
    location_rating: float
    reviews_breakdown: List[HotelReviews]
    property_token: str

class BuildCrewOptions(BaseModel):
    flight_info: str = Field(default=None, description="Formatted flight information for AI processing")
    departure_city: str = Field(default=None, description="IATA code of the departure city")
    arrival_city: str = Field(default=None, description="IATA code of the arrival city")
    departure_date: str = Field(default=None, description="Departure date in YYYY-MM-DD format")
    return_date: str = Field(default=None, description="Return date in YYYY-MM-DD format")
    passengers: int = Field(default=1, description="Number of passengers")

class AIReturnModel(BaseModel):
    flight_info: List[FlightTrip] = Field(default=[], description="List of flight trip options")
    ai_flight_summary: str = Field(default='', description="AI-generated summary of flight options")