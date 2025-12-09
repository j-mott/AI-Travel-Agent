import asyncio
import logging
import os
from crewai import Agent, Crew, Process, Task, LLM
from models.model import TravelRequest, BuildCrewOptions

logger = logging.getLogger(__name__)

class CrewAPIService:
    def __init__(self):
        # self.api_key = os.getenv("GEMINI_API_KEY")
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.flight_agent = self.__build_agent("flight")

    async def generate_flight_summary(self, travel_data: TravelRequest, flight_data: str) -> str:
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
            return str(e)
        

    def __create_prompt(self, agent: Agent, options: BuildCrewOptions):
        """Create a prompt for the given agent and options."""

        prompt = """
            From the provided flight data, identify and recommend the top 3 flight options, each selected for a different strength.
            Clearly explain why each flight stands out in one of the following categories:

            🥇 Flight 1 Best Value
                •	💰 Price: Why is this flight the best deal overall?
                •	Consider: lowest cost for features, balanced trade-offs

            🥈 Flight 2 Best Duration
                •	⏱️ Travel Time: Why is this the most time-efficient choice?
                •	Consider: fastest route, minimal layovers, direct flight

            🥉 Flight 3 Best Comfort
                •	💺 Travel Class & Experience: Why does this offer the most comfort or best overall travel experience?
                •	Consider: seat class, onboard amenities, fewer stops, airline quality

            ✅ Instructions:
                •	Use the provided flight data as your source
                •	Do not repeat or summarize the raw flight details
                •	Justify each recommendation clearly and concisely
                •	Make sure the reason for each selection is distinct
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
        llm = "openai/gpt-4.1-mini"
        # llm = "gemini/gemini-2.0-flash"

        llm_model = LLM(
            model = llm,
            api_key = self.api_key,
            temperature = 0.5,
            max_tokens = 1400,
        )

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
                llm=llm_model,
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
            verbose = False, 
        )

