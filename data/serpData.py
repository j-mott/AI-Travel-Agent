import json

def serp_flight_data():
    return json.loads(r'''
{
    "search_metadata": {
        "id": "6928d189302394f7e3bf8303",
        "status": "Success",
        "json_endpoint": "https://serpapi.com/searches/3d977dbd1c1f12d7/6928d189302394f7e3bf8303.json",
        "created_at": "2025-11-27 22:32:41 UTC",
        "processed_at": "2025-11-27 22:32:41 UTC",
        "google_flights_url": "https://www.google.com/travel/flights?hl=en&gl=us&curr=CAD&tfs=CBwQAhoeEgoyMDI2LTAyLTAxagcIARIDWVlacgcIARIDTUFOGh4SCjIwMjYtMDItMTBqBwgBEgNNQU5yBwgBEgNZWVpCAQFIAXABmAEB&tfu=EgIIAQ",
        "raw_html_file": "https://serpapi.com/searches/3d977dbd1c1f12d7/6928d189302394f7e3bf8303.html",
        "prettify_html_file": "https://serpapi.com/searches/3d977dbd1c1f12d7/6928d189302394f7e3bf8303.prettify",
        "total_time_taken": 0.44
    },
    "search_parameters": {
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "departure_id": "YYZ",
        "arrival_id": "MAN",
        "outbound_date": "2026-02-01",
        "return_date": "2026-02-10",
        "adults": 1,
        "currency": "CAD"
    },
    "best_flights": [
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 17:25"
            },
            "arrival_airport": {
                "name": "Dublin Airport",
                "id": "DUB",
                "time": "2026-02-02 05:15"
            },
            "duration": 410,
            "airplane": "Airbus A321neo",
            "airline": "Aer Lingus",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/EI.png",
            "travel_class": "Economy",
            "flight_number": "EI 126",
            "ticket_also_sold_by": [
                "British Airways"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "On-demand video",
                "Carbon emissions estimate: 384 kg"
            ],
            "overnight": true
            },
            {
            "departure_airport": {
                "name": "Dublin Airport",
                "id": "DUB",
                "time": "2026-02-02 06:30"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-02 07:35"
            },
            "duration": 65,
            "airplane": "Airbus A320",
            "airline": "Aer Lingus",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/EI.png",
            "travel_class": "Economy",
            "flight_number": "EI 202",
            "ticket_also_sold_by": [
                "British Airways"
            ],
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "Carbon emissions estimate: 48 kg"
            ]
            }
        ],
        "layovers": [
            {
            "duration": 75,
            "name": "Dublin Airport",
            "id": "DUB"
            }
        ],
        "total_duration": 550,
        "carbon_emissions": {
            "this_flight": 434000,
            "typical_for_this_route": 420000,
            "difference_percent": 3
        },
        "price": 932,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/EI.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3RGU1RFeU5ueEZTVEl3TWhvTENJUFlCUkFDR2dORFFVUTRISERraGdRPSIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIkRVQiIsbnVsbCwiRUkiLCIxMjYiXSxbIkRVQiIsIjIwMjYtMDItMDIiLCJNQU4iLG51bGwsIkVJIiwiMjAyIl1dXQ=="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 19:40"
            },
            "arrival_airport": {
                "name": "Keflavík International Airport",
                "id": "KEF",
                "time": "2026-02-02 06:25"
            },
            "duration": 345,
            "airplane": "Boeing 737MAX 9 Passenger",
            "airline": "Icelandair",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FI.png",
            "travel_class": "Economy",
            "flight_number": "FI 602",
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat USB outlet",
                "On-demand video",
                "Carbon emissions estimate: 309 kg"
            ],
            "overnight": true
            },
            {
            "departure_airport": {
                "name": "Keflavík International Airport",
                "id": "KEF",
                "time": "2026-02-02 08:00"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-02 10:45"
            },
            "duration": 165,
            "airplane": "Boeing 737MAX 8 Passenger",
            "airline": "Icelandair",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FI.png",
            "travel_class": "Economy",
            "flight_number": "FI 440",
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat USB outlet",
                "On-demand video",
                "Carbon emissions estimate: 147 kg"
            ]
            }
        ],
        "layovers": [
            {
            "duration": 95,
            "name": "Keflavík International Airport",
            "id": "KEF"
            }
        ],
        "total_duration": 605,
        "carbon_emissions": {
            "this_flight": 457000,
            "typical_for_this_route": 420000,
            "difference_percent": 9
        },
        "price": 939,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/FI.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3RHU1RZd01ueEdTVFEwTUJvTENQL2NCUkFDR2dORFFVUTRISENwaWdRPSIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIktFRiIsbnVsbCwiRkkiLCI2MDIiXSxbIktFRiIsIjIwMjYtMDItMDIiLCJNQU4iLG51bGwsIkZJIiwiNDQwIl1dXQ=="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 12:07"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-01 14:01"
            },
            "duration": 114,
            "airplane": "Canadair RJ 900",
            "airline": "Delta",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
            "travel_class": "Economy",
            "flight_number": "DL 5098",
            "ticket_also_sold_by": [
                "KLM",
                "Air France"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "Carbon emissions estimate: 111 kg"
            ],
            "plane_and_crew_by": "Endeavor Air DBA Delta Connection"
            },
            {
            "departure_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-01 18:40"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-02 06:40"
            },
            "duration": 420,
            "airplane": "Airbus A330",
            "airline": "Virgin Atlantic",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/VS.png",
            "travel_class": "Economy",
            "flight_number": "VS 128",
            "ticket_also_sold_by": [
                "KLM",
                "Air France",
                "Delta"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat USB outlet",
                "On-demand video",
                "Carbon emissions estimate: 406 kg"
            ],
            "overnight": true
            }
        ],
        "layovers": [
            {
            "duration": 279,
            "name": "John F. Kennedy International Airport",
            "id": "JFK"
            }
        ],
        "total_duration": 813,
        "carbon_emissions": {
            "this_flight": 518000,
            "typical_for_this_route": 420000,
            "difference_percent": 23
        },
        "price": 972,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/multi.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3hFVERVd09UaDhWbE14TWpnYUN3alo5Z1VRQWhvRFEwRkVPQnh3MFp3RSIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIkpGSyIsbnVsbCwiREwiLCI1MDk4Il0sWyJKRksiLCIyMDI2LTAyLTAxIiwiTUFOIixudWxsLCJWUyIsIjEyOCJdXV0="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 16:50"
            },
            "arrival_airport": {
                "name": "Frankfurt Airport",
                "id": "FRA",
                "time": "2026-02-02 06:40"
            },
            "duration": 470,
            "airplane": "Boeing 787",
            "airline": "Air Canada",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AC.png",
            "travel_class": "Economy",
            "flight_number": "AC 840",
            "ticket_also_sold_by": [
                "Lufthansa"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "On-demand video",
                "Carbon emissions estimate: 336 kg"
            ],
            "overnight": true
            },
            {
            "departure_airport": {
                "name": "Frankfurt Airport",
                "id": "FRA",
                "time": "2026-02-02 07:55"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-02 08:45"
            },
            "duration": 110,
            "airplane": "Airbus A319",
            "airline": "Lufthansa",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LH.png",
            "travel_class": "Economy",
            "flight_number": "LH 940",
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "Wi-Fi for a fee",
                "Carbon emissions estimate: 109 kg"
            ]
            }
        ],
        "layovers": [
            {
            "duration": 75,
            "name": "Frankfurt Airport",
            "id": "FRA"
            }
        ],
        "total_duration": 655,
        "carbon_emissions": {
            "this_flight": 446000,
            "typical_for_this_route": 420000,
            "difference_percent": 6
        },
        "price": 1030,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/multi.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3RCUXpnME1IeE1TRGswTUJvTENMT2tCaEFDR2dORFFVUTRISENhdlFRPSIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIkZSQSIsbnVsbCwiQUMiLCI4NDAiXSxbIkZSQSIsIjIwMjYtMDItMDIiLCJNQU4iLG51bGwsIkxIIiwiOTQwIl1dXQ=="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 18:05"
            },
            "arrival_airport": {
                "name": "Heathrow Airport",
                "id": "LHR",
                "time": "2026-02-02 06:15"
            },
            "duration": 430,
            "airplane": "Boeing 787",
            "airline": "British Airways",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/BA.png",
            "travel_class": "Economy",
            "flight_number": "BA 92",
            "ticket_also_sold_by": [
                "American",
                "Finnair"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "In-seat power & USB outlets",
                "On-demand video",
                "Carbon emissions estimate: 344 kg"
            ],
            "overnight": true
            },
            {
            "departure_airport": {
                "name": "Heathrow Airport",
                "id": "LHR",
                "time": "2026-02-02 07:45"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-02 08:50"
            },
            "duration": 65,
            "airplane": "Airbus A320",
            "airline": "British Airways",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/BA.png",
            "travel_class": "Economy",
            "flight_number": "BA 1360",
            "ticket_also_sold_by": [
                "American"
            ],
            "legroom": "29 in",
            "extensions": [
                "Below average legroom (29 in)",
                "Wi-Fi for a fee",
                "In-seat USB outlet",
                "Carbon emissions estimate: 47 kg"
            ]
            }
        ],
        "layovers": [
            {
            "duration": 90,
            "name": "Heathrow Airport",
            "id": "LHR"
            }
        ],
        "total_duration": 585,
        "carbon_emissions": {
            "this_flight": 391000,
            "typical_for_this_route": 420000,
            "difference_percent": -7
        },
        "price": 1127,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/BA.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3RDUVRreWZFSkJNVE0yTUJvTENJUHdCaEFDR2dORFFVUTRISENNOHdRPSIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIkxIUiIsbnVsbCwiQkEiLCI5MiJdLFsiTEhSIiwiMjAyNi0wMi0wMiIsIk1BTiIsbnVsbCwiQkEiLCIxMzYwIl1dXQ=="
        }
    ],
    "other_flights": [
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 18:13"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-01 20:18"
            },
            "duration": 125,
            "airplane": "Canadair RJ 900",
            "airline": "Delta",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
            "travel_class": "Economy",
            "flight_number": "DL 5163",
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "Carbon emissions estimate: 111 kg"
            ],
            "plane_and_crew_by": "Endeavor Air DBA Delta Connection"
            },
            {
            "departure_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-02 18:40"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-03 06:40"
            },
            "duration": 420,
            "airplane": "Airbus A330",
            "airline": "Virgin Atlantic",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/VS.png",
            "travel_class": "Economy",
            "flight_number": "VS 128",
            "ticket_also_sold_by": [
                "Delta"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat USB outlet",
                "On-demand video",
                "Carbon emissions estimate: 406 kg"
            ],
            "overnight": true
            }
        ],
        "layovers": [
            {
            "duration": 1342,
            "name": "John F. Kennedy International Airport",
            "id": "JFK",
            "overnight": true
            }
        ],
        "total_duration": 1887,
        "carbon_emissions": {
            "this_flight": 518000,
            "typical_for_this_route": 420000,
            "difference_percent": 23
        },
        "price": 976,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/multi.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3hFVERVeE5qTjhWbE14TWpnYUN3aWwrZ1VRQWhvRFEwRkVPQnh3bVo4RSIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIkpGSyIsbnVsbCwiREwiLCI1MTYzIl0sWyJKRksiLCIyMDI2LTAyLTAyIiwiTUFOIixudWxsLCJWUyIsIjEyOCJdXV0="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 18:15"
            },
            "arrival_airport": {
                "name": "Frankfurt Airport",
                "id": "FRA",
                "time": "2026-02-02 07:55"
            },
            "duration": 460,
            "airplane": "Boeing 787",
            "airline": "Lufthansa",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LH.png",
            "travel_class": "Economy",
            "flight_number": "LH 471",
            "ticket_also_sold_by": [
                "Air Canada"
            ],
            "legroom": "32 in",
            "extensions": [
                "Above average legroom (32 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "On-demand video",
                "Carbon emissions estimate: 378 kg"
            ],
            "overnight": true
            },
            {
            "departure_airport": {
                "name": "Frankfurt Airport",
                "id": "FRA",
                "time": "2026-02-02 11:30"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-02 12:20"
            },
            "duration": 110,
            "airplane": "Airbus A319",
            "airline": "Lufthansa",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LH.png",
            "travel_class": "Economy",
            "flight_number": "LH 942",
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "Wi-Fi for a fee",
                "Carbon emissions estimate: 109 kg"
            ]
            }
        ],
        "layovers": [
            {
            "duration": 215,
            "name": "Frankfurt Airport",
            "id": "FRA"
            }
        ],
        "total_duration": 785,
        "carbon_emissions": {
            "this_flight": 488000,
            "typical_for_this_route": 420000,
            "difference_percent": 16
        },
        "price": 1030,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LH.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3RNU0RRM01YeE1TRGswTWhvTENMT2tCaEFDR2dORFFVUTRISENhdlFRPSIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIkZSQSIsbnVsbCwiTEgiLCI0NzEiXSxbIkZSQSIsIjIwMjYtMDItMDIiLCJNQU4iLG51bGwsIkxIIiwiOTQyIl1dXQ=="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 21:30"
            },
            "arrival_airport": {
                "name": "Frankfurt Airport",
                "id": "FRA",
                "time": "2026-02-02 11:10"
            },
            "duration": 460,
            "airplane": "Boeing 787",
            "airline": "Air Canada",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AC.png",
            "travel_class": "Economy",
            "flight_number": "AC 842",
            "ticket_also_sold_by": [
                "Lufthansa"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "On-demand video",
                "Carbon emissions estimate: 336 kg"
            ],
            "overnight": true
            },
            {
            "departure_airport": {
                "name": "Frankfurt Airport",
                "id": "FRA",
                "time": "2026-02-02 14:00"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-02 14:50"
            },
            "duration": 110,
            "airplane": "Airbus A319",
            "airline": "Lufthansa",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/LH.png",
            "travel_class": "Economy",
            "flight_number": "LH 944",
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "Wi-Fi for a fee",
                "Carbon emissions estimate: 109 kg"
            ]
            }
        ],
        "layovers": [
            {
            "duration": 170,
            "name": "Frankfurt Airport",
            "id": "FRA"
            }
        ],
        "total_duration": 740,
        "carbon_emissions": {
            "this_flight": 446000,
            "typical_for_this_route": 420000,
            "difference_percent": 6
        },
        "price": 1105,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/multi.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3RCUXpnME1ueE1TRGswTkJvTENQL2VCaEFDR2dORFFVUTRISEQ2NWdRPSIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIkZSQSIsbnVsbCwiQUMiLCI4NDIiXSxbIkZSQSIsIjIwMjYtMDItMDIiLCJNQU4iLG51bGwsIkxIIiwiOTQ0Il1dXQ=="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-01 17:50"
            },
            "arrival_airport": {
                "name": "Amsterdam Airport Schiphol",
                "id": "AMS",
                "time": "2026-02-02 07:05"
            },
            "duration": 435,
            "airplane": "Boeing 787-10",
            "airline": "KLM",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/KL.png",
            "travel_class": "Economy",
            "flight_number": "KL 692",
            "ticket_also_sold_by": [
                "Virgin Atlantic"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat USB outlet",
                "On-demand video",
                "Carbon emissions estimate: 309 kg"
            ],
            "overnight": true
            },
            {
            "departure_airport": {
                "name": "Amsterdam Airport Schiphol",
                "id": "AMS",
                "time": "2026-02-02 07:55"
            },
            "arrival_airport": {
                "name": "Manchester Airport",
                "id": "MAN",
                "time": "2026-02-02 08:20"
            },
            "duration": 85,
            "airplane": "Boeing 737",
            "airline": "KLM",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/KL.png",
            "travel_class": "Economy",
            "flight_number": "KL 1029",
            "ticket_also_sold_by": [
                "Virgin Atlantic"
            ],
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "In-seat USB outlet",
                "Carbon emissions estimate: 57 kg"
            ]
            }
        ],
        "layovers": [
            {
            "duration": 50,
            "name": "Amsterdam Airport Schiphol",
            "id": "AMS"
            }
        ],
        "total_duration": 570,
        "carbon_emissions": {
            "this_flight": 367000,
            "typical_for_this_route": 420000,
            "difference_percent": -13
        },
        "price": 1217,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/KL.png",
        "departure_token": "WyJDalJJUjJsalFuTnRRWEIyVEUxQlFYQklZbEZDUnkwdExTMHRMUzB0TFhaM1ltbHhORUZCUVVGQlIydHZNRmxyU20xRU0yRkJFZ3hMVERZNU1ueExUREV3TWprYUN3amR0Z2NRQWhvRFEwRkVPQnh3dmFVRiIsW1siWVlaIiwiMjAyNi0wMi0wMSIsIkFNUyIsbnVsbCwiS0wiLCI2OTIiXSxbIkFNUyIsIjIwMjYtMDItMDIiLCJNQU4iLG51bGwsIktMIiwiMTAyOSJdXV0="
        }
    ],
    "price_insights": {
        "lowest_price": 932,
        "price_level": "high",
        "typical_price_range": [
        810,
        910
        ],
        "price_history": [
        [
            1759032000,
            848
        ],
        [
            1759118400,
            848
        ],
        [
            1759204800,
            848
        ],
        [
            1759291200,
            832
        ],
        [
            1759377600,
            832
        ],
        [
            1759464000,
            833
        ],
        [
            1759550400,
            794
        ],
        [
            1759636800,
            794
        ],
        [
            1759723200,
            754
        ],
        [
            1759809600,
            754
        ],
        [
            1759896000,
            793
        ],
        [
            1759982400,
            793
        ],
        [
            1760068800,
            832
        ],
        [
            1760155200,
            831
        ],
        [
            1760241600,
            831
        ],
        [
            1760328000,
            831
        ],
        [
            1760414400,
            831
        ],
        [
            1760500800,
            832
        ],
        [
            1760587200,
            832
        ],
        [
            1760673600,
            832
        ],
        [
            1760760000,
            833
        ],
        [
            1760846400,
            835
        ],
        [
            1760932800,
            835
        ],
        [
            1761019200,
            834
        ],
        [
            1761105600,
            794
        ],
        [
            1761192000,
            793
        ],
        [
            1761278400,
            792
        ],
        [
            1761364800,
            791
        ],
        [
            1761451200,
            791
        ],
        [
            1761537600,
            791
        ],
        [
            1761624000,
            791
        ],
        [
            1761710400,
            791
        ],
        [
            1761796800,
            791
        ],
        [
            1761883200,
            788
        ],
        [
            1761969600,
            788
        ],
        [
            1762056000,
            788
        ],
        [
            1762146000,
            788
        ],
        [
            1762232400,
            788
        ],
        [
            1762318800,
            812
        ],
        [
            1762405200,
            812
        ],
        [
            1762491600,
            812
        ],
        [
            1762578000,
            812
        ],
        [
            1762664400,
            813
        ],
        [
            1762750800,
            813
        ],
        [
            1762837200,
            813
        ],
        [
            1762923600,
            813
        ],
        [
            1763010000,
            813
        ],
        [
            1763096400,
            812
        ],
        [
            1763182800,
            812
        ],
        [
            1763269200,
            813
        ],
        [
            1763355600,
            813
        ],
        [
            1763442000,
            866
        ],
        [
            1763528400,
            866
        ],
        [
            1763614800,
            849
        ],
        [
            1763701200,
            849
        ],
        [
            1763787600,
            849
        ],
        [
            1763874000,
            849
        ],
        [
            1763960400,
            849
        ],
        [
            1764046800,
            849
        ],
        [
            1764133200,
            850
        ],
        [
            1764219600,
            932
        ]
        ]
    },
    "airports": [
        {
        "departure": [
            {
            "airport": {
                "id": "YYZ",
                "name": "Toronto Pearson International Airport"
            },
            "city": "Toronto",
            "country": "Canada",
            "country_code": "CA",
            "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQWPEoHJ9ZdKzv94rrhqqT-m_aOLtacPBnX8s8Fd4GzxCQ8BmgveJ72xmyMfMSLarPprt6XrklbwK-_tw",
            "thumbnail": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQGhv7dw8LBbMsCv9kv586cMlQBryS9N16uYov7WUD7Mbc1QBEkyd7o1Tf1013cK2ZjzDJu2uYY3WF5w-iQkYUeu4tKg9DR1vjDtJ9vRcA"
            }
        ],
        "arrival": [
            {
            "airport": {
                "id": "MAN",
                "name": "Manchester Airport"
            },
            "city": "Manchester",
            "country": "United Kingdom",
            "country_code": "GB",
            "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTTNUewWaPkLx7U-O4QLkOffkKe-vWjkPMFEowfMNAam9aJq5A78vp54NH8-Dwv8UcK-KJgvBgQf3aeKA",
            "thumbnail": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRYI78ftzh_cqqBG1wANTxyA6EVwiaKoPgvx8hE-VaF6lS8uXN_eCq0APuFsRFtejaYshXoPMA_BqWvSPOjkxgh1gXGBgmWyOJKFAwHb_4"
            }
        ]
        },
        {
        "departure": [
            {
            "airport": {
                "id": "MAN",
                "name": "Manchester Airport"
            },
            "city": "Manchester",
            "country": "United Kingdom",
            "country_code": "GB",
            "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTTNUewWaPkLx7U-O4QLkOffkKe-vWjkPMFEowfMNAam9aJq5A78vp54NH8-Dwv8UcK-KJgvBgQf3aeKA",
            "thumbnail": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRYI78ftzh_cqqBG1wANTxyA6EVwiaKoPgvx8hE-VaF6lS8uXN_eCq0APuFsRFtejaYshXoPMA_BqWvSPOjkxgh1gXGBgmWyOJKFAwHb_4"
            }
        ],
        "arrival": [
            {
            "airport": {
                "id": "YYZ",
                "name": "Toronto Pearson International Airport"
            },
            "city": "Toronto",
            "country": "Canada",
            "country_code": "CA",
            "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQWPEoHJ9ZdKzv94rrhqqT-m_aOLtacPBnX8s8Fd4GzxCQ8BmgveJ72xmyMfMSLarPprt6XrklbwK-_tw",
            "thumbnail": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQGhv7dw8LBbMsCv9kv586cMlQBryS9N16uYov7WUD7Mbc1QBEkyd7o1Tf1013cK2ZjzDJu2uYY3WF5w-iQkYUeu4tKg9DR1vjDtJ9vRcA"
            }
        ]
        }
    ]
    }
''')