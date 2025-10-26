from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class TravelAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def create_itinerary(self, destination, days, budget, interests):
        """Generate a travel itinerary"""
        
        print(f"🌍 Planning {days}-day trip to {destination}...")
        print(f"💰 Budget: ${budget} per person")
        print(f"🎯 Interests: {interests}")
        print()
        
        prompt = f"""
        Create a detailed {days}-day travel itinerary for {destination}.
        Budget: ${budget} per person
        Interests: {interests}
        
        Please provide:
        1. Day-by-day activities (morning, afternoon, evening)
        2. Restaurant recommendations with price ranges
        3. Estimated costs for each activity
        4. Travel tips and transportation suggestions
        5. Must-see attractions based on interests
        
        Format it clearly with each day separated.
        """
        
        print("🤖 AI is generating your itinerary...")
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert travel planner who creates detailed, budget-conscious itineraries."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        itinerary = response.choices[0].message.content
        print("✅ Itinerary generated!")
        print()
        
        return itinerary
    
    def create_itinerary_with_weather(self, destination, days, budget, interests, weather_summary, start_date=None):
        """Generate itinerary with pre-fetched weather data from orchestrator"""
        
        if not start_date:
            start_date = datetime.now()
        
        print(f"🌍 Travel Agent: Planning {days}-day trip to {destination}...")
        
        prompt = f"""
        Create a {days}-day travel itinerary for {destination}.
        Budget: ${budget} per person
        Interests: {interests}
        Start Date: {start_date.strftime('%Y-%m-%d')}
        
        WEATHER FORECAST:
        {weather_summary}
        
        Please provide a day-by-day itinerary that:
        1. Takes weather conditions into account
        2. Suggests indoor activities on rainy days
        3. Optimizes outdoor activities for best weather
        4. Includes estimated costs for each activity
        5. Provides restaurant recommendations with price ranges
        
        Format each day clearly with morning, afternoon, and evening activities.
        """
        
        print("🤖 Travel Agent: Generating weather-aware itinerary...")
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert travel planner who creates detailed, weather-aware itineraries."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        print("✅ Travel Agent: Itinerary complete!")
        
        return response.choices[0].message.content

# Test the Travel Agent
if __name__ == "__main__":
    print("="*70)
    print("🧪 TESTING TRAVEL AGENT")
    print("="*70)
    print()
    
    try:
        # Create travel agent
        agent = TravelAgent()
        
        # Test parameters
        destination = "Tokyo"
        days = 4
        budget = 1500
        interests = "anime, food, temples, technology"
        
        print(f"📝 Test Parameters:")
        print(f"   Destination: {destination}")
        print(f"   Duration: {days} days")
        print(f"   Budget: ${budget}")
        print(f"   Interests: {interests}")
        print()
        print("-"*70)
        print()
        
        # Generate itinerary
        itinerary = agent.create_itinerary(
            destination=destination,
            days=days,
            budget=budget,
            interests=interests
        )
        
        # Display results
        print()
        print("="*70)
        print("📄 YOUR TRAVEL ITINERARY")
        print("="*70)
        print()
        print(itinerary)
        
        print()
        print("="*70)
        print("✅ TEST COMPLETED SUCCESSFULLY!")
        print("="*70)
        
    except Exception as e:
        print()
        print("="*70)
        print("❌ TEST FAILED!")
        print("="*70)
        print(f"Error: {str(e)}")
        print()
        print("Common issues:")
        print("  - Missing OpenAI API key in .env file")
        print("  - Invalid API key")
        print("  - Network connection issues")