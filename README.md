# AI-Travel-Agent
A multi-agent AI travel planner

## Overview
AI-Travel-Agent is an AI-powered travel assistant that finds and evaluates flights for you. It gathers flight options, normalizes them into clear data models, and uses an agent (CrewAI) to recommend the best choice based on price, airline reputation, duration, layovers, and travel class. The result is a concise, reasoned summary tailored to your trip details, so you can book confidently without sifting through pages of results.


## Endpoints
- `POST /search_flights/` – Parses flight results and returns data with an optional AI summary.
	- Body (JSON):
		- `departure_city` (string) – Origin city name or code.
		- `arrival_city` (string) – Destination city name or code.
		- `departure_date` (string, ISO `YYYY-MM-DD`) – Outbound date.
		- `return_date` (string, ISO `YYYY-MM-DD`, optional) – Return date.
		- `passengers` (integer, default `1`) – Number of travelers.
	- Response:
		- `flights` (array) – Parsed flight options.
		- `ai_summary` (string, optional) – CrewAI recommendation when an LLM key is set.
