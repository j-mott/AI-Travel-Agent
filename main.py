from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from models.model import AIReturnModel, TravelRequest
from helpers.helper import format_data_for_ai
from services.serp import SerpAPIService
from services.crew import CrewAPIService
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
app = FastAPI() # FastAPI application instance used by Uvicorn/asgi servers.


"""Flight search and AI summary endpoint."""
@app.post("/search_flights/", response_model = Union[AIReturnModel, str])
async def get_flight_info(
    travel_info: TravelRequest,
    serp_service: Annotated[SerpAPIService, Depends()],
    crew_service: Annotated[CrewAPIService, Depends()]
    ) -> AIReturnModel:
    
    try:
        # Search for flights using SERP API
        flights = await serp_service.search_flights(travel_info)
        print(f"Flights found: ")
        # If no flights were parsed, return a simple message
        if not flights:
            return "No flight data was found"
        
        flights_doc = format_data_for_ai(flights)
        ai_flight_summary = await crew_service.generate_flight_summary(travel_info, flights_doc)

        return AIReturnModel(flight_info=flights, ai_flight_summary=ai_flight_summary)
    
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    

"""Hotel search endpoint."""
@app.post("/search_hotels/")
async def get_hotel_info(
    travel_info: TravelRequest,
    serp_service: Annotated[SerpAPIService, Depends()],
    ):

    try:
        hotels = await serp_service.search_hotels(travel_info) 
        return hotels
    
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    
