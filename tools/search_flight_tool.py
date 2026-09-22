import os
import requests
from dotenv import load_dotenv
load_dotenv()

AVIATION_STACK_API_KEY=os.getenv("AVIATION_STACK_API_KEY")

def search_flights(query:str):
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": AVIATION_STACK_API_KEY,
        "limit": 5
    }

    response = requests.get(url=url,params=params)

    data = response.json()

    flights = []

    if "data" in data:
        for flight in data["data"][:5]:
            airline = flight.get("airline",{}).get("name","unknown")
            departure = flight.get(
                "departure", {}
            ).get("airport", "Unknown")

            arrival = flight.get(
                "arrival", {}
            ).get("airport", "Unknown")

            status = flight.get("flight_status", "Unknown")

            flights.append(
                f"""
                    Airline: {airline}
                    Departure: {departure}
                    Arrival: {arrival}
                    Status: {status}
                    """
            )

    return "\n".join(flights)
