from datetime import datetime
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class FlightAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        print("✈️ Flight Agent initialized!")
    
    def search_flights(self, origin, destination, departure_date, return_date=None, passengers=1, preferences=""):
        """Search and recommend flights"""
        
        print(f"✈️ Flight Agent: Searching flights from {origin} to {destination}...")
        
        flight_prompt = f"""Find and recommend flights for this trip:

FROM: {origin}
TO: {destination}
DEPARTURE: {departure_date}
{"RETURN: " + return_date if return_date else "ONE-WAY TRIP"}
PASSENGERS: {passengers}
PREFERENCES: {preferences if preferences else "Best value"}

Provide:

1. 🎯 RECOMMENDED FLIGHTS (3-5 options)
   For each option include:
   - Airline name
   - Flight numbers
   - Departure/arrival times
   - Duration and layovers
   - Price estimate per person
   - Pros and cons
   
2. 💰 PRICE COMPARISON
   - Economy class range
   - Premium economy (if available)
   
3. ⏰ BEST TIME TO BOOK
   - Current price trend
   
4. 🎒 BAGGAGE INFO
   - Carry-on and checked bag allowances
   
5. 💡 INSIDER TIPS
   - Best days to fly
   - How to save money

Use emojis and make it scannable.
Include real airline names and realistic prices."""

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert flight search assistant providing detailed flight recommendations."
                },
                {"role": "user", "content": flight_prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        print("✅ Flight Agent: Flight search complete!")
        return response.choices[0].message.content