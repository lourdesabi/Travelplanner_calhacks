
import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class WeatherAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.api_active = False
        self._check_api_status()
    
    def _check_api_status(self):
        """Check if API key is activated"""
        try:
            test_url = f"{self.base_url}/weather"
            params = {"q": "London", "appid": self.api_key}
            response = requests.get(test_url, params=params, timeout=5)
            
            if response.status_code == 200:
                self.api_active = True
                print("✅ Weather API is active!")
            elif response.status_code == 401:
                print("⏳ Weather API key not activated yet. Using mock data.")
            else:
                print(f"⚠️ Weather API returned status {response.status_code}")
        except Exception as e:
            print(f"⚠️ Could not connect to Weather API: {e}")
    
    def _get_mock_weather(self, city):
        """Return mock weather data when API isn't ready"""
        return {
            "temperature": 20,
            "feels_like": 18,
            "description": "partly cloudy",
            "humidity": 65,
            "wind_speed": 3.5,
            "icon": "02d"
        }
    
    def _get_mock_forecast(self, days=5):
        """Return mock forecast data"""
        forecast = {}
        base_date = datetime.now()
        
        for i in range(days):
            date = (base_date + timedelta(days=i)).strftime('%Y-%m-%d')
            forecast[date] = {
                "avg_temp": 20 + i,
                "min_temp": 15 + i,
                "max_temp": 25 + i,
                "description": "partly cloudy",
                "avg_humidity": 60,
                "rain_chance": 20 if i % 2 == 0 else 10
            }
        
        return forecast
    
    def get_current_weather(self, city):
        """Get current weather for a city"""
        if not self.api_active:
            print(f"⚠️ Using mock weather data for {city}")
            return self._get_mock_weather(city)
        
        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 401:
                print("⏳ API key still not active. Using mock data.")
                self.api_active = False
                return self._get_mock_weather(city)
            
            response.raise_for_status()
            data = response.json()
            
            return {
                "temperature": data['main']['temp'],
                "feels_like": data['main']['feels_like'],
                "description": data['weather'][0]['description'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed'],
                "icon": data['weather'][0]['icon']
            }
        except Exception as e:
            print(f"Error getting weather: {e}")
            return self._get_mock_weather(city)
    
    def get_forecast(self, city, days=5):
        """Get weather forecast"""
        if not self.api_active:
            print(f"⚠️ Using mock forecast data for {city}")
            return self._get_mock_forecast(days)
        
        url = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "cnt": days * 8
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 401:
                print("⏳ API key still not active. Using mock data.")
                self.api_active = False
                return self._get_mock_forecast(days)
            
            response.raise_for_status()
            data = response.json()
            
            daily_forecast = {}
            
            for item in data['list']:
                date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
                
                if date not in daily_forecast:
                    daily_forecast[date] = {
                        "temps": [],
                        "descriptions": [],
                        "humidity": [],
                        "rain_chance": 0
                    }
                
                daily_forecast[date]["temps"].append(item['main']['temp'])
                daily_forecast[date]["descriptions"].append(item['weather'][0]['description'])
                daily_forecast[date]["humidity"].append(item['main']['humidity'])
                
                if 'rain' in item or item.get('pop', 0) > 0:
                    daily_forecast[date]["rain_chance"] = max(
                        daily_forecast[date]["rain_chance"], 
                        item.get('pop', 0) * 100
                    )
            
            forecast_summary = {}
            for date, data_item in daily_forecast.items():
                forecast_summary[date] = {
                    "avg_temp": round(sum(data_item['temps']) / len(data_item['temps']), 1),
                    "min_temp": round(min(data_item['temps']), 1),
                    "max_temp": round(max(data_item['temps']), 1),
                    "description": max(set(data_item['descriptions']), key=data_item['descriptions'].count),
                    "avg_humidity": round(sum(data_item['humidity']) / len(data_item['humidity'])),
                    "rain_chance": round(data_item['rain_chance'])
                }
            
            return forecast_summary
            
        except Exception as e:
            print(f"Error getting forecast: {e}")
            return self._get_mock_forecast(days)
    
    def get_weather_recommendations(self, forecast_data):
        """Generate packing recommendations based on weather"""
        recommendations = {
            "packing_list": [],
            "activity_tips": [],
            "warnings": []
        }
        
        if not forecast_data:
            return recommendations
        
        temps = [day['avg_temp'] for day in forecast_data.values()]
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        
        if avg_temp > 25:
            recommendations["packing_list"].extend([
                "Light, breathable clothing",
                "Sunscreen (SPF 30+)",
                "Sunglasses",
                "Hat for sun protection",
                "Water bottle"
            ])
        elif avg_temp > 15:
            recommendations["packing_list"].extend([
                "Light jacket or sweater",
                "Comfortable walking shoes",
                "Light layers"
            ])
        else:
            recommendations["packing_list"].extend([
                "Warm jacket",
                "Scarf and gloves",
                "Warm layers",
                "Waterproof boots"
            ])
        
        rain_days = sum(1 for day in forecast_data.values() if day['rain_chance'] > 50)
        if rain_days > 0:
            recommendations["packing_list"].extend([
                "Umbrella",
                "Rain jacket",
                "Waterproof shoes"
            ])
        
        if max_temp > 35:
            recommendations["warnings"].append("⚠️ Extreme heat - stay hydrated!")
        elif min_temp < 0:
            recommendations["warnings"].append("⚠️ Freezing temps - dress warmly!")
        
        return recommendations
    
    def format_weather_summary(self, city, forecast_data, recommendations):
        """Format weather as readable text"""
        summary = f"""
🌤️ **Weather for {city}**

**Forecast:**
"""
        for date, data in list(forecast_data.items())[:5]:
            summary += f"\n📅 {date}: {data['min_temp']}°C - {data['max_temp']}°C, {data['description']}"
            if data['rain_chance'] > 30:
                summary += f" (Rain: {data['rain_chance']}%)"
        
        summary += "\n\n🎒 **Pack:**"
        for item in recommendations['packing_list'][:5]:
            summary += f"\n  • {item}"
        
        if recommendations['warnings']:
            summary += "\n\n⚠️ **Warnings:**"
            for warning in recommendations['warnings']:
                summary += f"\n  • {warning}"
        
        return summary

# Test the weather agent
if __name__ == "__main__":
    print("="*70)
    print("🧪 TESTING WEATHER AGENT")
    print("="*70)
    print()
    
    weather = WeatherAgent()
    
    city = "Paris"
    print(f"Getting weather for {city}...\n")
    
    forecast = weather.get_forecast(city, days=5)
    recommendations = weather.get_weather_recommendations(forecast)
    summary = weather.format_weather_summary(city, forecast, recommendations)
    
    print(summary)
    print()
    print("="*70)
    print("✅ TEST COMPLETED!")
    print("="*70)