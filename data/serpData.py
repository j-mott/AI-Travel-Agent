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

def serp_hotel_data():
    return json.loads(r'''
    {
        "search_metadata": {
            "id": "6933432727714319a4b8c8fe",
            "status": "Success",
            "json_endpoint": "https://serpapi.com/searches/8af8d3fd98ee3231/6933432727714319a4b8c8fe.json",
            "created_at": "2025-12-05T20:40:07.013Z",
            "processed_at": "2025-12-05T20:40:07.014Z",
            "google_hotels_url": "https://www.google.com/_/TravelFrontendUi/data/batchexecute?rpcids=AtySUc&source-path=/travel/search&hl=en&gl=ca&rt=c&soc-app=162&soc-platform=1&soc-device=1",
            "raw_html_file": "https://serpapi.com/searches/8af8d3fd98ee3231/6933432727714319a4b8c8fe.html",
            "prettify_html_file": "https://serpapi.com/searches/8af8d3fd98ee3231/6933432727714319a4b8c8fe.prettify",
            "total_time_taken": {
            "float": 1.31007719039917
            }
        },
        "search_parameters": {
            "engine": "google_hotels",
            "q": "JFK",
            "gl": "ca",
            "hl": "en",
            "currency": "CAD",
            "check_in_date": "2026-02-05",
            "check_out_date": "2026-02-13",
            "adults": 1,
            "children": 0,
            "sort_by": "13",
            "rating": "7"
        },
        "search_information": {
            "total_results": 13
        },
        "brands": [
            {
            "id": 20,
            "name": "Choice Hotels",
            "children": [
                {
                "id": 63,
                "name": "Ascend"
                },
                {
                "id": 27,
                "name": "Comfort"
                },
                {
                "id": 82,
                "name": "Quality Inn"
                },
                {
                "id": 78,
                "name": "Rodeway Inn"
                }
            ]
            },
            {
            "id": 28,
            "name": "Hilton Honors",
            "children": [
                {
                "id": 115,
                "name": "Hampton by Hilton"
                }
            ]
            },
            {
            "id": 17,
            "name": "IHG Hotels & Resorts",
            "children": [
                {
                "id": 56,
                "name": "Holiday Inn Express"
                }
            ]
            },
            {
            "id": 46,
            "name": "Marriott Bonvoy",
            "children": [
                {
                "id": 58,
                "name": "Fairfield Inn by Marriott"
                }
            ]
            },
            {
            "id": 345,
            "name": "Red Roof Inn",
            "children": [
                {
                "id": 4,
                "name": "Red Roof"
                }
            ]
            },
            {
            "id": 53,
            "name": "Wyndham Hotels & Resorts",
            "children": [
                {
                "id": 30,
                "name": "Baymont"
                }
            ]
            }
        ],
        "properties": [
            {
            "type": "hotel",
            "name": "Inn On The Square, an Ascend Hotel Collection",
            "description": "Warmly furnished rooms in a classic hotel offering a cozy bar, a restaurant & breakfast.",
            "link": "https://innonthesquare.net/",
            "property_token": "ChcI_9nXzP_Y9J8JGgsvZy8xdnA3NG1wYhAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChcI_9nXzP_Y9J8JGgsvZy8xdnA3NG1wYhAB&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.1883558,
                "longitude": -82.1594969
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "11:00 AM",
            "rate_per_night": {
                "lowest": "$194",
                "extracted_lowest": 194,
                "before_taxes_fees": "$175",
                "extracted_before_taxes_fees": 175
            },
            "total_rate": {
                "lowest": "$1,552",
                "extracted_lowest": 1552,
                "before_taxes_fees": "$1,398",
                "extracted_before_taxes_fees": 1398
            },
            "nearby_places": [
                {
                "name": "The Railroad Historical Center",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "6 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 20 min"
                    }
                ]
                },
                {
                "name": "Howard's On Main",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "5 min"
                    }
                ]
                }
            ],
            "hotel_class": "3-star hotel",
            "extracted_hotel_class": 3,
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMYgVr9ok1HS0jWZON4uNg0hkqpY6GcmY9J-upq=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMYgVr9ok1HS0jWZON4uNg0hkqpY6GcmY9J-upq=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPZnKFgyLZG2z_-UfoJBlzmVl8oJPhgcQYrYQIh=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPZnKFgyLZG2z_-UfoJBlzmVl8oJPhgcQYrYQIh=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMmzr09mvr4CBk4TTK6nxBo3YUZGdiBoDgV0N2w=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMmzr09mvr4CBk4TTK6nxBo3YUZGdiBoDgV0N2w=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOf7GDbnXZku7JO8JmUnBC6617geaJW3-U9l3eY=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOf7GDbnXZku7JO8JmUnBC6617geaJW3-U9l3eY=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPdOFPYehVpS6UcpoF1ImcFEbXNHPNNZ4rB_34d=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPdOFPYehVpS6UcpoF1ImcFEbXNHPNNZ4rB_34d=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOKlfCh5I8kjBbE9cJW2zazDv8NXX1w4Ua4-gUj=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOKlfCh5I8kjBbE9cJW2zazDv8NXX1w4Ua4-gUj=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMfk3i7g7UdKuSc9M1S_kx-iOQRrmctQR6QhuvS=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMfk3i7g7UdKuSc9M1S_kx-iOQRrmctQR6QhuvS=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipO26480cQg-k5zclB508YGVRhmPxFJ4JPO9J9Fp=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipO26480cQg-k5zclB508YGVRhmPxFJ4JPO9J9Fp=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMz1KM7wykrHIU3t1XA4Yf-Tyc4UKmNeVGc9JMA=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMz1KM7wykrHIU3t1XA4Yf-Tyc4UKmNeVGc9JMA=s10000"
                }
            ],
            "overall_rating": 4.5,
            "reviews": 772,
            "ratings": [
                {
                "stars": 5,
                "count": 553
                },
                {
                "stars": 4,
                "count": 130
                },
                {
                "stars": 3,
                "count": 44
                },
                {
                "stars": 2,
                "count": 23
                },
                {
                "stars": 1,
                "count": 22
                }
            ],
            "location_rating": 4.1,
            "reviews_breakdown": [
                {
                "name": "Bar",
                "description": "Bar or lounge",
                "total_mentioned": 63,
                "positive": 54,
                "negative": 6,
                "neutral": 3
                },
                {
                "name": "Breakfast",
                "description": "Breakfast",
                "total_mentioned": 130,
                "positive": 114,
                "negative": 11,
                "neutral": 5
                },
                {
                "name": "Dining",
                "description": "Food and Beverage",
                "total_mentioned": 91,
                "positive": 76,
                "negative": 8,
                "neutral": 7
                },
                {
                "name": "Couples",
                "description": "Couple friendly",
                "total_mentioned": 18,
                "positive": 14,
                "negative": 0,
                "neutral": 4
                },
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 220,
                "positive": 196,
                "negative": 18,
                "neutral": 6
                },
                {
                "name": "Restaurant",
                "description": "Restaurant",
                "total_mentioned": 73,
                "positive": 61,
                "negative": 8,
                "neutral": 4
                }
            ],
            "amenities": [
                "Breakfast ($)",
                "Free Wi-Fi",
                "Free parking",
                "Air conditioning",
                "Bar",
                "Restaurant",
                "Room service",
                "Accessible",
                "Kid-friendly",
                "Smoke-free property"
            ]
            },
            {
            "type": "hotel",
            "name": "Baymont by Wyndham Greenwood",
            "description": "Simply styled rooms for up to 5 guests have pillow-top beds & access to pool, gym & meeting space.",
            "link": "http://www.baymontgwd.com/",
            "property_token": "ChkIgbaU-eeEwoftARoML2cvMTI0eXExdzZfEAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChkIgbaU-eeEwoftARoML2cvMTI0eXExdzZfEAE&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.2169198,
                "longitude": -82.16452199999999
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "11:00 AM",
            "rate_per_night": {
                "lowest": "$109",
                "extracted_lowest": 109,
                "before_taxes_fees": "$109",
                "extracted_before_taxes_fees": 109
            },
            "total_rate": {
                "lowest": "$875",
                "extracted_lowest": 875,
                "before_taxes_fees": "$875",
                "extracted_before_taxes_fees": 875
            },
            "nearby_places": [
                {
                "name": "Greenwood Museum",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "7 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 16 min"
                    }
                ]
                },
                {
                "name": "TASTY WINGS & SEAFOOD",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "9 min"
                    }
                ]
                }
            ],
            "hotel_class": "2-star hotel",
            "extracted_hotel_class": 2,
            "images": [
                {
                "thumbnail": "https://lh6.googleusercontent.com/proxy/UtIzTeHjma8LecMd0WnbcOIGEwKQuOjOpeZ-X17zPmeVRSHUiwZKyTmDjCUR_r_sl6YERbreMOyQZ_Euun7BqGf8-aKIVlj4LHellggbn2wzgMlA3VaTws7_gqQaoi7c5CtILRlNRXMipK6WlDOq1D2QfepwJA=s287-w287-h192-n-k-no-v1",
                "original_image": "https://images.trvl-media.com/lodging/1000000/50000/43600/43558/a45640b6_z.jpg"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipND0UlNoAvZrtN8n4uqaac3tuV61ojk5-vf4kRW=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipND0UlNoAvZrtN8n4uqaac3tuV61ojk5-vf4kRW=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMM8jaBGyMSuvuBTwMVCKUmL7LUxDTj_dT5bhsy=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMM8jaBGyMSuvuBTwMVCKUmL7LUxDTj_dT5bhsy=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNhTlopkXgesET5WeJbT_NCkNh8KsHkUSo95D5p=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNhTlopkXgesET5WeJbT_NCkNh8KsHkUSo95D5p=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOOsKk7bFdBFK0Yq9YmBiN-fF1ZFsrOa14fn4s0=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOOsKk7bFdBFK0Yq9YmBiN-fF1ZFsrOa14fn4s0=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOCOOrcVmdYDMZWVQHgN-gggKghZB5Kn2EKd9FN=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOCOOrcVmdYDMZWVQHgN-gggKghZB5Kn2EKd9FN=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOlSY-CXqwK175CQVONS0q3ciG66u51uEMUIO7k=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOlSY-CXqwK175CQVONS0q3ciG66u51uEMUIO7k=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNtJIHtyLjT2SCBWeRaTDw4kDZNPriq2nQdckpL=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNtJIHtyLjT2SCBWeRaTDw4kDZNPriq2nQdckpL=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipM1vXKj_SEH6KURElnANBVe2nRy2oKlc6Rmboq4=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipM1vXKj_SEH6KURElnANBVe2nRy2oKlc6Rmboq4=s10000"
                }
            ],
            "overall_rating": 3.8,
            "reviews": 532,
            "ratings": [
                {
                "stars": 5,
                "count": 235
                },
                {
                "stars": 4,
                "count": 127
                },
                {
                "stars": 3,
                "count": 71
                },
                {
                "stars": 2,
                "count": 29
                },
                {
                "stars": 1,
                "count": 70
                }
            ],
            "location_rating": 3.4,
            "reviews_breakdown": [
                {
                "name": "Breakfast",
                "description": "Breakfast",
                "total_mentioned": 42,
                "positive": 21,
                "negative": 17,
                "neutral": 4
                },
                {
                "name": "Cleanliness",
                "description": "Cleanliness",
                "total_mentioned": 122,
                "positive": 82,
                "negative": 36,
                "neutral": 4
                },
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 142,
                "positive": 88,
                "negative": 43,
                "neutral": 11
                },
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 112,
                "positive": 67,
                "negative": 39,
                "neutral": 6
                },
                {
                "name": "Bathroom",
                "description": "Bathroom and toiletries",
                "total_mentioned": 37,
                "positive": 5,
                "negative": 32,
                "neutral": 0
                },
                {
                "name": "Fitness",
                "description": "Fitness",
                "total_mentioned": 32,
                "positive": 8,
                "negative": 17,
                "neutral": 7
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Air conditioning",
                "Pet-friendly",
                "Fitness center",
                "Restaurant",
                "Golf",
                "Accessible",
                "Business center",
                "Kid-friendly"
            ]
            },
            {
            "type": "hotel",
            "name": "Holiday Inn Express & Suites Greenwood Mall by IHG",
            "description": "Straightforward hotel featuring complimentary breakfast, Wi-Fi & parking, plus an outdoor pool.",
            "link": "https://www.ihg.com/holidayinnexpress/hotels/us/en/greenwood/grdwd/hoteldetail?cm_mmc=GoogleMaps-_-EX-_-US-_-GRDWD",
            "property_token": "ChkIzru--Oej7Z1AGg0vZy8xMWJfMnlwNWRuEAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChkIzru--Oej7Z1AGg0vZy8xMWJfMnlwNWRuEAE&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.212396999999996,
                "longitude": -82.1848897
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "11:00 AM",
            "rate_per_night": {
                "lowest": "$255",
                "extracted_lowest": 255,
                "before_taxes_fees": "$230",
                "extracted_before_taxes_fees": 230
            },
            "total_rate": {
                "lowest": "$2,040",
                "extracted_lowest": 2040,
                "before_taxes_fees": "$1,838",
                "extracted_before_taxes_fees": 1838
            },
            "nearby_places": [
                {
                "name": "Grace Street Park",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "5 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 15 min"
                    }
                ]
                },
                {
                "name": "Olive Branch - Mediterranean & Italian Grill",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "4 min"
                    }
                ]
                }
            ],
            "hotel_class": "2-star hotel",
            "extracted_hotel_class": 2,
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipO0YKtxIUExNd8nxDlFIYFNZPL3HBPXm6Bqww-l=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipO0YKtxIUExNd8nxDlFIYFNZPL3HBPXm6Bqww-l=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNUnccapwVmpUkE64Q22tLeoaEViAU9Jd-G82wd=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNUnccapwVmpUkE64Q22tLeoaEViAU9Jd-G82wd=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMvLb6qEhFNoxjeaD2OnccgvuqKUBWVGxARHPWo=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMvLb6qEhFNoxjeaD2OnccgvuqKUBWVGxARHPWo=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipN_w7hABTDDQpT8st60qrr33KhYGvg_2nrA-3S0=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipN_w7hABTDDQpT8st60qrr33KhYGvg_2nrA-3S0=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOyBQqOXkD1hlO9TQ26QTnyvP8n9PDY8jl-P2mY=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOyBQqOXkD1hlO9TQ26QTnyvP8n9PDY8jl-P2mY=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipN_575Wbeyf7N0NOLIzcauVvltrxQyAuvaWjFx1=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipN_575Wbeyf7N0NOLIzcauVvltrxQyAuvaWjFx1=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNe1iAOyfSikYbfLt5kI8nxDsD0oc-4haXttHBe=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNe1iAOyfSikYbfLt5kI8nxDsD0oc-4haXttHBe=s10000"
                },
                {
                "thumbnail": "https://lh6.googleusercontent.com/proxy/GsDCtAQPBzvT_Ek6VIS7PXUgs5LuKYJUbDJ7m_sB_RYA9KYE26KATaWIsg2xfaBQfjCTXCwDb1HAGzPVEOjXZ2ZKhas4COWpSIyX7zwqytpqORgh7zoOlqJETXyTA5nWWWAMCjMb6yk8c9X2jIEy3e_mAHznUSM=s287-w287-h192-n-k-no-v1",
                "original_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/eb/1f/ed/breakfast-area.jpg?w=1900&h=1400&s=1"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPT4O1qmnZabDv1sYo4zAGvs9h4gbs6VG7XRVHp=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPT4O1qmnZabDv1sYo4zAGvs9h4gbs6VG7XRVHp=s10000"
                }
            ],
            "overall_rating": 4.3,
            "reviews": 504,
            "ratings": [
                {
                "stars": 5,
                "count": 314
                },
                {
                "stars": 4,
                "count": 105
                },
                {
                "stars": 3,
                "count": 35
                },
                {
                "stars": 2,
                "count": 19
                },
                {
                "stars": 1,
                "count": 31
                }
            ],
            "location_rating": 3.5,
            "reviews_breakdown": [
                {
                "name": "Breakfast",
                "description": "Breakfast",
                "total_mentioned": 63,
                "positive": 42,
                "negative": 14,
                "neutral": 7
                },
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 153,
                "positive": 115,
                "negative": 32,
                "neutral": 6
                },
                {
                "name": "Cleanliness",
                "description": "Cleanliness",
                "total_mentioned": 118,
                "positive": 95,
                "negative": 19,
                "neutral": 4
                },
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 132,
                "positive": 109,
                "negative": 19,
                "neutral": 4
                },
                {
                "name": "Bathroom",
                "description": "Bathroom and toiletries",
                "total_mentioned": 39,
                "positive": 11,
                "negative": 25,
                "neutral": 3
                },
                {
                "name": "Restaurant",
                "description": "Restaurant",
                "total_mentioned": 31,
                "positive": 22,
                "negative": 7,
                "neutral": 2
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Air conditioning",
                "Fitness center",
                "Full-service laundry",
                "Accessible",
                "Business center",
                "Kid-friendly",
                "Smoke-free property"
            ]
            },
            {
            "type": "hotel",
            "name": "Hampton Inn Greenwood",
            "description": "Relaxed rooms & suites in a modest hotel offering free hot breakfast, an outdoor pool & a gym.",
            "link": "https://www.hilton.com/en/hotels/grdlrhx-hampton-greenwood/?SEO_id=GMB-AMER-HX-GRDLRHX&y_source=1_MjA4MjU3Mi03MTUtbG9jYXRpb24ud2Vic2l0ZQ%3D%3D",
            "property_token": "ChgI_IT_8aSR-qr6ARoLL2cvMXZwNzRtcDMQAQ",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChgI_IT_8aSR-qr6ARoLL2cvMXZwNzRtcDMQAQ&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.2174337,
                "longitude": -82.1587577
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "11:00 AM",
            "rate_per_night": {
                "lowest": "$225",
                "extracted_lowest": 225,
                "before_taxes_fees": "$203",
                "extracted_before_taxes_fees": 203
            },
            "total_rate": {
                "lowest": "$1,802",
                "extracted_lowest": 1802,
                "before_taxes_fees": "$1,623",
                "extracted_before_taxes_fees": 1623
            },
            "nearby_places": [
                {
                "name": "Grace Street Park",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "4 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 15 min"
                    }
                ]
                },
                {
                "name": "Capri's Italian Greenwood",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "3 min"
                    }
                ]
                }
            ],
            "hotel_class": "3-star hotel",
            "extracted_hotel_class": 3,
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPiyuR8hnZMTGaysdeMhLIdKCEYiLIHKYI359p8=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPiyuR8hnZMTGaysdeMhLIdKCEYiLIHKYI359p8=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOXO8gYnYJj7csJmhlAMPnw2rv74D_7u8LaGQdU=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOXO8gYnYJj7csJmhlAMPnw2rv74D_7u8LaGQdU=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOjDqNRCkuwUMs1bcyZgGY7IAnuviYtRG3BlZxb=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOjDqNRCkuwUMs1bcyZgGY7IAnuviYtRG3BlZxb=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMV1x65osmIB0AbzJjTs1ZV5Zw10imr5rlfmD2x=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMV1x65osmIB0AbzJjTs1ZV5Zw10imr5rlfmD2x=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOF2HdNG8LWeZOvtWTrKRUzU0Yn_Zq5rpbhZ3vh=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOF2HdNG8LWeZOvtWTrKRUzU0Yn_Zq5rpbhZ3vh=s10000"
                },
                {
                "thumbnail": "https://lh6.googleusercontent.com/proxy/1lAf4SMzqa8fJWWik6-9CxpdZmFCRLP9qZNOBcLKzUKnoWUIEsTCBib-hiZoSF3LD8chI41TsRD3ArjkCKU4f9G0AfgNGrOXd2fL0IKhYt-qeA-2-Uk35ePpGiMF7dObrrLBdrwQ1RVGu7CZwogGVKlP9avPRzg=s287-w287-h192-n-k-no-v1",
                "original_image": "https://photos.hotelbeds.com/giata/original/16/163690/163690a_hb_a_002.jpg"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipM7rZrpUzY647kQuv5XPd72VnZYbwXOrCtPOveN=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipM7rZrpUzY647kQuv5XPd72VnZYbwXOrCtPOveN=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPn6v4nka0runUgwa0938wTuBOPja_ClHhHdtCN=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPn6v4nka0runUgwa0938wTuBOPja_ClHhHdtCN=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPqZIpCMSr-5Lmjj_AHi8V95D4nyzVR1OCzBywC=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPqZIpCMSr-5Lmjj_AHi8V95D4nyzVR1OCzBywC=s10000"
                }
            ],
            "overall_rating": 4.1,
            "reviews": 502,
            "ratings": [
                {
                "stars": 5,
                "count": 262
                },
                {
                "stars": 4,
                "count": 137
                },
                {
                "stars": 3,
                "count": 46
                },
                {
                "stars": 2,
                "count": 24
                },
                {
                "stars": 1,
                "count": 33
                }
            ],
            "location_rating": 3.7,
            "reviews_breakdown": [
                {
                "name": "Breakfast",
                "description": "Breakfast",
                "total_mentioned": 50,
                "positive": 34,
                "negative": 12,
                "neutral": 4
                },
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 146,
                "positive": 116,
                "negative": 27,
                "neutral": 3
                },
                {
                "name": "Cleanliness",
                "description": "Cleanliness",
                "total_mentioned": 111,
                "positive": 85,
                "negative": 22,
                "neutral": 4
                },
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 124,
                "positive": 97,
                "negative": 18,
                "neutral": 9
                },
                {
                "name": "Restaurant",
                "description": "Restaurant",
                "total_mentioned": 28,
                "positive": 19,
                "negative": 7,
                "neutral": 2
                },
                {
                "name": "Accessibility",
                "description": "Accessibility",
                "total_mentioned": 10,
                "positive": 3,
                "negative": 6,
                "neutral": 1
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Air conditioning",
                "Pet-friendly",
                "Fitness center",
                "Accessible",
                "Business center",
                "Kid-friendly",
                "Smoke-free property"
            ],
            "eco_certified": true
            },
            {
            "type": "hotel",
            "name": "Comfort Inn & Suites Greenwood near University",
            "description": "Contemporary lodging with a fitness center & outdoor pool, plus free hot breakfast & WiFi.",
            "link": "https://www.choicehotels.com/south-carolina/greenwood/comfort-inn-hotels/sc541?mc=llgoxxpx",
            "property_token": "ChcIxZL0x4q-q4Y2GgsvZy8xdGQ2MWw0YxAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChcIxZL0x4q-q4Y2GgsvZy8xdGQ2MWw0YxAB&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.2096527,
                "longitude": -82.1746497
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "11:00 AM",
            "rate_per_night": {
                "lowest": "$200",
                "extracted_lowest": 200,
                "before_taxes_fees": "$180",
                "extracted_before_taxes_fees": 180
            },
            "total_rate": {
                "lowest": "$1,599",
                "extracted_lowest": 1599,
                "before_taxes_fees": "$1,441",
                "extracted_before_taxes_fees": 1441
            },
            "nearby_places": [
                {
                "name": "Greenwood Museum",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "4 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 16 min"
                    }
                ]
                },
                {
                "name": "Olive Branch - Mediterranean & Italian Grill",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "1 min"
                    }
                ]
                }
            ],
            "hotel_class": "2-star hotel",
            "extracted_hotel_class": 2,
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOC90oLVPObs-RJnk7a0S1_MSnD3FOL3PPAzlTJ=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOC90oLVPObs-RJnk7a0S1_MSnD3FOL3PPAzlTJ=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMQtclE2MDpoIRhtJwAHjP6-e1vNc6RO93sqSUB=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMQtclE2MDpoIRhtJwAHjP6-e1vNc6RO93sqSUB=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPVAfMBEBRaZkfrR0aNwVXG7GPaxAk3_mdLj9u0=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPVAfMBEBRaZkfrR0aNwVXG7GPaxAk3_mdLj9u0=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipObXx7J_W4r_KVA1LlPbnlAQ3x4TqkwV-4lMpom=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipObXx7J_W4r_KVA1LlPbnlAQ3x4TqkwV-4lMpom=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOb6rFcRpAEOAcUzhZ_FF9BfkBEnlSG2LukTtqG=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOb6rFcRpAEOAcUzhZ_FF9BfkBEnlSG2LukTtqG=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNKziWTyiuGZJVFn1HeNWyYV79zm8kgjies-Kq9=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNKziWTyiuGZJVFn1HeNWyYV79zm8kgjies-Kq9=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNGn7iylZ1qFEUVkjoHtjnF-aKudcMsYcYaOK2p=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNGn7iylZ1qFEUVkjoHtjnF-aKudcMsYcYaOK2p=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipORSXCuvnmYJPUexm3I2Xi4UgPC2AVNEXxeY6zQ=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipORSXCuvnmYJPUexm3I2Xi4UgPC2AVNEXxeY6zQ=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNnQWRLRqFRUPNjbyrTPRF8bWbcsi0gwrfHWqVz=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNnQWRLRqFRUPNjbyrTPRF8bWbcsi0gwrfHWqVz=s10000"
                }
            ],
            "overall_rating": 3.7,
            "reviews": 435,
            "ratings": [
                {
                "stars": 5,
                "count": 191
                },
                {
                "stars": 4,
                "count": 110
                },
                {
                "stars": 3,
                "count": 37
                },
                {
                "stars": 2,
                "count": 25
                },
                {
                "stars": 1,
                "count": 72
                }
            ],
            "location_rating": 4,
            "reviews_breakdown": [
                {
                "name": "Breakfast",
                "description": "Breakfast",
                "total_mentioned": 33,
                "positive": 22,
                "negative": 7,
                "neutral": 4
                },
                {
                "name": "Atmosphere",
                "description": "Atmosphere",
                "total_mentioned": 13,
                "positive": 12,
                "negative": 0,
                "neutral": 1
                },
                {
                "name": "Location",
                "description": "Location",
                "total_mentioned": 21,
                "positive": 15,
                "negative": 5,
                "neutral": 1
                },
                {
                "name": "Room",
                "description": "Room amenities",
                "total_mentioned": 23,
                "positive": 6,
                "negative": 16,
                "neutral": 1
                },
                {
                "name": "Bathroom",
                "description": "Bathroom and toiletries",
                "total_mentioned": 43,
                "positive": 8,
                "negative": 31,
                "neutral": 4
                },
                {
                "name": "Sleep",
                "description": "Sleep",
                "total_mentioned": 61,
                "positive": 13,
                "negative": 43,
                "neutral": 5
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Pools",
                "Hot tub",
                "Fitness center",
                "Restaurant",
                "Kitchen",
                "Golf",
                "Accessible",
                "Business center",
                "Kid-friendly",
                "Smoke-free property"
            ]
            },
            {
            "type": "hotel",
            "name": "Red Roof Inn & Suites Greenwood, SC",
            "description": "Warm rooms & suites in a relaxed budget hotel offering complimentary breakfast, Wi-Fi & parking.",
            "link": "https://www.redroof.com/property/sc/greenwood/RRI469?utm_source=GMB&utm_medium=Google&utm_campaign=GMB_Performance_RRI469",
            "property_token": "ChkIy-nXkdeDi40sGg0vZy8xMWNtYm5tOTd4EAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChkIy-nXkdeDi40sGg0vZy8xMWNtYm5tOTd4EAE&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.2088088,
                "longitude": -82.1774597
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "11:00 AM",
            "rate_per_night": {
                "lowest": "$115",
                "extracted_lowest": 115,
                "before_taxes_fees": "$115",
                "extracted_before_taxes_fees": 115
            },
            "total_rate": {
                "lowest": "$922",
                "extracted_lowest": 922,
                "before_taxes_fees": "$922",
                "extracted_before_taxes_fees": 922
            },
            "nearby_places": [
                {
                "name": "Greenwood Museum",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "4 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 17 min"
                    }
                ]
                },
                {
                "name": "Olive Branch - Mediterranean & Italian Grill",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "4 min"
                    }
                ]
                }
            ],
            "hotel_class": "2-star hotel",
            "extracted_hotel_class": 2,
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPJArzZU-gwmT7G0AyldWsZhlTI3TyC3yBBwPV-=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPJArzZU-gwmT7G0AyldWsZhlTI3TyC3yBBwPV-=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNNK537ZG4b07cgQy_V4ciLxeIaAQjjpUGP7Q1r=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNNK537ZG4b07cgQy_V4ciLxeIaAQjjpUGP7Q1r=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMsNLDQMmI0rNpp6QNGTFb9d4TsOjv_OWL115Go=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMsNLDQMmI0rNpp6QNGTFb9d4TsOjv_OWL115Go=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOV_G0cjkNIpbWb3ItRDJfW8jxjo0vVnNNS6Ry6=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOV_G0cjkNIpbWb3ItRDJfW8jxjo0vVnNNS6Ry6=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSzzWk6quIu9T0shL-BPRnkRnCZa_mqXtyiOYGhJtZu2YXfhxlE0h0xoI7eKua6EAQnA4XZa9LxXHFQ_oYqttlOzOFdM66tFfxR-Atht5tOZBjKghxL09OxxwPvYniYzA7QXzRF_=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgIDfv9qD9gE=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMDwZY8-20CEtEaEqCPMEn27rvoujaEZNzrqKvz=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMDwZY8-20CEtEaEqCPMEn27rvoujaEZNzrqKvz=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPrky9yV5iWDaVRbNsPXlAnFCIcik9hqGqdY_zw=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPrky9yV5iWDaVRbNsPXlAnFCIcik9hqGqdY_zw=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNB7nUR-p7bx2Wq4b0nUdGalG95OZFd09TeQrON=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNB7nUR-p7bx2Wq4b0nUdGalG95OZFd09TeQrON=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMCcKqaYXPwKVO98v0GLD3o_Ew-BX5GwXcj92kS=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMCcKqaYXPwKVO98v0GLD3o_Ew-BX5GwXcj92kS=s10000"
                }
            ],
            "overall_rating": 3.5,
            "reviews": 427,
            "ratings": [
                {
                "stars": 5,
                "count": 184
                },
                {
                "stars": 4,
                "count": 69
                },
                {
                "stars": 3,
                "count": 44
                },
                {
                "stars": 2,
                "count": 46
                },
                {
                "stars": 1,
                "count": 84
                }
            ],
            "location_rating": 3.9,
            "reviews_breakdown": [
                {
                "name": "Cleanliness",
                "description": "Cleanliness",
                "total_mentioned": 118,
                "positive": 61,
                "negative": 54,
                "neutral": 3
                },
                {
                "name": "Wi-Fi",
                "description": "Wi-Fi",
                "total_mentioned": 6,
                "positive": 4,
                "negative": 2,
                "neutral": 0
                },
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 113,
                "positive": 74,
                "negative": 31,
                "neutral": 8
                },
                {
                "name": "Bathroom",
                "description": "Bathroom and toiletries",
                "total_mentioned": 46,
                "positive": 5,
                "negative": 39,
                "neutral": 2
                },
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 118,
                "positive": 70,
                "negative": 44,
                "neutral": 4
                },
                {
                "name": "Pets",
                "description": "Pets",
                "total_mentioned": 11,
                "positive": 7,
                "negative": 3,
                "neutral": 1
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Air conditioning",
                "Pet-friendly",
                "Fitness center",
                "Accessible",
                "Business center",
                "Kid-friendly"
            ]
            },
            {
            "type": "hotel",
            "name": "Fairfield by Marriott Inn & Suites Greenwood",
            "description": "Relaxed quarters in a straightforward property offering an indoor pool, plus free breakfast & Wi-Fi.",
            "link": "https://www.marriott.com/en-us/hotels/grdfi-fairfield-inn-and-suites-greenwood/overview/?scid=f2ae0541-1279-4f24-b197-a979c79310b0",
            "property_token": "ChgI_Na4l8q2hJfIARoLL2cvMXZsNWhtczIQAQ",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChgI_Na4l8q2hJfIARoLL2cvMXZsNWhtczIQAQ&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.2028051,
                "longitude": -82.193377
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "12:00 PM",
            "rate_per_night": {
                "lowest": "$271",
                "extracted_lowest": 271,
                "before_taxes_fees": "$244",
                "extracted_before_taxes_fees": 244
            },
            "total_rate": {
                "lowest": "$2,169",
                "extracted_lowest": 2169,
                "before_taxes_fees": "$1,955",
                "extracted_before_taxes_fees": 1955
            },
            "nearby_places": [
                {
                "name": "Greenwood Museum",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "8 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 18 min"
                    }
                ]
                },
                {
                "name": "Fusion Japanese & Thai",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "5 min"
                    }
                ]
                }
            ],
            "hotel_class": "3-star hotel",
            "extracted_hotel_class": 3,
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipM7OVd6D12HmtLLNKBOUGsEmJ7f43F6b5d6eI0=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipM7OVd6D12HmtLLNKBOUGsEmJ7f43F6b5d6eI0=s10000"
                },
                {
                "thumbnail": "https://lh5.googleusercontent.com/proxy/QlI_3IxLq9TQ5x7cyPEckOIp43LglTMF5tRmnKXcbLbcscKAcJBpXjsvpV_5vIxLuv6aNqnNeDSY1Oy0_OTbsDIbBU5ZadogcDFvjSo7aJXmeG1_a_-3BHEguf3ZLumpaG1c9ZO_wzzGbZSqZKS6GTGOURaVlQ=s287-w287-h192-n-k-no-v1",
                "original_image": "https://photos.hotelbeds.com/giata/original/71/712299/712299a_hb_a_006.jpg"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipO1gVWbbzaD8XOZzqR0VUWmQ_QXypR85GHu4j8=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipO1gVWbbzaD8XOZzqR0VUWmQ_QXypR85GHu4j8=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPbbfMKeOYTpwdX-qSLeqhplDnNSlkdw2yQWig=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPbbfMKeOYTpwdX-qSLeqhplDnNSlkdw2yQWig=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNv-qaRCi1uS0NBUEUDaOReJugwha41ExQ7eEM=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNv-qaRCi1uS0NBUEUDaOReJugwha41ExQ7eEM=s10000"
                },
                {
                "thumbnail": "https://lh6.googleusercontent.com/proxy/QwrhZ1s4tlX1vTrIFohAhqRnm40jqF4fkb2giSfYO-Ufbirzj1WS4QgB0UgkZtYhdBlT8-EhThC8DYibIqfY2WqU3DPAVnid_xBS60DgdGOyJTxu-AiYJPTdSbrMlnNHZSU_h2gp0xeJ9DI5N69clhX2RGXY5Q=s287-w287-h192-n-k-no-v1",
                "original_image": "https://photos.hotelbeds.com/giata/original/71/712299/712299a_hb_r_003.jpg"
                },
                {
                "thumbnail": "https://lh4.googleusercontent.com/proxy/EYA1gOty7Hz4B1q7yEA_lgfTa3DzejbaR0L9qlg5TyGCBxlhvTAR2Qc_glJSxs8OpC0EuDrPs0_9rm1qR-D04UTHaZDI0u--AzO86Jt6TK23R8CbbxNSaLSDmMh3w5DCi_lrQWS6ZmjfCbLdngXkRrSWYZlFd4c=s287-w287-h192-n-k-no-v1",
                "original_image": "https://photos.hotelbeds.com/giata/original/71/712299/712299a_hb_f_007.jpg"
                },
                {
                "thumbnail": "https://lh6.googleusercontent.com/proxy/aD7_w_gFmMYimmkn-oAgXInNXJyCZwKNOX87byx9LOvExyIaHMwuBk7l6J3g062XdWEM43D8jV5J3y2kOeh3VvpvZPzWuXx6dRGnTGPr2KGCNIxH-5m6pEdiL7KfxSh6DGSbwJU6wyOgtfM6tufIbiqDB_dvJvc=s287-w287-h192-n-k-no-v1",
                "original_image": "https://photos.hotelbeds.com/giata/original/71/712299/712299a_hb_f_001.jpg"
                },
                {
                "thumbnail": "https://lh4.googleusercontent.com/proxy/V8E6TUBUFyG2xberQZ4HzAiTsI_kAa6gmPMs8vCG_48Ujp2hWzhfNeQ6EHJKT_GULZws7LgIcAcvyLrIwOHytyPMr_zC39bjpDASOpZrkBpM8xR04i3sCTDc2lg2NdlLXM2DfGI_57IHbigmT-ETLquQi6C7lqA=s287-w287-h192-n-k-no-v1",
                "original_image": "https://d2hyz2bfif3cr8.cloudfront.net/imageRepo/1/0/172/30/307/fi-grdfi-outdoor-space28835-59200_Classic-Hor_O.jpg"
                }
            ],
            "overall_rating": 4.1,
            "reviews": 350,
            "ratings": [
                {
                "stars": 5,
                "count": 176
                },
                {
                "stars": 4,
                "count": 100
                },
                {
                "stars": 3,
                "count": 35
                },
                {
                "stars": 2,
                "count": 10
                },
                {
                "stars": 1,
                "count": 29
                }
            ],
            "location_rating": 3.7,
            "reviews_breakdown": [
                {
                "name": "Hot Tub",
                "description": "Hot tub",
                "total_mentioned": 9,
                "positive": 3,
                "negative": 4,
                "neutral": 2
                },
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 99,
                "positive": 70,
                "negative": 21,
                "neutral": 8
                },
                {
                "name": "Breakfast",
                "description": "Breakfast",
                "total_mentioned": 33,
                "positive": 20,
                "negative": 10,
                "neutral": 3
                },
                {
                "name": "Bathroom",
                "description": "Bathroom and toiletries",
                "total_mentioned": 36,
                "positive": 11,
                "negative": 20,
                "neutral": 5
                },
                {
                "name": "Cleanliness",
                "description": "Cleanliness",
                "total_mentioned": 77,
                "positive": 61,
                "negative": 15,
                "neutral": 1
                },
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 95,
                "positive": 75,
                "negative": 16,
                "neutral": 4
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Indoor pool",
                "Air conditioning",
                "Fitness center",
                "Accessible",
                "Business center",
                "Kid-friendly",
                "Smoke-free property"
            ]
            },
            {
            "type": "hotel",
            "name": "Rodeway Inn Greenwood",
            "link": "https://www.choicehotels.com/south-carolina/greenwood/rodeway-inn-hotels/sc098?mc=llgoxxpx",
            "property_token": "ChoImtGp8bLk6aenARoNL2cvMTFyc2c3ejQ5cBAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChoImtGp8bLk6aenARoNL2cvMTFyc2c3ejQ5cBAB&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.209864,
                "longitude": -82.1503072
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "11:00 AM",
            "rate_per_night": {
                "lowest": "$105",
                "extracted_lowest": 105,
                "before_taxes_fees": "$95",
                "extracted_before_taxes_fees": 95
            },
            "total_rate": {
                "lowest": "$844",
                "extracted_lowest": 844,
                "before_taxes_fees": "$760",
                "extracted_before_taxes_fees": 760
            },
            "nearby_places": [
                {
                "name": "Greenwood Museum",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "6 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 18 min"
                    }
                ]
                },
                {
                "name": "Lovo's bar and grill ll mexican restaurant",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "2 min"
                    }
                ]
                }
            ],
            "images": [
                {
                "thumbnail": "https://lh4.googleusercontent.com/proxy/T5bl6XK_rHzIMBwKkB_UYBjraLZajVW0ekep6EWXBBHVgxGgkxt6ch8H5JNjDtoHGJ2D2ALoua7PtAZZVT5k5I1WrnWl1FH65YE5V7MuoiQ9linkIelu6cCcK8Jd0otZHL203lBxi9-ftzFeae77fB1zdy77-w=s287-w287-h192-n-k-no-v1",
                "original_image": "https://photos.hotelbeds.com/giata/original/92/921783/921783a_hb_w_004.jpg?20250123122949?20250505203209"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipN3ZMWcEE_eH6qXuZx-jSzzzT9aUHfq9DcY39qS=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipN3ZMWcEE_eH6qXuZx-jSzzzT9aUHfq9DcY39qS=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNkGDIqS8KaadipQz60M83rWHjClIB9bjl6OzO5=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNkGDIqS8KaadipQz60M83rWHjClIB9bjl6OzO5=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMM0RB9yD5bL7ouenC_yQAiaQKQWjaVqHtel5Vc=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMM0RB9yD5bL7ouenC_yQAiaQKQWjaVqHtel5Vc=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPYLoslHePTUwgynqQ1YfqOpSHXhCFr7FVcAKGj=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPYLoslHePTUwgynqQ1YfqOpSHXhCFr7FVcAKGj=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/proxy/Pq7tvrFhJIG9yjpYKIWV9ILpYf47ObZMcyFNX0VGSezCOEkVnATtCA6nakGwGHCJ3Ug9tc3TUzHSjKMhKeK6NHn7IDY9Ha5VlGnpFWHZqvpNHjsOBALmLfe_LkQ8DIXsWLtEvv6yESWViZt9KBU3YK5erNXWz48=s287-w287-h192-n-k-no-v1",
                "original_image": "https://photos.hotelbeds.com/giata/original/92/921783/921783a_hb_l_002.JPG?20250123122948?20250505203210"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMviXjzHgNWTbXyiCGTMRgmHxDy8KCnvkYyzVDZ=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMviXjzHgNWTbXyiCGTMRgmHxDy8KCnvkYyzVDZ=s10000"
                },
                {
                "thumbnail": "https://lh5.googleusercontent.com/proxy/UxzqFuvd6yuEVwMjVyv5WO_jpGqglV_A9K57Th-hobZm82m5Og-8PEJSP1K9OZVTht08pFm438yqvFrJwkQEn7omozVRHoVH7E-k4wvQ4yDYmeV-bKu6cr9UvMAdSdF4vWJwYCAF-wJJRSV2GMmGjpvp9jMDaQ=s287-w287-h192-n-k-no-v1",
                "original_image": "https://photos.hotelbeds.com/giata/original/92/921783/921783a_hb_w_001.jpg?20250123122948?20250505203210"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipO9mN9GKcHDzrLYw0yVEGz2M5szVsds6ApT1jil=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipO9mN9GKcHDzrLYw0yVEGz2M5szVsds6ApT1jil=s10000"
                }
            ],
            "overall_rating": 4,
            "reviews": 130,
            "ratings": [
                {
                "stars": 5,
                "count": 70
                },
                {
                "stars": 4,
                "count": 25
                },
                {
                "stars": 3,
                "count": 11
                },
                {
                "stars": 2,
                "count": 13
                },
                {
                "stars": 1,
                "count": 11
                }
            ],
            "location_rating": 3.4,
            "reviews_breakdown": [
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 51,
                "positive": 45,
                "negative": 3,
                "neutral": 3
                },
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 47,
                "positive": 39,
                "negative": 5,
                "neutral": 3
                },
                {
                "name": "Cleanliness",
                "description": "Cleanliness",
                "total_mentioned": 34,
                "positive": 25,
                "negative": 7,
                "neutral": 2
                },
                {
                "name": "Safety",
                "description": "Safety",
                "total_mentioned": 5,
                "positive": 3,
                "negative": 2,
                "neutral": 0
                },
                {
                "name": "Bathroom",
                "description": "Bathroom and toiletries",
                "total_mentioned": 8,
                "positive": 3,
                "negative": 3,
                "neutral": 2
                },
                {
                "name": "Sleep",
                "description": "Sleep",
                "total_mentioned": 18,
                "positive": 13,
                "negative": 2,
                "neutral": 3
                }
            ],
            "amenities": [
                "Free breakfast",
                "Free Wi-Fi",
                "Free parking",
                "Air conditioning",
                "Pet-friendly",
                "Golf",
                "Accessible",
                "Business center",
                "Kid-friendly"
            ]
            },
            {
            "type": "hotel",
            "name": "Lake Greenwood Motorcoach Resort",
            "description": "Casual lakeside motorcoach getaway offering a heated outdoor pool & a clubhouse with a fireplace.",
            "link": "http://lakegreenwoodmotorcoachresort.com/",
            "property_token": "ChcI7NuTr97Z1PpcGgsvZy8xdGNfcnFxbBAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChcI7NuTr97Z1PpcGgsvZy8xdGNfcnFxbBAB&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.2575838,
                "longitude": -82.01096249999999
            },
            "nearby_places": [
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 13 min"
                    }
                ]
                },
                {
                "name": "Port Grill"
                }
            ],
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipORmTF6SrLB_FVWakYVKbfe7SAhOr6dSLmAKkv4=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipORmTF6SrLB_FVWakYVKbfe7SAhOr6dSLmAKkv4=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMoeofQpcLvzEPOSa7HZDgEnYW5Ll8SYN_JUjXT=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMoeofQpcLvzEPOSa7HZDgEnYW5Ll8SYN_JUjXT=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipN8mfBcLPOeelTCx_8VqUUAHCrRTxr6qr1rCju6=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipN8mfBcLPOeelTCx_8VqUUAHCrRTxr6qr1rCju6=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSxCcCgpFL2jnRd3UIjnVRt2DtdPIm4XCpXpekaj8Y1RugN1DRqJWc0AKF-vfxw13TkPxAyrXeV3yMH18uXCKuBx8zrASSu2ehNyUTs3zmSvmWuTdpKib9IfLkGsRfySRb2xaSHa4A=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgID__NHMoAE=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMe9QsbpkYZUiAb5lpRq3tIvnhxhyDPRtYzf2ED=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMe9QsbpkYZUiAb5lpRq3tIvnhxhyDPRtYzf2ED=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPduXFYBIvcsKDGFKt1I11h-yLPo4Lc9BISWciG=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPduXFYBIvcsKDGFKt1I11h-yLPo4Lc9BISWciG=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOG83lRlATdXcwhpltsotuae6eRzfF83urq986b=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOG83lRlATdXcwhpltsotuae6eRzfF83urq986b=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMJJrMc34Ad1l-Bw_n_ErvQeWnKyOSFIfOF_S3C=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMJJrMc34Ad1l-Bw_n_ErvQeWnKyOSFIfOF_S3C=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOBdl1ZH24nnpZWAGN5rhxVBFWhKf4yhphGXCOc=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOBdl1ZH24nnpZWAGN5rhxVBFWhKf4yhphGXCOc=s10000"
                }
            ],
            "overall_rating": 4.5,
            "reviews": 96,
            "ratings": [
                {
                "stars": 5,
                "count": 75
                },
                {
                "stars": 4,
                "count": 9
                },
                {
                "stars": 3,
                "count": 5
                },
                {
                "stars": 2,
                "count": 1
                },
                {
                "stars": 1,
                "count": 6
                }
            ],
            "location_rating": 3,
            "reviews_breakdown": [
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 23,
                "positive": 20,
                "negative": 3,
                "neutral": 0
                },
                {
                "name": "Nature",
                "description": "Nature and outdoor activities",
                "total_mentioned": 10,
                "positive": 8,
                "negative": 2,
                "neutral": 0
                }
            ],
            "amenities": [
                "Free Wi-Fi",
                "Free parking",
                "Outdoor pool",
                "Golf"
            ]
            },
            {
            "type": "hotel",
            "name": "Lakeside Cabins and Motel",
            "link": "https://m.facebook.com/lakesidegreenwood/",
            "property_token": "ChoI79ii68CH4NnVARoNL2cvMTFjbjVxbXAzbhAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChoI79ii68CH4NnVARoNL2cvMTFjbjVxbXAzbhAB&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.284654599999996,
                "longitude": -82.0571643
            },
            "check_in_time": "3:00 PM",
            "nearby_places": [
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 7 min"
                    }
                ]
                },
                {
                "name": "Lake Greenwood Bait & Tackle",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "2 min"
                    }
                ]
                }
            ],
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOPHjZ9yoFk6dlzd0E-YIsmyTWNyJbjxEyOZlfs=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOPHjZ9yoFk6dlzd0E-YIsmyTWNyJbjxEyOZlfs=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMPOw1_vltE8jJXUPzflYLjLMBWMwMwfhoL7A9N=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMPOw1_vltE8jJXUPzflYLjLMBWMwMwfhoL7A9N=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPM4SzhBjeqXLuf730fQ-NBHuzRa9eJ3E1ToSQF=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPM4SzhBjeqXLuf730fQ-NBHuzRa9eJ3E1ToSQF=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSwvR2cw4EAB6xy7fr5gjvJt4VnlaxCpq47JbsBJTb1RGDz61Y5Tfa1ADxAiRplEfrKongg3iBWyzNeQ5kCoBA0CUOEkX7EIjalwlaWh47q2GrqRq7e0dMpucUygFPhBwjJNcfF-pw=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgIDJxL-jgwE=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSxFHOIXlBL8nkZHqRPbojfEokpx_pvmKQVuQKG7XxSwGG4R5Q8dftVsECXFQTsOJ0VOp2l2e4grCrmWlVx7pGVuVMBTKEgOnpjthH2Ayb790Hia5SpF5vnyPzI_T6zswTz6lvU7=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgIDE2eu2DA=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSy2Htu1i6RVEgfZjrYgD8H_bTiC3OvafWhcU0HXNu2O6t4YNRETVoNPbAabp61Blb8xHlJg2t7mqH-7yQYnLCKjK6KFMjpyrxqxzZlhun1r-xPq_cvzqQyikveJ33DJuISx5xcG=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgIDsmISIAg=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSy86ev4RRq0w3HiAJ4t9h6V3M3urNvaW0MYMYIiPOiEYEKfJ0_mC5UNZNWhY7atk-9lx9hOV9ATIGzutxAohntsTNK4eDploNHKkHJitc4i_BayaL75mLbdmBA7X0jhAcS_HGSC=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgICWnMLFdw=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipP5z-wdJ-7KjLEpAferE_7FP8gDjLE_Kj0J2iye=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipP5z-wdJ-7KjLEpAferE_7FP8gDjLE_Kj0J2iye=s10000"
                },
                {
                "thumbnail": "https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=jUDr845R8j-zlUSUo2XvdA&cb_client=search.estubs.gps&w=287&h=192&yaw=292.91916&pitch=0&thumbfov=100&scale=2",
                "original_image": "https://lh5.googleusercontent.com/p/jUDr845R8j-zlUSUo2XvdA=s10000"
                }
            ],
            "overall_rating": 3.7,
            "reviews": 77,
            "ratings": [
                {
                "stars": 5,
                "count": 36
                },
                {
                "stars": 4,
                "count": 15
                },
                {
                "stars": 3,
                "count": 10
                },
                {
                "stars": 2,
                "count": 1
                },
                {
                "stars": 1,
                "count": 15
                }
            ],
            "location_rating": 2.6,
            "reviews_breakdown": [
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 18,
                "positive": 14,
                "negative": 4,
                "neutral": 0
                },
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 16,
                "positive": 11,
                "negative": 4,
                "neutral": 1
                },
                {
                "name": "Cleanliness",
                "description": "Cleanliness",
                "total_mentioned": 13,
                "positive": 5,
                "negative": 8,
                "neutral": 0
                }
            ],
            "amenities": [
                "Free Wi-Fi",
                "Free parking"
            ]
            },
            {
            "type": "hotel",
            "name": "Liberty Springs RV Park",
            "link": "https://libertyspringsrvpark.com/",
            "property_token": "ChoI5viT2I6ko_2lARoNL2cvMTFmbmd2Y3MwcBAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChoI5viT2I6ko_2lARoNL2cvMTFmbmd2Y3MwcBAB&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.3132982,
                "longitude": -81.9925506
            },
            "nearby_places": [
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 4 min"
                    }
                ]
                },
                {
                "name": "Mayberry Diner",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "4 min"
                    }
                ]
                }
            ],
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOu8-GyeSP6uOOay--Ek4Jz2pPTS5j9gaiOwdec=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOu8-GyeSP6uOOay--Ek4Jz2pPTS5j9gaiOwdec=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMdpsR14zxhWwRlfkcqcxdsGlJVkoGFzvQBC1Rl=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMdpsR14zxhWwRlfkcqcxdsGlJVkoGFzvQBC1Rl=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipO2wOZCckeWHPL13_CS5lDAxrwhiCowRaoruTbC=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipO2wOZCckeWHPL13_CS5lDAxrwhiCowRaoruTbC=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMJXReUDfW0rMNV1ahgPsqyh9vzkcszpXzhlSFE=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMJXReUDfW0rMNV1ahgPsqyh9vzkcszpXzhlSFE=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipPB5weybV-p0suweSMCqxv_mxuww-KhxJVH67UN=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipPB5weybV-p0suweSMCqxv_mxuww-KhxJVH67UN=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMCPma6wIq9F2OwFVOrebxVtSwJ4M2mIM-ihCLo=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMCPma6wIq9F2OwFVOrebxVtSwJ4M2mIM-ihCLo=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOue34o9oMTGZL8StFBmwRlnQt2SRakJ93cyVWQ=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOue34o9oMTGZL8StFBmwRlnQt2SRakJ93cyVWQ=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSxwq2Zwfe0H-gBFefMwynKDCUv78kbzsUmMOKXC500-xiHvBcRezE2wrIpbTmULFSim1LhfXb6Pe-TllYhQUf5ajnALQl--WgigYxWZWNqbzK2NF8SZUAQELfqv_uSmteLkZMc=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgICMsp7Hbg=s10000"
                },
                {
                "thumbnail": "https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=ej9IRLsyZT2gEwFbPxD-NQ&cb_client=search.estubs.gps&w=287&h=192&yaw=197.01793&pitch=0&thumbfov=100&scale=2",
                "original_image": "https://lh5.googleusercontent.com/p/ej9IRLsyZT2gEwFbPxD-NQ=s10000"
                }
            ],
            "overall_rating": 4.6,
            "reviews": 33,
            "ratings": [
                {
                "stars": 5,
                "count": 26
                },
                {
                "stars": 4,
                "count": 4
                },
                {
                "stars": 3,
                "count": 2
                },
                {
                "stars": 2,
                "count": 0
                },
                {
                "stars": 1,
                "count": 1
                }
            ],
            "location_rating": 2.5,
            "reviews_breakdown": [
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 18,
                "positive": 18,
                "negative": 0,
                "neutral": 0
                }
            ]
            },
            {
            "type": "hotel",
            "name": "All Seasons Family Campground",
            "link": "http://www.allseasonsfamilycamp.com/",
            "property_token": "ChcIsdvmr-_mqYAqGgsvZy8xdHg0N3J6cxAB",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChcIsdvmr-_mqYAqGgsvZy8xdHg0N3J6cxAB&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.2677488,
                "longitude": -81.9809274
            },
            "nearby_places": [
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 10 min"
                    }
                ]
                },
                {
                "name": "Mayberry Diner",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "6 min"
                    }
                ]
                }
            ],
            "images": [
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMmxUSVAwEGEp7cOa3RMoQzloVv0zadCKoTNdBe=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMmxUSVAwEGEp7cOa3RMoQzloVv0zadCKoTNdBe=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMAy4lXNYoc8SzL99TAUyH5iRXkna_LaH_zn1B8=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMAy4lXNYoc8SzL99TAUyH5iRXkna_LaH_zn1B8=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipM9I2tz2f6dck_cSScr4ALq9mFGmWziTb1J8Bq0=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipM9I2tz2f6dck_cSScr4ALq9mFGmWziTb1J8Bq0=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipODP29G9rNHGnRTtpeDu0wT9sK0J7QNplR3M2op=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipODP29G9rNHGnRTtpeDu0wT9sK0J7QNplR3M2op=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMojCSpBAJQWqPzknZCqBNyAJq9dnnKZ0hbcnX3=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMojCSpBAJQWqPzknZCqBNyAJq9dnnKZ0hbcnX3=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNS6eSPGLzcyoHmBW3iEeMkZE_4qM-0xyVhU1qb=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNS6eSPGLzcyoHmBW3iEeMkZE_4qM-0xyVhU1qb=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipOLcb2ZsAgaTLJSV6PhNqEi_N8isyr3LTcT8mii=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipOLcb2ZsAgaTLJSV6PhNqEi_N8isyr3LTcT8mii=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSxMk_v3Pm0TLGsc3pW0OHQ5wJRI7w_YxpX4tBuv0LcFOCJDRFLHTZcMCm2NMe3cQ6TeZsmRRRpTJUrtWPiOl1VswI00YWHEYWtd1AuzAbnjWqqb5Eu2N5YMDRwU2r3zBy_tGSC2=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgIDK8uGuhwE=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/gps-cs-s/AG0ilSwgWfL99zmwAlKwS4VmAH1c7w4_DZOsLNoKTEGm1J37iuFaeizt6jSrZY7RymBq9TmkdAANYpbeH1B2gF9bKdVM8wuaupsdb3Ue3ATNTQy92bCqW-ROuC19juGnJoQUtr46zDtO=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/CIHM0ogKEICAgICG0rqOKQ=s10000"
                }
            ],
            "overall_rating": 4.8,
            "reviews": 32,
            "ratings": [
                {
                "stars": 5,
                "count": 29
                },
                {
                "stars": 4,
                "count": 2
                },
                {
                "stars": 3,
                "count": 0
                },
                {
                "stars": 2,
                "count": 0
                },
                {
                "stars": 1,
                "count": 1
                }
            ],
            "location_rating": 2.5,
            "reviews_breakdown": [
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 13,
                "positive": 13,
                "negative": 0,
                "neutral": 0
                }
            ],
            "amenities": [
                "Kid-friendly"
            ]
            },
            {
            "type": "hotel",
            "name": "SUNRISE INN OF GREENWOOD",
            "property_token": "ChkIpfG78dbE3vRvGg0vZy8xMXg5NXlxYmo1EAE",
            "serpapi_property_details_link": "https://serpapi.com/search.json?adults=1&check_in_date=2026-02-05&check_out_date=2026-02-13&children=0&currency=CAD&engine=google_hotels&gl=ca&hl=en&property_token=ChkIpfG78dbE3vRvGg0vZy8xMXg5NXlxYmo1EAE&q=JFK&rating=7&sort_by=13",
            "gps_coordinates": {
                "latitude": 34.2116859,
                "longitude": -82.1748561
            },
            "check_in_time": "3:00 PM",
            "check_out_time": "11:00 AM",
            "nearby_places": [
                {
                "name": "Greenwood Museum",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "6 min"
                    }
                ]
                },
                {
                "name": "Greenville-Spartanburg International Airport",
                "transportations": [
                    {
                    "type": "Taxi",
                    "duration": "1 hr 16 min"
                    }
                ]
                },
                {
                "name": "Santa Fe Mexican Grill",
                "transportations": [
                    {
                    "type": "Walking",
                    "duration": "2 min"
                    }
                ]
                }
            ],
            "hotel_class": "2-star hotel",
            "extracted_hotel_class": 2,
            "images": [
                {
                "thumbnail": "https://lh5.googleusercontent.com/proxy/ZQ2sLnDxyG1swsW7FnGhrtCtcpjPtcKo4H_0aOP8SRE-VLj_JfoLK28FXMLdG3YRstF8F9m6FxFlEgfaK12iil3uQztS37O_JBAGgR0wHlWaQrmoBUDrGP5Bt4hA6ubsVxfIRa0fPqL2G7AbrlTVurzsAFD4fQ=s287-w287-h192-n-k-no-v1",
                "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KAPitTAQFAIHVPoPxNhzkywkN-uB7Tjs"
                },
                {
                "thumbnail": "https://lh4.googleusercontent.com/proxy/BcZju3T5lsF6pcxfCQcRbh-7l-bW4Od15VprUHdPFVlN2Bsk57dOzgTBOTTu9-orwYxHW0cbayN7B3h4tmsOwM1CdOcFP57iIWxUR1y2_lNXip4nzueEhekVAfj8sUxVsOfKR1YY0J8P7EHj3bZkFu9Vrp03cNM=s287-w287-h192-n-k-no-v1",
                "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KAPatTAQFAOovP4xf4O6NtbD4_-Z0Ols"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMQV_HyDW0tGZbxus_IKYblhPkcUGFg_593AYvj=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMQV_HyDW0tGZbxus_IKYblhPkcUGFg_593AYvj=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipMbMo2GvI03rd6nSNMFc_CS1i-tmb-T5P23AAra=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipMbMo2GvI03rd6nSNMFc_CS1i-tmb-T5P23AAra=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipP4Vic4CVTLcvM3kyAm-gGX93hNxE5KlLROC_IP=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipP4Vic4CVTLcvM3kyAm-gGX93hNxE5KlLROC_IP=s10000"
                },
                {
                "thumbnail": "https://lh3.googleusercontent.com/p/AF1QipNRuEogMRHppsfkUFAQce87wBqc_op6deL5hDg0=s287-w287-h192-n-k-no-v1",
                "original_image": "https://lh5.googleusercontent.com/p/AF1QipNRuEogMRHppsfkUFAQce87wBqc_op6deL5hDg0=s10000"
                },
                {
                "thumbnail": "https://lh5.googleusercontent.com/proxy/O7K_irgkNdmlJMSaQuvX80Voc_tRQVQY6jp7s9g4RCN5Hl2e4Rr-XIpa-A4k7E3Ct8Zvqyk4u3u5zWqBXg53bDPBinOn5SJydDdQxdl26R4gbUpK_jzG3hDTkASgv2v9Sa47WUnPPR_DGzlyey3RZtUKYK0DKQ=s287-w287-h192-n-k-no-v1",
                "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KAASuTAQFAFQJI7xoXmUUCrwI6b6U8K0"
                },
                {
                "thumbnail": "https://lh5.googleusercontent.com/proxy/XJDAH_d4gQLesXNdLdAFLyLLbaosdvoqjA5yi524y0hLaqLIFUr_LikJs4ejqeCGXucvokWWqz8L5za3qvVbmFDO6c0-0ay9JiekSxlKetGuEr5iN0UAGiQ-Z5NOq22rD8c3UNTNor8LTWRpvM216jXk0MH7BV0=s287-w287-h192-n-k-no-v1",
                "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KAPmtTAQFAIzmVWUyrvNyZZnZZi2DXU4"
                },
                {
                "thumbnail": "https://lh5.googleusercontent.com/proxy/4hsJctwhNpmQS4nj3VGHRhWYoTwjnxAYuw5CNn8ywOrTCN9GOMvIcC_FLoOfQ_j0IOdLea95ZEXrWrJeGrRTBjc86S7pNJdWZfGZOg4KKf9YYNfE7K6Zux-grXpQaq6w7hj6MSZPx3nQU69LJukjHsK5AzhOxw=s287-w287-h192-n-k-no-v1",
                "original_image": "https://i.giatamedia.com/m.php?m=AQABAAAAla4KAP2tTAQFAN5ol5mv0qPyexs22U2imDY"
                }
            ],
            "overall_rating": 5,
            "reviews": 20,
            "ratings": [
                {
                "stars": 5,
                "count": 19
                },
                {
                "stars": 4,
                "count": 1
                },
                {
                "stars": 3,
                "count": 0
                },
                {
                "stars": 2,
                "count": 0
                },
                {
                "stars": 1,
                "count": 0
                }
            ],
            "location_rating": 3.9,
            "reviews_breakdown": [
                {
                "name": "Property",
                "description": "Property",
                "total_mentioned": 13,
                "positive": 13,
                "negative": 0,
                "neutral": 0
                },
                {
                "name": "Service",
                "description": "Service",
                "total_mentioned": 13,
                "positive": 13,
                "negative": 0,
                "neutral": 0
                }
            ],
            "amenities": [
                "Free Wi-Fi",
                "Free parking",
                "Air conditioning",
                "Pet-friendly",
                "Fitness center",
                "Golf",
                "Accessible"
            ]
            }
        ]
        }
''')
