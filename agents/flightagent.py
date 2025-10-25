"""
Flight Search Assistant - All Airlines
Provides flight recommendations and auto-filled booking links for all airlines
"""
from datetime import datetime
from uuid import uuid4
import json
import os
import re

from anthropic import Anthropic
from dotenv import load_dotenv
from uagents import Context, Protocol, Agent
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    EndSessionContent,
    StartSessionContent,
    TextContent,
    chat_protocol_spec,
)


load_dotenv()


def create_text_chat(text: str, end_session: bool = False) -> ChatMessage:
    """Create a chat message"""
    content = [TextContent(type="text", text=text)]
    if end_session:
        content.append(EndSessionContent(type="end-session"))
    return ChatMessage(timestamp=datetime.utcnow(), msg_id=uuid4(), content=content)


class FlightSearchAssistant:
    """General flight search assistant for all airlines"""
    
    AIRPORT_CODES = {
        "taipei": "TPE", "los angeles": "LAX", "san francisco": "SFO",
        "new york": "JFK", "seattle": "SEA", "chicago": "ORD",
        "houston": "IAH", "vancouver": "YVR", "toronto": "YYZ",
        "bangkok": "BKK", "singapore": "SIN", "tokyo": "NRT",
        "osaka": "KIX", "seoul": "ICN", "hong kong": "HKG",
        "manila": "MNL", "london": "LHR", "paris": "CDG",
        "vienna": "VIE", "amsterdam": "AMS", "la": "LAX",
        "sf": "SFO", "nyc": "JFK", "ny": "JFK", "taiwan": "TPE"
    }
    
    def __init__(self, claude_client):
        self.client = claude_client
    
    def get_airport_code(self, city_or_code):
        """Convert city name to airport code"""
        city_lower = str(city_or_code).lower().strip()
        return self.AIRPORT_CODES.get(city_lower, city_or_code.upper())
    
    def create_booking_links(self, origin, destination, departure_date, return_date=None, passengers=1):
        """Create fully pre-filled booking links"""
        origin_code = self.get_airport_code(origin)
        dest_code = self.get_airport_code(destination)
        
        links = {}
        
        # Google Flights - Best comparison tool
        dep_date_formatted = departure_date.replace("-", "")
        google_url = f"https://www.google.com/travel/flights?q=Flights%20to%20{dest_code}%20from%20{origin_code}%20on%20{dep_date_formatted}"
        if return_date:
            ret_date_formatted = return_date.replace("-", "")
            google_url += f"%20through%20{ret_date_formatted}"
        google_url += f"&curr=USD"
        links['google'] = google_url
        
        # Kayak - Price tracking
        kayak_url = f"https://www.kayak.com/flights/{origin_code}-{dest_code}/{departure_date}"
        if return_date:
            kayak_url += f"/{return_date}"
        kayak_url += f"/{passengers}adults?sort=bestflight_a"
        links['kayak'] = kayak_url
        
        # Skyscanner - Global search
        if return_date:
            sky_url = f"https://www.skyscanner.com/transport/flights/{origin_code.lower()}/{dest_code.lower()}/{departure_date}/{return_date}/?adults={passengers}&adultsv2={passengers}&cabinclass=economy"
        else:
            sky_url = f"https://www.skyscanner.com/transport/flights/{origin_code.lower()}/{dest_code.lower()}/{departure_date}/?adults={passengers}&adultsv2={passengers}&cabinclass=economy"
        links['skyscanner'] = sky_url
        
        # Expedia - Bundle deals
        expedia_url = f"https://www.expedia.com/Flights-Search"
        expedia_url += f"?flight-type={'roundtrip' if return_date else 'oneway'}"
        expedia_url += f"&mode=search"
        expedia_url += f"&trip={'roundtrip' if return_date else 'oneway'}"
        expedia_url += f"&leg1=from:{origin_code},to:{dest_code},departure:{departure_date}TANYT"
        if return_date:
            expedia_url += f"&leg2=from:{dest_code},to:{origin_code},departure:{return_date}TANYT"
        expedia_url += f"&passengers=adults:{passengers},children:0,infantinlap:N"
        expedia_url += "&options=cabinclass:economy"
        links['expedia'] = expedia_url
        
        # Momondo - Deal finder
        momondo_url = f"https://www.momondo.com/flight-search/{origin_code}-{dest_code}/{departure_date}"
        if return_date:
            momondo_url += f"/{return_date}"
        momondo_url += f"?sort=bestflight_a"
        links['momondo'] = momondo_url
        
        # CheapOair - Budget options
        cheapoair_url = f"https://www.cheapoair.com/flights/results"
        cheapoair_url += f"?type={'roundtrip' if return_date else 'oneway'}"
        cheapoair_url += f"&from1={origin_code}&to1={dest_code}&date1={departure_date}"
        if return_date:
            cheapoair_url += f"&date2={return_date}"
        cheapoair_url += f"&adults={passengers}&seniors=0&children=0"
        links['cheapoair'] = cheapoair_url
        
        return links
    
    def format_flight_search(self, origin, destination, departure_date, return_date=None, passengers=1):
        """Create formatted flight search response with auto-filled booking links"""
        
        origin_code = self.get_airport_code(origin)
        dest_code = self.get_airport_code(destination)
        
        # Get booking links
        links = self.create_booking_links(origin, destination, departure_date, return_date, passengers)
        
        # Build response
        response = "✈️ **FLIGHT SEARCH RESULTS**\n\n"
        response += f"📍 **Route:** {origin} ({origin_code}) → {destination} ({dest_code})\n"
        response += f"📅 **Date:** {departure_date}\n"
        if return_date:
            response += f"🔄 **Return:** {return_date}\n"
        response += f"👥 **Passengers:** {passengers}\n\n"
        
        response += "🔗 **Click below for REAL-TIME PRICES from all airlines!**\n"
        response += "\n" + "="*70 + "\n\n"
        
        # Google Flights - Primary recommendation
        response += "🔍 **Google Flights** ⭐ RECOMMENDED\n"
        response += f"   {links['google']}\n"
        response += f"   ✅ Compare ALL airlines at once\n"
        response += f"   ✅ Real-time prices updated live\n"
        response += f"   ✅ See price calendar & trends\n"
        response += f"   ✅ Track prices for free\n"
        response += f"   → **CLICK FOR INSTANT RESULTS**\n\n"
        
        response += "💵 **Kayak**\n"
        response += f"   {links['kayak']}\n"
        response += f"   ✅ Everything pre-filled\n"
        response += f"   ✅ Set price alerts\n"
        response += f"   ✅ Compare booking sites\n"
        response += f"   → **CLICK TO SEE PRICES**\n\n"
        
        response += "🌍 **Skyscanner**\n"
        response += f"   {links['skyscanner']}\n"
        response += f"   ✅ Global price comparison\n"
        response += f"   ✅ Find cheapest month\n"
        response += f"   ✅ Budget airline options\n"
        response += f"   → **CLICK TO COMPARE**\n\n"
        
        response += "🏨 **Expedia**\n"
        response += f"   {links['expedia']}\n"
        response += f"   ✅ Bundle with hotel & save\n"
        response += f"   ✅ Earn rewards points\n"
        response += f"   ✅ Package deals\n"
        response += f"   → **CLICK FOR BUNDLES**\n\n"
        
        response += "💰 **Momondo**\n"
        response += f"   {links['momondo']}\n"
        response += f"   ✅ Find hidden deals\n"
        response += f"   ✅ Price prediction\n"
        response += f"   → **CLICK FOR DEALS**\n\n"
        
        response += "✈️ **CheapOair**\n"
        response += f"   {links['cheapoair']}\n"
        response += f"   ✅ Budget-friendly options\n"
        response += f"   ✅ Last-minute deals\n"
        response += f"   → **CLICK FOR SAVINGS**\n\n"
        
        response += "="*70 + "\n\n"
        
        # Booking strategy
        response += "🎯 **HOW TO FIND THE BEST DEAL**\n\n"
        response += "**1️⃣ Click Google Flights link above** ⭐\n"
        response += f"   → Already filled: {origin_code} to {dest_code}, {departure_date}\n"
        response += "   → See all airlines and prices instantly\n"
        response += "   → Compare options side-by-side\n\n"
        
        response += "**2️⃣ Check prices on 2-3 other sites**\n"
        response += "   → Open Kayak and Skyscanner tabs\n"
        response += "   → Compare prices across sites\n"
        response += "   → Sometimes one site has better deals\n\n"
        
        response += "**3️⃣ Book the best option**\n"
        response += "   → Choose flight with best price/time combo\n"
        response += "   → Consider total travel time\n"
        response += "   → Check baggage allowance\n"
        response += "   → Book directly or through comparison site\n\n"
        
        response += "💡 **PRO TIPS:**\n"
        response += "• All links above are PRE-FILLED (no typing needed!)\n"
        response += "• Open multiple sites in tabs to compare\n"
        response += "• Book directly with airline for best service\n"
        response += "• Check if credit card offers travel insurance\n"
        response += "• Consider premium economy for long flights (10+ hours)\n\n"
        
        response += "="*70 + "\n\n"
        
        response += "✨ **ABOUT THESE LINKS**\n\n"
        response += "All links above have your search details automatically filled in:\n"
        response += f"• Origin: {origin_code}\n"
        response += f"• Destination: {dest_code}\n"
        response += f"• Date: {departure_date}\n"
        if return_date:
            response += f"• Return: {return_date}\n"
        response += f"• Passengers: {passengers}\n\n"
        response += "Just click → See real-time prices → Book! 🎉\n"
        
        return response


# Initialize
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
if not anthropic_api_key:
    raise EnvironmentError(
        "Missing ANTHROPIC_API_KEY environment variable. "
        "Add it to your .env file or export it before running the flight agent."
    )
client = Anthropic(api_key=anthropic_api_key)
agent = Agent(name="flight_search", seed="flight_search_general")
protocol = Protocol(spec=chat_protocol_spec)

conversations = {}
flight_assistant = FlightSearchAssistant(client)


def extract_params(text):
    """Extract flight parameters"""
    try:
        prompt = f"""Extract flight info from: "{text}"
Return JSON with: origin, destination, departure_date (YYYY-MM-DD), return_date, passengers
Today is {datetime.now().strftime('%Y-%m-%d')}.
JSON only:"""
        
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}]
        )
        
        result = message.content[0].text
        json_match = re.search(r'\{.*\}', result, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except Exception as e:
        print(f"Error: {e}")
    return {}


@protocol.on_message(ChatMessage)
async def handle_message(ctx: Context, sender: str, msg: ChatMessage):
    """Handle messages"""
    
    await ctx.send(
        sender,
        ChatAcknowledgement(timestamp=datetime.now(), acknowledged_msg_id=msg.msg_id),
    )
    
    if sender not in conversations:
        conversations[sender] = {"history": []}
    
    if any(isinstance(item, StartSessionContent) for item in msg.content):
        greeting = """✈️ **FLIGHT SEARCH ASSISTANT**
🔗 *Smart Search with Auto-Filled Booking Links*

**I HELP YOU FIND FLIGHTS:**
• 🔍 Search all major airlines
• 💰 Compare prices across multiple sites
• 🔗 Auto-filled booking links (no typing!)
• ⚡ Real-time prices when you click

**HOW IT WORKS:**
1️⃣ Tell me where & when you want to fly
2️⃣ I create pre-filled booking links
3️⃣ You click → See live prices → Book!

**EXAMPLE:**
You: "Find flights from Los Angeles to Tokyo on March 15"
Me: [Provides 6 auto-filled booking links]
You: [Click Google Flights] → See all airlines & prices

**TRY IT:**
"Find flights from [city] to [city] on [date]"

Let's find your perfect flight! 🎯
"""
        await ctx.send(sender, create_text_chat(greeting, end_session=False))
        return
    
    text = msg.text()
    if not text:
        return
    
    conversations[sender]["history"].append({"role": "user", "content": text})
    
    try:
        is_search = any(word in text.lower() for word in [
            "flight", "fly", "search", "find", "book", "ticket", "price", "cost"
        ])
        
        if is_search:
            ctx.logger.info("🔍 Creating flight search...")
            
            await ctx.send(sender, create_text_chat(
                "🔍 Creating your flight search with auto-filled booking links...",
                end_session=False
            ))
            
            params = extract_params(text)
            ctx.logger.info(f"Params: {params}")
            
            if params.get("origin") and params.get("destination"):
                # Generate flight search with links
                response = flight_assistant.format_flight_search(
                    params["origin"],
                    params["destination"],
                    params.get("departure_date", "2025-12-15"),
                    params.get("return_date"),
                    params.get("passengers", 1)
                )
            else:
                response = "❌ **Missing Information**\n\n"
                response += "Please provide:\n"
                if not params.get("origin"):
                    response += "• Departure city\n"
                if not params.get("destination"):
                    response += "• Destination city\n"
                response += "\n**Example:** 'Find flights from New York to London on June 1'"
        
        else:
            system = """You are a helpful flight and travel expert. Answer questions about:
            - Flights and airlines
            - Booking tips and strategies
            - Travel planning
            - Airports and routes
            - Baggage and travel policies
            Be helpful, concise, and friendly."""
            
            message = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=600,
                system=system,
                messages=conversations[sender]["history"][-6:],
            )
            response = message.content[0].text
        
        conversations[sender]["history"].append({"role": "assistant", "content": response})
        
    except Exception as e:
        ctx.logger.exception('Error')
        response = f"❌ Error: {str(e)}\n\nPlease try rephrasing your request."
    
    await ctx.send(sender, create_text_chat(response, end_session=False))


@protocol.on_message(ChatAcknowledgement)
async def handle_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    pass


agent.include(protocol, publish_manifest=True)


if __name__ == "__main__":
    print("=" * 70)
    print("✈️  FLIGHT SEARCH ASSISTANT")
    print("🔗 All Airlines - Auto-Filled Booking Links")
    print("=" * 70)
    print()
    print("✨ Features:")
    print("   • Search flights from ALL airlines")
    print("   • Compare prices across 6 booking sites")
    print("   • Auto-filled links (no typing needed)")
    print("   • Real-time prices when you click")
    print("   • Best deal recommendations")
    print()
    print("🎯 Just ask: 'Find flights from [city] to [city] on [date]'")
    print()
    print("💡 I'll give you 6 pre-filled booking links!")
    print("   Click any link → See live prices → Book best deal")
    print()
    print("Press Ctrl+C to stop")
    print("=" * 70)
    print()
    
    agent.run()
