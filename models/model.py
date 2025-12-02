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

class AIReturnModel(BaseModel):
    flight_info: List[FlightTrip] = Field(default_factory=list)
    # hotel_info: List[Any] = Field(default_factory=list)
    # ai_flight_info: str = ""
    # ai_hotel_info: str = ""