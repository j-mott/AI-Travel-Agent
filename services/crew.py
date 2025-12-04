import asyncio
import logging
import os
from crewai import Agent, Crew, Process, Task
from models.model import TravelRequest, BuildCrewOptions

logger = logging.getLogger(__name__)

class CrewAPIService:
    def __init__(self):
        self.flight_agent = self.__build_agent("flight")

    async def generate_flight_summary(self, travel_data: TravelRequest,flight_data: str) -> str:
        logger.info("Generating flight summary using CrewAI...")
        
        options = BuildCrewOptions(
            flight_info = flight_data,
            departure_city = travel_data.departure_city,
            arrival_city = travel_data.arrival_city,
            departure_date = travel_data.departure_date,
            return_date = travel_data.return_date,
            passengers = travel_data.passengers
        )

        crew = self.__create_crew(options)
        try:
            results = await asyncio.to_thread(crew.kickoff)

            if hasattr(results, 'raw'):
                logger.info("CrewAI flight summary generated successfully.")
                return results.raw
            else:
                logger.info("CrewAI flight summary generated successfully.")
                return str(results)
        
        except Exception as e:
            logger.error("Error during CrewAI flight summary generation: %s", e)
            return e
        

    def __create_prompt(self, agent: Agent, options: BuildCrewOptions):
        """Create a prompt for the given agent and options.
        Uses getattr to avoid attribute errors if Agent does not expose 'name'.
        """

        prompt = """
            Recommend the best flight option based on the data provided.
            
            Your recommendation must include a clear justification across the following criteria:
            • Price: Explain why this option offers the best value compared to others.
            • Airlines: Highlight the airlines involved and their reputations.
            • Duration: Justify the flights total travel time and how it compares favorably.
            • Layovers: Assess the number of layovers and why this route is optimal.
            • Travel Class: Describe why this option offers the best comfort, class, or onboard experience.

            Important:
            • Use only the provided flight data.
            • Do not repeat or summarize the flight details focus on your reasoned recommendation.  
            
            Flight Data:
            """

        # Attach structured flight data to the prompt so the agent has context
        if options and getattr(options, "flight_info", None):
            prompt = f"{prompt}\n{options.flight_info}"

        return Task(
            agent = agent,
            description = prompt,
            expected_output = "Concise flight recommendation with justification."
        )

                
    def __build_agent(self, agent_type: str) -> Agent:
        """Create and return a CrewAI agent based on the specified type."""

        if agent_type == "flight":
            return Agent(
                name="Flight Info Agent",
                role="Provides detailed summaries of flight options based on provided data.",
                goal=(
                    "Analyze flight data and generate a clear, concise summary highlighting price, duration, layovers, and airlines."
                ),
                backstory=(
                    "You are a helpful travel assistant specializing in comparing flight options and presenting user-friendly summaries."
                ),
                verbose = False,
                allow_delegation = False,
            )

    def __create_crew(self, options: BuildCrewOptions) -> Crew:
        """Create a crew for the given workflow type."""
        agent = self.flight_agent
        task = self.__create_prompt(agent, options)
        return Crew(
            tasks = [task],
            agents = [agent],
            process = Process.sequential,
            memory = False,
            verbose = False, 
        )

