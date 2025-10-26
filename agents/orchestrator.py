from travel import TravelAgent
from weather_agent import WeatherAgent
from flight_agent import FlightAgent
from datetime import datetime

class OrchestratorAgent:
    """Coordinates between multiple AI agents for complete trip planning"""
    
    def __init__(self):
        print("🎯 Initializing Orchestrator Agent...")
        self.travel_agent = TravelAgent()
        self.weather_agent = WeatherAgent()
        self.flight_agent = FlightAgent()
        print("✅ All agents initialized!")
        print()
    
    def plan_complete_trip(self, origin, destination, departure_date, return_date, 
                          days, budget, interests, passengers=1, start_date=None):
        """Orchestrate complete trip planning with flights"""
        
        if not start_date:
            start_date = datetime.now()
        
        print("="*70)
        print("🎯 ORCHESTRATOR: Starting Complete Trip Planning")
        print("="*70)
        print(f"🛫 Origin: {origin}")
        print(f"📍 Destination: {destination}")
        print(f"📅 Departure: {departure_date}")
        print(f"📅 Return: {return_date}")
        print(f"👥 Travelers: {passengers}")
        print(f"📅 Duration: {days} days")
        print(f"💰 Budget: ${budget} per person")
        print(f"🎯 Interests: {interests}")
        print("="*70)
        print()
        
        # AGENT 1: Flight Agent
        print("┌" + "─"*68 + "┐")
        print("│ ✈️  AGENT 1: FLIGHT AGENT" + " "*42 + "│")
        print("└" + "─"*68 + "┘")
        print()
        print("📡 ORCHESTRATOR → Flight Agent: Searching flights...")
        
        flights = self.flight_agent.search_flights(
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            return_date=return_date,
            passengers=passengers,
            preferences=f"Budget: ${budget}, Interests: {interests}"
        )
        
        print("✅ Flight Agent → ORCHESTRATOR: Flight options received")
        print()
        
        # AGENT 2: Weather Agent
        print("┌" + "─"*68 + "┐")
        print("│ 🌤️  AGENT 2: WEATHER AGENT" + " "*40 + "│")
        print("└" + "─"*68 + "┘")
        print()
        print("📡 ORCHESTRATOR → Weather Agent: Requesting forecast...")
        
        forecast = self.weather_agent.get_forecast(destination, days)
        recommendations = self.weather_agent.get_weather_recommendations(forecast)
        weather_summary = self.weather_agent.format_weather_summary(
            destination, forecast, recommendations
        )
        
        print("✅ Weather Agent → ORCHESTRATOR: Data received")
        print()
        
        # AGENT 3: Travel Agent
        print("┌" + "─"*68 + "┐")
        print("│ 🗺️  AGENT 3: TRAVEL AGENT" + " "*42 + "│")
        print("└" + "─"*68 + "┘")
        print()
        print("📡 ORCHESTRATOR → Travel Agent: Creating itinerary...")
        
        itinerary = self.travel_agent.create_itinerary_with_weather(
            destination=destination,
            days=days,
            budget=budget,
            interests=interests,
            weather_summary=weather_summary,
            start_date=start_date
        )
        
        print("✅ Travel Agent → ORCHESTRATOR: Itinerary received")
        print()
        
        # Combine All Results
        print("┌" + "─"*68 + "┐")
        print("│ 🔄 ORCHESTRATOR: COMBINING ALL RESULTS" + " "*29 + "│")
        print("└" + "─"*68 + "┘")
        print()
        
        complete_plan = f"""
{'='*70}
✈️ YOUR COMPLETE TRAVEL PLAN
{'='*70}

🛫 FLIGHTS
{'='*70}
{flights}

{'='*70}
🌤️ WEATHER FORECAST
{'='*70}
{weather_summary}

{'='*70}
🗺️ DAILY ITINERARY
{'='*70}
{itinerary}

{'='*70}
✅ Complete Plan Created by Multi-Agent System:
   ✈️  Flight Agent - Flight search & recommendations
   🌤️  Weather Agent - Forecast & packing tips
   🗺️  Travel Agent - Daily itinerary planning
   🎯 Orchestrator - Coordination & integration
{'='*70}
"""
        
        print("✅ ORCHESTRATOR: Complete trip planning finished!")
        print()
        
        return complete_plan

# Test
if __name__ == "__main__":
    print()
    print("="*70)
    print("🧪 TESTING COMPLETE ORCHESTRATOR WITH FLIGHTS")
    print("="*70)
    print()
    
    try:
        orchestrator = OrchestratorAgent()
        
        plan = orchestrator.plan_complete_trip(
            origin="San Francisco",
            destination="Barcelona",
            departure_date="2025-12-15",
            return_date="2025-12-22",
            days=7,
            budget=2000,
            interests="architecture, food, beaches, Gaudi",
            passengers=2
        )
        
        print()
        print("="*70)
        print("📄 COMPLETE TRAVEL PLAN")
        print("="*70)
        print()
        print(plan)
        
        print()
        print("="*70)
        print("✅ ORCHESTRATOR TEST COMPLETED!")
        print("="*70)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()