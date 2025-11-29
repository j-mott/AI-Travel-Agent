from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated
from models.model import AIReturnModel, TravelRequest
from services.serp import SerpAPIService
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
app = FastAPI() # FastAPI application instance used by Uvicorn/asgi servers.

@app.post("/search_flights/", response_model=AIReturnModel)
async def get_flight_info(
    travel_info: TravelRequest,
    serp_service: Annotated[SerpAPIService, Depends()]
    ) -> AIReturnModel:
    
    try:
        flights = await serp_service.search_flights(travel_info)
        return AIReturnModel(flight_info=flights)
    
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    

    
