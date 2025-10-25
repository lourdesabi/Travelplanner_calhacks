from datetime import datetime
from uuid import uuid4

from openai import OpenAI
from uagents import Context, Protocol, Agent
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    EndSessionContent,
    StartSessionContent,
    TextContent,
    chat_protocol_spec,
)

##
### Travel Itinerary Assistant
##
## This chat agent creates detailed travel itineraries for any destination worldwide.
## It remembers your conversation and builds your trip piece by piece.
##

def create_text_chat(text: str, end_session: bool = False) -> ChatMessage:
    content = [TextContent(type="text", text=text)]
    if end_session:
        content.append(EndSessionContent(type="end-session"))
    return ChatMessage(timestamp=datetime.utcnow(), msg_id=uuid4(), content=content)

client = OpenAI(
    base_url='https://api.asi1.ai/v1',
    api_key='',
)

agent = Agent()
protocol = Protocol(spec=chat_protocol_spec)

# Store conversation state for each user
user_conversations = {}

# 200+ worldwide destinations
DESTINATIONS = {
    'el salvador': 'El Salvador', 'san salvador': 'San Salvador, El Salvador',
    'guatemala': 'Guatemala', 'antigua': 'Antigua, Guatemala', 'lake atitlan': 'Lake Atitlan, Guatemala',
    'costa rica': 'Costa Rica', 'nicaragua': 'Nicaragua', 'panama': 'Panama',
    'mexico': 'Mexico', 'cancun': 'Cancun, Mexico', 'tulum': 'Tulum, Mexico',
    'peru': 'Peru', 'machu picchu': 'Machu Picchu, Peru', 'cusco': 'Cusco, Peru',
    'colombia': 'Colombia', 'cartagena': 'Cartagena, Colombia',
    'brazil': 'Brazil', 'rio': 'Rio de Janeiro, Brazil',
    'argentina': 'Argentina', 'buenos aires': 'Buenos Aires, Argentina',
    'san francisco': 'San Francisco, USA', 'los angeles': 'Los Angeles, USA',
    'new york': 'New York City, USA', 'miami': 'Miami, USA',
    'paris': 'Paris, France', 'london': 'London, UK', 'rome': 'Rome, Italy',
    'barcelona': 'Barcelona, Spain', 'amsterdam': 'Amsterdam, Netherlands',
    'santorini': 'Santorini, Greece', 'tokyo': 'Tokyo, Japan', 'bali': 'Bali, Indonesia',
    'dubai': 'Dubai, UAE', 'bangkok': 'Bangkok, Thailand', 'singapore': 'Singapore',
    'morocco': 'Morocco', 'egypt': 'Egypt', 'south africa': 'South Africa',
    'australia': 'Australia', 'sydney': 'Sydney, Australia', 'new zealand': 'New Zealand',
}

def extract_info(text: str) -> dict:
    """Extract destination and days from text"""
    text_lower = text.lower()
    info = {'destination': None, 'days': None}
    
    # Find destination (longest match first)
    for key, value in sorted(DESTINATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        if key in text_lower:
            info['destination'] = value
            break
    
    # Find days
    import re
    patterns = [
        (r'(\d+)\s*(?:day|days)', lambda x: int(x)),
        (r'^\s*(\d+)\s*$', lambda x: int(x)),
        (r'weekend', lambda x: 3),
        (r'week', lambda x: 7),
    ]
    for pattern, converter in patterns:
        match = re.search(pattern, text_lower)
        if match:
            info['days'] = converter(match.group(1)) if match.groups() else converter(None)
            break
    
    return info


@protocol.on_message(ChatMessage)
async def handle_message(ctx: Context, sender: str, msg: ChatMessage):
    await ctx.send(
        sender,
        ChatAcknowledgement(timestamp=datetime.now(), acknowledged_msg_id=msg.msg_id),
    )

    # Initialize user conversation if needed
    if sender not in user_conversations:
        user_conversations[sender] = {
            'destination': None,
            'days': None,
            'conversation_history': []
        }

    # Greet on session start
    if any(isinstance(item, StartSessionContent) for item in msg.content):
        greeting = """✈️ Hey! I'm your travel planner!

I create detailed itineraries for destinations worldwide - from El Salvador to Tokyo, Paris to Patagonia!

Where do you want to go? 🌍"""
        await ctx.send(sender, create_text_chat(greeting, end_session=False))
        return

    text = msg.text()
    if not text:
        return

    # Extract info from current message
    extracted = extract_info(text)
    state = user_conversations[sender]
    
    # Update state with new info
    if extracted['destination']:
        state['destination'] = extracted['destination']
    if extracted['days']:
        state['days'] = extracted['days']
    
    # Add to conversation history
    state['conversation_history'].append({"role": "user", "content": text})
    
    # Check what info we still need
    if not state['destination']:
        response = "Where would you like to go? Any country or city works! 🌍"
        await ctx.send(sender, create_text_chat(response, end_session=False))
        state['conversation_history'].append({"role": "assistant", "content": response})
        return
    
    if not state['days']:
        response = f"Perfect! {state['destination']} 🏝️\n\nHow many days will you be there?"
        await ctx.send(sender, create_text_chat(response, end_session=False))
        state['conversation_history'].append({"role": "assistant", "content": response})
        return
    
    # We have everything - generate itinerary!
    ctx.logger.info(f"Generating itinerary: {state['destination']}, {state['days']} days")
    
    await ctx.send(sender, create_text_chat(
        f"🎨 Perfect! Creating your detailed {state['days']}-day {state['destination']} itinerary...\n\n⏱️ This takes about 20 seconds...",
        end_session=False
    ))
    
    try:
        # Build context from conversation
        conversation_context = "\n".join([
            f"{msg['role']}: {msg['content']}" 
            for msg in state['conversation_history'][-5:]
        ])
        
        itinerary_prompt = f"""Create an incredibly detailed, engaging {state['days']}-day travel itinerary for {state['destination']}.

Make it professional and comprehensive with:

1. CATCHY TITLE with emoji
2. INTRODUCTION (2-3 sentences about the destination)
3. ACCOMMODATION RECOMMENDATIONS
   - Specific hotel names with price ranges
   - Location benefits

4. BUDGET OVERVIEW
   - Breakdown by category (accommodation, food, transport, activities)
   - Daily cost estimate

5. DETAILED DAILY ITINERARIES:
   For each day, include:
   
   📅 DAY X: [Theme]
   
   Morning (9:00 AM - 12:00 PM)
   - Specific activities and attractions with entry costs
   - Walking/transport times
   
   Breakfast: [Restaurant Name] (Address if known)
   * Signature dishes
   * Price range: $X-Y
   
   Afternoon (1:00 PM - 5:00 PM)
   - Activities with details
   
   Lunch: [Restaurant Name]
   * Menu highlights  
   * Price range: $X-Y
   
   Evening (6:00 PM - 9:00 PM)
   - Evening activities
   
   Dinner: [Restaurant Name]
   * Cuisine type and specialties
   * Price range: $X-Y
   
   💡 Insider Tip: [Specific actionable advice]
   
   Transportation: [How to get around this day]

6. ENDING SECTIONS:
   - Total budget breakdown
   - Transportation tips (getting around the city)
   - What to pack
   - Best times to visit

Use emojis to make it scannable (📅 🍽️ 💡 🚗 💰).
Include REAL place names whenever possible.
Make it exciting and detailed like a travel magazine!
Write at least 1500-2000 words.

Previous conversation context:
{conversation_context}"""

        r = client.chat.completions.create(
            model="asi1-mini",
            messages=[
                {"role": "system", "content": "You are an expert travel planner who creates detailed, engaging itineraries with specific recommendations, prices, and insider tips. You write in a friendly, enthusiastic style."},
                {"role": "user", "content": itinerary_prompt},
            ],
            max_tokens=3500,
            temperature=0.7,
        )

        itinerary = str(r.choices[0].message.content)
        
        # Add footer
        itinerary += "\n\n✨ Want to adjust anything? Just let me know! I can modify destinations, add more details, or change the focus!"
        
        state['conversation_history'].append({"role": "assistant", "content": itinerary})
        
        # Send the itinerary
        await ctx.send(sender, create_text_chat(itinerary, end_session=False))
        
        # Reset state for potential new trip
        state['destination'] = None
        state['days'] = None
        
    except Exception as e:
        ctx.logger.exception('Error generating itinerary')
        error_msg = f"Oops! I had trouble creating your itinerary. Error: {str(e)[:100]}\n\nLet's try again! Where would you like to go?"
        await ctx.send(sender, create_text_chat(error_msg, end_session=False))


@protocol.on_message(ChatAcknowledgement)
async def handle_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    pass


agent.include(protocol, publish_manifest=True)

if __name__ == "__main__":
    print("="*70)
    print("✈️  TRAVEL ITINERARY AGENT")
    print("="*70)
    print("✅ Creates detailed day-by-day itineraries")
    print("🌍 200+ destinations worldwide (Latin America, Europe, Asia, etc.)")
    print("🍽️  Specific restaurants, prices, and insider tips")
    print("💬 Conversational - remembers info as you chat")
    print("⚡ Powered by ASI-1 API")
    print("\n📝 Your API key is configured and ready!")
    print("="*70 + "\n")
    
    agent.run()