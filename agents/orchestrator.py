
from agents.travel import TravelAgent
from agents.weather_agent import WeatherAgent
from datetime import datetime

class OrchestratorAgent:
    """Coordinates between multiple AI agents for complete trip planning"""
    
    def __init__(self):
        print("🎯 Initializing Orchestrator Agent...")
        self.travel_agent = TravelAgent()
        self.weather_agent = WeatherAgent()
        print("✅ All agents initialized!")
        print()
    
    def plan_trip(self, destination, days, budget, interests, start_date=None):
        """Orchestrate the complete trip planning process"""
        
        if not start_date:
            start_date = datetime.now()
        
        print("="*70)
        print("🎯 ORCHESTRATOR: Starting Multi-Agent Trip Planning")
        print("="*70)
        print(f"📍 Destination: {destination}")
        print(f"📅 Duration: {days} days")
        print(f"💰 Budget: ${budget} per person")
        print(f"🎯 Interests: {interests}")
        print("="*70)
        print()
        
        # AGENT 1: Weather Agent
        print("┌" + "─"*68 + "┐")
        print("│ 🌤️  AGENT 1: WEATHER AGENT" + " "*40 + "│")
        print("└" + "─"*68 + "┘")
        print()
        print("📡 ORCHESTRATOR → Weather Agent: Requesting forecast data...")
        
        forecast = self.weather_agent.get_forecast(destination, days)
        recommendations = self.weather_agent.get_weather_recommendations(forecast)
        weather_summary = self.weather_agent.format_weather_summary(
            destination, forecast, recommendations
        )
        
        print("✅ Weather Agent → ORCHESTRATOR: Data received")
        print()
        
        # AGENT 2: Travel Agent
        print("┌" + "─"*68 + "┐")
        print("│ ✈️  AGENT 2: TRAVEL AGENT" + " "*42 + "│")
        print("└" + "─"*68 + "┘")
        print()
        print("📡 ORCHESTRATOR → Travel Agent: Requesting itinerary...")
        print("   Including weather forecast data from Agent 1")
        print()
        
        itinerary = self.travel_agent.create_itinerary_with_weather(
            destination=destination,
            days=days,
            budget=budget,
            interests=interests,
            weather_summary=weather_summary,
            start_date=start_date
        )
        
        print()
        print("✅ Travel Agent → ORCHESTRATOR: Itinerary received")
        print()
        
        # Combine Results
        print("┌" + "─"*68 + "┐")
        print("│ 🔄 ORCHESTRATOR: COMBINING RESULTS" + " "*33 + "│")
        print("└" + "─"*68 + "┘")
        print()
        
        full_plan = f"""
{weather_summary}

{'='*70}

📋 YOUR COMPLETE TRAVEL PLAN
{'='*70}

{itinerary}

{'='*70}
✅ Plan created by Multi-Agent System:
   🌤️  Weather Agent - Forecast & recommendations
   ✈️  Travel Agent - Itinerary planning
   🎯 Orchestrator - Coordination & integration
{'='*70}
"""
        
        print("✅ ORCHESTRATOR: Trip planning complete!")
        print()
        
        return full_plan

# Test the orchestrator
if __name__ == "__main__":
    print()
    print("="*70)
    print("🧪 TESTING ORCHESTRATOR AGENT")
    print("="*70)
    print()
    
    try:
        # Initialize orchestrator (which initializes all agents)
        orchestrator = OrchestratorAgent()
        
        # Plan a trip
        plan = orchestrator.plan_trip(
            destination="Barcelona",
            days=4,
            budget=1200,
            interests="architecture, food, beaches, Gaudi"
        )
        
        # Display final plan
        print()
        print("="*70)
        print("📄 FINAL MULTI-AGENT TRAVEL PLAN")
        print("="*70)
        print()
        print(plan)
        
        print()
        print("="*70)
        print("✅ ORCHESTRATOR TEST COMPLETED!")
        print("="*70)
        
    except Exception as e:
        print()
        print("="*70)
        print("❌ ORCHESTRATOR TEST FAILED!")
        print("="*70)
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()