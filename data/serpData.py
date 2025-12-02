import json

def serp_flight_data():
    return json.loads(r'''
    {
    "search_metadata": {
        "id": "692f40febd1731899f939947",
        "status": "Success",
        "json_endpoint": "https://serpapi.com/searches/4b4d30e44e2de780/692f40febd1731899f939947.json",
        "created_at": "2025-12-02 19:41:50 UTC",
        "processed_at": "2025-12-02 19:41:50 UTC",
        "google_flights_url": "https://www.google.com/travel/flights?hl=en&gl=ca&curr=CAD&tfs=CBwQAhoeEgoyMDI2LTAyLTA1agcIARIDWVlacgcIARIDSkZLGh4SCjIwMjYtMDItMTNqBwgBEgNKRktyBwgBEgNZWVpCAQFIAXABmAEB&tfu=EgIIAQ",
        "raw_html_file": "https://serpapi.com/searches/4b4d30e44e2de780/692f40febd1731899f939947.html",
        "prettify_html_file": "https://serpapi.com/searches/4b4d30e44e2de780/692f40febd1731899f939947.prettify",
        "total_time_taken": 1.36
    },
    "search_parameters": {
        "engine": "google_flights",
        "hl": "en",
        "gl": "ca",
        "departure_id": "YYZ",
        "arrival_id": "JFK",
        "outbound_date": "2026-02-05",
        "return_date": "2026-02-13",
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
                "time": "2026-02-05 07:00"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-05 09:00"
            },
            "duration": 120,
            "airplane": "Embraer 175",
            "airline": "American",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
            "travel_class": "Economy",
            "flight_number": "AA 4559",
            "ticket_also_sold_by": [
                "Porter Airlines"
            ],
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "Stream media to your device",
                "Carbon emissions estimate: 110 kg"
            ],
            "plane_and_crew_by": "Republic Airways as American Eagle"
            }
        ],
        "total_duration": 120,
        "carbon_emissions": {
            "this_flight": 111000,
            "typical_for_this_route": 98000,
            "difference_percent": 13
        },
        "price": 349,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZ1pCUVRRMU5Ua2FDd2lya0FJUUFob0RRMEZFT0J4dzhNSUIiLFtbIllZWiIsIjIwMjYtMDItMDUiLCJKRksiLG51bGwsIkFBIiwiNDU1OSJdXV0="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-05 10:30"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-05 12:15"
            },
            "duration": 105,
            "airplane": "Embraer 175",
            "airline": "American",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
            "travel_class": "Economy",
            "flight_number": "AA 4552",
            "ticket_also_sold_by": [
                "Porter Airlines"
            ],
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "Stream media to your device",
                "Carbon emissions estimate: 110 kg"
            ],
            "plane_and_crew_by": "Republic Airways as American Eagle"
            }
        ],
        "total_duration": 105,
        "carbon_emissions": {
            "this_flight": 111000,
            "typical_for_this_route": 98000,
            "difference_percent": 13
        },
        "price": 349,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZ1pCUVRRMU5USWFDd2lya0FJUUFob0RRMEZFT0J4dzhNSUIiLFtbIllZWiIsIjIwMjYtMDItMDUiLCJKRksiLG51bGwsIkFBIiwiNDU1MiJdXV0="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-05 20:55"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-05 22:39"
            },
            "duration": 104,
            "airplane": "Embraer 175",
            "airline": "Air Canada",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AC.png",
            "travel_class": "Economy",
            "flight_number": "AC 8556",
            "ticket_also_sold_by": [
                "United"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "In-seat USB outlet",
                "Stream media to your device",
                "Carbon emissions estimate: 110 kg"
            ],
            "plane_and_crew_by": "Air Canada Express - Jazz"
            }
        ],
        "total_duration": 104,
        "carbon_emissions": {
            "this_flight": 111000,
            "typical_for_this_route": 98000,
            "difference_percent": 13
        },
        "price": 416,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AC.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZ1pCUXpnMU5UWWFDd2lreEFJUUFob0RRMEZFT0J4d2h1Z0IiLFtbIllZWiIsIjIwMjYtMDItMDUiLCJKRksiLG51bGwsIkFDIiwiODU1NiJdXV0="
        }
    ],
    "other_flights": [
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-05 10:59"
            },
            "arrival_airport": {
                "name": "Ronald Reagan Washington National Airport",
                "id": "DCA",
                "time": "2026-02-05 12:49"
            },
            "duration": 110,
            "airplane": "Canadair RJ 900",
            "airline": "American",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
            "travel_class": "Economy",
            "flight_number": "AA 5668",
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "Stream media to your device",
                "Carbon emissions estimate: 100 kg"
            ],
            "plane_and_crew_by": "PSA Airlines as American Eagle"
            },
            {
            "departure_airport": {
                "name": "Ronald Reagan Washington National Airport",
                "id": "DCA",
                "time": "2026-02-05 13:35"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-05 14:57"
            },
            "duration": 82,
            "airplane": "Embraer 175",
            "airline": "American",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
            "travel_class": "Economy",
            "flight_number": "AA 4522",
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "Stream media to your device",
                "Carbon emissions estimate: 80 kg"
            ],
            "plane_and_crew_by": "Republic Airways as American Eagle"
            }
        ],
        "layovers": [
            {
            "duration": 46,
            "name": "Ronald Reagan Washington National Airport",
            "id": "DCA"
            }
        ],
        "total_duration": 238,
        "carbon_emissions": {
            "this_flight": 181000,
            "typical_for_this_route": 98000,
            "difference_percent": 85
        },
        "price": 349,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZzFCUVRVMk5qaDhRVUUwTlRJeUdnc0lxNUFDRUFJYUEwTkJSRGdjY1BEQ0FRPT0iLFtbIllZWiIsIjIwMjYtMDItMDUiLCJEQ0EiLG51bGwsIkFBIiwiNTY2OCJdLFsiRENBIiwiMjAyNi0wMi0wNSIsIkpGSyIsbnVsbCwiQUEiLCI0NTIyIl1dXQ=="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-05 17:15"
            },
            "arrival_airport": {
                "name": "Ronald Reagan Washington National Airport",
                "id": "DCA",
                "time": "2026-02-05 19:14"
            },
            "duration": 119,
            "airplane": "Canadair RJ 700",
            "airline": "American",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
            "travel_class": "Economy",
            "flight_number": "AA 5667",
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "Stream media to your device",
                "Carbon emissions estimate: 118 kg"
            ],
            "often_delayed_by_over_30_min": true,
            "plane_and_crew_by": "PSA Airlines as American Eagle"
            },
            {
            "departure_airport": {
                "name": "Ronald Reagan Washington National Airport",
                "id": "DCA",
                "time": "2026-02-06 06:10"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-06 07:27"
            },
            "duration": 77,
            "airplane": "Embraer 175",
            "airline": "American",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
            "travel_class": "Economy",
            "flight_number": "AA 4396",
            "legroom": "30 in",
            "extensions": [
                "Average legroom (30 in)",
                "Wi-Fi for a fee",
                "In-seat power & USB outlets",
                "Stream media to your device",
                "Carbon emissions estimate: 80 kg"
            ],
            "plane_and_crew_by": "Republic Airways as American Eagle"
            }
        ],
        "layovers": [
            {
            "duration": 656,
            "name": "Ronald Reagan Washington National Airport",
            "id": "DCA",
            "overnight": true
            }
        ],
        "total_duration": 852,
        "carbon_emissions": {
            "this_flight": 200000,
            "typical_for_this_route": 98000,
            "difference_percent": 104
        },
        "price": 349,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AA.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZzFCUVRVMk5qZDhRVUUwTXprMkdnc0lxNUFDRUFJYUEwTkJSRGdjY1BEQ0FRPT0iLFtbIllZWiIsIjIwMjYtMDItMDUiLCJEQ0EiLG51bGwsIkFBIiwiNTY2NyJdLFsiRENBIiwiMjAyNi0wMi0wNiIsIkpGSyIsbnVsbCwiQUEiLCI0Mzk2Il1dXQ=="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-05 14:30"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-05 16:09"
            },
            "duration": 99,
            "airplane": "Embraer 175",
            "airline": "Air Canada",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AC.png",
            "travel_class": "Economy",
            "flight_number": "AC 8554",
            "ticket_also_sold_by": [
                "United"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "In-seat USB outlet",
                "Stream media to your device",
                "Carbon emissions estimate: 110 kg"
            ],
            "plane_and_crew_by": "Air Canada Express - Jazz"
            }
        ],
        "total_duration": 99,
        "carbon_emissions": {
            "this_flight": 111000,
            "typical_for_this_route": 98000,
            "difference_percent": 13
        },
        "price": 454,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/AC.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZ1pCUXpnMU5UUWFDd2kzNGdJUUFob0RRMEZFT0J4d3ovMEIiLFtbIllZWiIsIjIwMjYtMDItMDUiLCJKRksiLG51bGwsIkFDIiwiODU1NCJdXV0="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-05 06:00"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-05 08:04"
            },
            "duration": 124,
            "airplane": "Canadair RJ 900",
            "airline": "Delta",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
            "travel_class": "Economy",
            "flight_number": "DL 5066",
            "ticket_also_sold_by": [
                "WestJet"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "Carbon emissions estimate: 111 kg"
            ],
            "plane_and_crew_by": "Endeavor Air DBA Delta Connection"
            }
        ],
        "total_duration": 124,
        "carbon_emissions": {
            "this_flight": 112000,
            "typical_for_this_route": 98000,
            "difference_percent": 14
        },
        "price": 534,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZ1pFVERVd05qWWFDd2lYb1FNUUFob0RRMEZFT0J4d3dxb0MiLFtbIllZWiIsIjIwMjYtMDItMDUiLCJKRksiLG51bGwsIkRMIiwiNTA2NiJdXV0="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-05 18:13"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-05 20:18"
            },
            "duration": 125,
            "airplane": "Canadair RJ 900",
            "airline": "Delta",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
            "travel_class": "Economy",
            "flight_number": "DL 5163",
            "ticket_also_sold_by": [
                "WestJet"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "Carbon emissions estimate: 111 kg"
            ],
            "plane_and_crew_by": "Endeavor Air DBA Delta Connection"
            }
        ],
        "total_duration": 125,
        "carbon_emissions": {
            "this_flight": 112000,
            "typical_for_this_route": 98000,
            "difference_percent": 14
        },
        "price": 573,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZ1pFVERVeE5qTWFDd2pFdndNUUFob0RRMEZFT0J4d25zQUMiLFtbIllZWiIsIjIwMjYtMDItMDUiLCJKRksiLG51bGwsIkRMIiwiNTE2MyJdXV0="
        },
        {
        "flights": [
            {
            "departure_airport": {
                "name": "Toronto Pearson International Airport",
                "id": "YYZ",
                "time": "2026-02-05 12:07"
            },
            "arrival_airport": {
                "name": "John F. Kennedy International Airport",
                "id": "JFK",
                "time": "2026-02-05 14:01"
            },
            "duration": 114,
            "airplane": "Canadair RJ 900",
            "airline": "Delta",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
            "travel_class": "Economy",
            "flight_number": "DL 5098",
            "ticket_also_sold_by": [
                "WestJet"
            ],
            "legroom": "31 in",
            "extensions": [
                "Average legroom (31 in)",
                "Wi-Fi for a fee",
                "Carbon emissions estimate: 111 kg"
            ],
            "plane_and_crew_by": "Endeavor Air DBA Delta Connection"
            }
        ],
        "total_duration": 114,
        "carbon_emissions": {
            "this_flight": 112000,
            "typical_for_this_route": 98000,
            "difference_percent": 14
        },
        "price": 699,
        "type": "Round trip",
        "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
        "extensions": [
            "Checked baggage for a fee",
            "Bag and fare conditions depend on the return flight"
        ],
        "departure_token": "WyJDalJJY1hKa01HUllObmhpUjBsQlJUWjFjVkZDUnkwdExTMHRMUzB0TFhsc2JIRXhNVUZCUVVGQlIydDJVVkE0UVRReVNESkJFZ1pFVERVd09UZ2FDd2o4b1FRUUFob0RRMEZFT0J4dzE0WUQiLFtbIllZWiIsIjIwMjYtMDItMDUiLCJKRksiLG51bGwsIkRMIiwiNTA5OCJdXV0="
        }
    ],
    "price_insights": {
        "lowest_price": 349,
        "price_level": "typical",
        "typical_price_range": [
        330,
        410
        ],
        "price_history": [
        [
            1759464000,
            328
        ],
        [
            1759550400,
            380
        ],
        [
            1759636800,
            380
        ],
        [
            1759723200,
            328
        ],
        [
            1759809600,
            328
        ],
        [
            1759896000,
            318
        ],
        [
            1759982400,
            328
        ],
        [
            1760068800,
            289
        ],
        [
            1760155200,
            383
        ],
        [
            1760241600,
            383
        ],
        [
            1760328000,
            289
        ],
        [
            1760414400,
            310
        ],
        [
            1760500800,
            310
        ],
        [
            1760587200,
            310
        ],
        [
            1760673600,
            310
        ],
        [
            1760760000,
            384
        ],
        [
            1760846400,
            384
        ],
        [
            1760932800,
            310
        ],
        [
            1761019200,
            310
        ],
        [
            1761105600,
            310
        ],
        [
            1761192000,
            354
        ],
        [
            1761278400,
            354
        ],
        [
            1761364800,
            407
        ],
        [
            1761451200,
            407
        ],
        [
            1761537600,
            354
        ],
        [
            1761624000,
            354
        ],
        [
            1761710400,
            361
        ],
        [
            1761796800,
            362
        ],
        [
            1761883200,
            346
        ],
        [
            1761969600,
            392
        ],
        [
            1762056000,
            407
        ],
        [
            1762146000,
            362
        ],
        [
            1762232400,
            363
        ],
        [
            1762318800,
            363
        ],
        [
            1762405200,
            363
        ],
        [
            1762491600,
            362
        ],
        [
            1762578000,
            408
        ],
        [
            1762664400,
            407
        ],
        [
            1762750800,
            362
        ],
        [
            1762837200,
            362
        ],
        [
            1762923600,
            352
        ],
        [
            1763010000,
            352
        ],
        [
            1763096400,
            352
        ],
        [
            1763182800,
            397
        ],
        [
            1763269200,
            397
        ],
        [
            1763355600,
            352
        ],
        [
            1763442000,
            352
        ],
        [
            1763528400,
            352
        ],
        [
            1763614800,
            352
        ],
        [
            1763701200,
            353
        ],
        [
            1763787600,
            373
        ],
        [
            1763874000,
            373
        ],
        [
            1763960400,
            337
        ],
        [
            1764046800,
            344
        ],
        [
            1764133200,
            342
        ],
        [
            1764219600,
            347
        ],
        [
            1764306000,
            335
        ],
        [
            1764392400,
            336
        ],
        [
            1764478800,
            344
        ],
        [
            1764565200,
            350
        ],
        [
            1764651600,
            349
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
                "id": "JFK",
                "name": "John F. Kennedy International Airport"
            },
            "city": "New York",
            "country": "United States",
            "country_code": "US",
            "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRa1dwH1NZQk4dsbPiyA9Vrq2RX75jXSZ-OkHn7NkLHl-11HercqDXoZ4p2cDxJkH6vca2degawrCzHEQ",
            "thumbnail": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQEaUa9NsdPWGpAUGkTApkZDT_4M6_6V8wTcC0v1b1wJAJX-BuMSiipXbsoznGgcI1xLOc5QiTcR_xovexgjdOz0gqQe0tRQ9h0bUkZ07Q"
            }
        ]
        },
        {
        "departure": [
            {
            "airport": {
                "id": "JFK",
                "name": "John F. Kennedy International Airport"
            },
            "city": "New York",
            "country": "United States",
            "country_code": "US",
            "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRa1dwH1NZQk4dsbPiyA9Vrq2RX75jXSZ-OkHn7NkLHl-11HercqDXoZ4p2cDxJkH6vca2degawrCzHEQ",
            "thumbnail": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQEaUa9NsdPWGpAUGkTApkZDT_4M6_6V8wTcC0v1b1wJAJX-BuMSiipXbsoznGgcI1xLOc5QiTcR_xovexgjdOz0gqQe0tRQ9h0bUkZ07Q"
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