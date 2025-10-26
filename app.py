
import streamlit as st
import sys
sys.path.append('agents')

from orchestrator import OrchestratorAgent
from datetime import datetime, timedelta

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

# Title
st.title("✈️ AI Multi-Agent Travel Planner")
st.markdown("*Powered by Flight Agent, Weather Agent, and Travel Agent*")

# Sidebar for inputs
with st.sidebar:
    st.header("📋 Trip Details")
    
    origin = st.text_input("🛫 From:", "San Francisco")
    destination = st.text_input("📍 To:", "Barcelona")
    
    col1, col2 = st.columns(2)
    with col1:
        departure_date = st.date_input("Departure:", datetime.now() + timedelta(days=30))
    with col2:
        return_date = st.date_input("Return:", datetime.now() + timedelta(days=37))
    
    days = (return_date - departure_date).days
    st.write(f"**Duration:** {days} days")
    
    passengers = st.number_input("👥 Travelers:", min_value=1, max_value=10, value=2)
    budget = st.number_input("💰 Budget per person ($):", min_value=100, max_value=10000, value=2000, step=100)
    interests = st.text_input("🎯 Interests:", "architecture, food, beaches")
    
    plan_button = st.button("🚀 Plan My Trip!", type="primary", use_container_width=True)

# Main content
if plan_button:
    with st.spinner("🤖 AI Agents are working together to plan your perfect trip..."):
        try:
            # Initialize orchestrator
            orchestrator = OrchestratorAgent()
            
            # Generate plan
            plan = orchestrator.plan_complete_trip(
                origin=origin,
                destination=destination,
                departure_date=str(departure_date),
                return_date=str(return_date),
                days=days,
                budget=budget,
                interests=interests,
                passengers=passengers
            )
            
            # Display results
            st.success("✅ Your trip is planned!")
            
            # Show the complete plan
            st.markdown(plan)
            
            # Download button
            st.download_button(
                label="📥 Download Travel Plan",
                data=plan,
                file_name=f"travel_plan_{destination}_{departure_date}.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.write("Check your API keys in .env file")

else:
    # Welcome message
    st.info("👈 Fill in your trip details and click **Plan My Trip!**")
    
    st.markdown("---")
    
    st.subheader("🤖 Our AI Agents")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### ✈️ Flight Agent")
        st.write("Searches flights, compares prices, finds best deals")
    
    with col2:
        st.markdown("### 🌤️ Weather Agent")
        st.write("Forecasts weather, packing recommendations")
    
    with col3:
        st.markdown("### 🗺️ Travel Agent")
        st.write("Creates day-by-day itineraries with activities")