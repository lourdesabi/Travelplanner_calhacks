from travel import TravelAgent
from weather_agent import WeatherAgent
from flight_agent import FlightAgent
from links_agent import LinksAgent
from datetime import datetime

class OrchestratorAgent:
    """Coordinates between multiple AI agents for complete trip planning"""
    
    def __init__(self):
        print("🎯 Initializing Orchestrator Agent...")
        self.travel_agent = TravelAgent()
        self.weather_agent = WeatherAgent()
        self.flight_agent = FlightAgent()
        self.links_agent = LinksAgent()
        print("✅ All agents initialized!")
        print()
    
    def plan_complete_trip(self, origin, destination, departure_date, return_date, 
                          days, budget, interests, passengers=1, start_date=None):
        """Orchestrate complete trip planning with flights"""
        
        if not start_date:
            start_date = datetime.now()
        
        print("-"*50)
        print("🎯 ORCHESTRATOR: Starting Complete Trip Planning")
        print("-"*50)
        print(f"🛫 Origin: {origin}")
        print(f"📍 Destination: {destination}")
        print(f"📅 Departure: {departure_date}")
        print(f"📅 Return: {return_date}")
        print(f"👥 Travelers: {passengers}")
        print(f"📅 Duration: {days} days")
        print(f"💰 Budget: ${budget} per person")
        print(f"🎯 Interests: {interests}")
        print("-"*50)
        print()
        
        # AGENT 1: Links Agent
        print("┌" + "─"*68 + "┐")
        print("│ 🔗 AGENT 1: LINKS AGENT" + " "*44 + "│")
        print("└" + "─"*68 + "┘")
        print()
        print("📡 ORCHESTRATOR → Links Agent: Generating booking links...")
        
        booking_links = self.links_agent.format_all_links(
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            return_date=return_date,
            passengers=passengers
        )
        
        print("✅ Links Agent → ORCHESTRATOR: Booking links ready!")
        print()
        
        # AGENT 2: Flight Agent
        print("┌" + "─"*68 + "┐")
        print("│ ✈️  AGENT 2: FLIGHT AGENT" + " "*42 + "│")
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
        
        # AGENT 3: Weather Agent
        print("┌" + "─"*68 + "┐")
        print("│ 🌤️  AGENT 3: WEATHER AGENT" + " "*40 + "│")
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
        
        # AGENT 4: Travel Agent
        print("┌" + "─"*68 + "┐")
        print("│ 🗺️  AGENT 4: TRAVEL AGENT" + " "*42 + "│")
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
        
        # CLEAN OUTPUT - NO UGLY DASHES!
        complete_plan = f"""✈️ YOUR COMPLETE TRAVEL PLAN

{booking_links}

✈️ FLIGHT RECOMMENDATIONS

{flights}

🌤️ WEATHER FORECAST

{weather_summary}

🗺️ DAILY ITINERARY

{itinerary}

✅ Complete Plan Created by Multi-Agent System:
   🔗 Links Agent - Direct booking links
   ✈️ Flight Agent - Flight search & recommendations
   🌤️ Weather Agent - Forecast & packing tips
   🗺️ Travel Agent - Daily itinerary planning
   🎯 Orchestrator - Coordination & integration
"""
        
        print("✅ ORCHESTRATOR: Complete trip planning finished!")
        print()
        
        return complete_plan

# Test
if __name__ == "__main__":
    print()
    print("-"*50)
    print("🧪 TESTING COMPLETE ORCHESTRATOR WITH FLIGHTS")
    print("-"*50)
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
        print("-"*50)
        print("📄 COMPLETE TRAVEL PLAN")
        print("-"*50)
        print()
        print(plan)
        
        print()
        print("-"*50)
        print("✅ ORCHESTRATOR TEST COMPLETED!")
        print("-"*50)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
