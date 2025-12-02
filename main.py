from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated
from models.model import AIReturnModel, TravelRequest
from helpers.helper import format_data_for_ai
from services.serp import SerpAPIService
from services.crew import CrewAPIService
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
app = FastAPI() # FastAPI application instance used by Uvicorn/asgi servers.

@app.post("/search_flights/", response_model=AIReturnModel)
async def get_flight_info(
    travel_info: TravelRequest,
    serp_service: Annotated[SerpAPIService, Depends()],
    crew_service: Annotated[CrewAPIService, Depends()]
    ) -> AIReturnModel:
    
    try:
        flights = await serp_service.search_flights(travel_info)
        flights_doc = format_data_for_ai(flights)

        return AIReturnModel(flight_info=flights)
    
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    

    
