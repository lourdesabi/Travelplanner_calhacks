from datetime import datetime
from urllib.parse import quote

class LinksAgent:
    """Generates booking links for flights, hotels, and activities"""
    
    def __init__(self):
        print("🔗 Links Agent initialized!")
    
    def generate_flight_links(self, origin, destination, departure_date, return_date, passengers=1):
        """Generate flight search links for multiple platforms"""
        
        print(f"🔗 Links Agent: Generating flight search links...")
        
        # Format dates for URLs (YYYY-MM-DD)
        dep_date = departure_date if isinstance(departure_date, str) else departure_date.strftime('%Y-%m-%d')
        ret_date = return_date if isinstance(return_date, str) else return_date.strftime('%Y-%m-%d')
        
        links = {
            "Google Flights": f"https://www.google.com/travel/flights?q=flights+from+{quote(origin)}+to+{quote(destination)}+on+{dep_date}+return+{ret_date}",
            
            "Kayak": f"https://www.kayak.com/flights/{quote(origin)}-{quote(destination)}/{dep_date}/{ret_date}/{passengers}adults",
            
            "Skyscanner": f"https://www.skyscanner.com/transport/flights/{quote(origin)}/{quote(destination)}/{dep_date}/{ret_date}/?adults={passengers}",
            
            "Expedia": f"https://www.expedia.com/Flights-Search?flight-type=on&starDate={dep_date}&endDate={ret_date}&mode=search&trip=roundtrip&leg1=from:{quote(origin)},to:{quote(destination)}&passengers=adults:{passengers}",
            
            "Momondo": f"https://www.momondo.com/flight-search/{quote(origin)}-{quote(destination)}/{dep_date}/{ret_date}?sort=bestflight_a"
        }
        
        print("✅ Links Agent: Flight links generated!")
        return links
    
    def generate_hotel_links(self, destination, check_in, check_out, guests=2):
        """Generate hotel search links"""
        
        print(f"🔗 Links Agent: Generating hotel search links...")
        
        # Format dates
        checkin_date = check_in if isinstance(check_in, str) else check_in.strftime('%Y-%m-%d')
        checkout_date = check_out if isinstance(check_out, str) else check_out.strftime('%Y-%m-%d')
        
        links = {
            "Booking.com": f"https://www.booking.com/searchresults.html?ss={quote(destination)}&checkin={checkin_date}&checkout={checkout_date}&group_adults={guests}",
            
            "Hotels.com": f"https://www.hotels.com/search.do?destination={quote(destination)}&startDate={checkin_date}&endDate={checkout_date}&rooms=1&adults={guests}",
            
            "Airbnb": f"https://www.airbnb.com/s/{quote(destination)}/homes?checkin={checkin_date}&checkout={checkout_date}&adults={guests}",
            
            "Expedia Hotels": f"https://www.expedia.com/Hotel-Search?destination={quote(destination)}&startDate={checkin_date}&endDate={checkout_date}&rooms=1&adults={guests}",
            
            "Tripadvisor": f"https://www.tripadvisor.com/Hotels-g{quote(destination)}-Hotels.html"
        }
        
        print("✅ Links Agent: Hotel links generated!")
        return links
    
    def generate_activity_links(self, destination):
        """Generate links for activities and attractions"""
        
        print(f"🔗 Links Agent: Generating activity links...")
        
        links = {
            "Viator": f"https://www.viator.com/searchResults/all?text={quote(destination)}",
            
            "GetYourGuide": f"https://www.getyourguide.com/s/?q={quote(destination)}",
            
            "Tripadvisor Activities": f"https://www.tripadvisor.com/Attractions-g{quote(destination)}-Activities.html",
            
            "Klook": f"https://www.klook.com/en-US/search/?query={quote(destination)}",
            
            "Airbnb Experiences": f"https://www.airbnb.com/s/{quote(destination)}/experiences"
        }
        
        print("✅ Links Agent: Activity links generated!")
        return links
    
    def generate_restaurant_links(self, destination):
        """Generate restaurant search links"""
        
        print(f"🔗 Links Agent: Generating restaurant links...")
        
        links = {
            "OpenTable": f"https://www.opentable.com/s/?dateTime={quote(destination)}&covers=2&view=list&metroId=&latitude=&longitude=",
            
            "Yelp": f"https://www.yelp.com/search?find_desc=restaurants&find_loc={quote(destination)}",
            
            "Tripadvisor Restaurants": f"https://www.tripadvisor.com/Restaurants-g{quote(destination)}.html",
            
            "The Fork": f"https://www.thefork.com/search?cityId={quote(destination)}",
            
            "Google Maps": f"https://www.google.com/maps/search/restaurants+near+{quote(destination)}"
        }
        
        print("✅ Links Agent: Restaurant links generated!")
        return links
    
    def format_all_links(self, origin, destination, departure_date, return_date, passengers=2):
        """Generate all booking links and format as markdown"""
        
        print(f"🔗 Links Agent: Generating complete booking guide...")
        
        flight_links = self.generate_flight_links(origin, destination, departure_date, return_date, passengers)
        hotel_links = self.generate_hotel_links(destination, departure_date, return_date, passengers)
        activity_links = self.generate_activity_links(destination)
        restaurant_links = self.generate_restaurant_links(destination)
        
        formatted = f"""
{'='*70}
🔗 YOUR BOOKING LINKS
{'='*70}

✈️ FLIGHT BOOKING
{'='*70}
"""
        for name, url in flight_links.items():
            formatted += f"• {name}: {url}\n"
        
        formatted += f"""
{'='*70}
🏨 HOTEL BOOKING
{'='*70}
"""
        for name, url in hotel_links.items():
            formatted += f"• {name}: {url}\n"
        
        formatted += f"""
{'='*70}
🎯 ACTIVITIES & TOURS
{'='*70}
"""
        for name, url in activity_links.items():
            formatted += f"• {name}: {url}\n"
        
        formatted += f"""
{'='*70}
🍽️ RESTAURANT RESERVATIONS
{'='*70}
"""
        for name, url in restaurant_links.items():
            formatted += f"• {name}: {url}\n"
        
        formatted += f"""
{'='*70}
💡 TIP: Click these links to compare prices and book directly!
{'='*70}
"""
        
        print("✅ Links Agent: Complete booking guide ready!")
        return formatted

# Test
if __name__ == "__main__":
    print("="*70)
    print("🧪 TESTING LINKS AGENT")
    print("="*70)
    print()
    
    agent = LinksAgent()
    
    links = agent.format_all_links(
        origin="San Francisco",
        destination="Barcelona",
        departure_date="2025-12-15",
        return_date="2025-12-22",
        passengers=2
    )
    
    print(links)
    
    print()
    print("="*70)
    print("✅ LINKS AGENT TEST COMPLETE!")
    print("="*70)