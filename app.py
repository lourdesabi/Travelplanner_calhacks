import streamlit as st
import sys
sys.path.append('agents')

from orchestrator import OrchestratorAgent
from team_config import TeamConfig
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title=TeamConfig.APP_NAME,
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for inputs
with st.sidebar:
    st.markdown("## Plan Your Journey")
    st.markdown("---")
    
    st.markdown("### Flight Details")
    origin = st.text_input("From", "San Francisco", help="Departure city")
    destination = st.text_input("To", "Barcelona", help="Destination city")
    
    st.markdown("### Travel Dates")
    col1, col2 = st.columns(2)
    with col1:
        departure_date = st.date_input(
            "Depart", 
            datetime.now() + timedelta(days=30)
        )
    with col2:
        return_date = st.date_input(
            "Return", 
            datetime.now() + timedelta(days=30 + TeamConfig.DEFAULT_DAYS)
        )
    
    days = (return_date - departure_date).days
    if days > 0:
        st.success(f"**{days} day trip**")
    else:
        st.error("Return must be after departure")
    
    st.markdown("### Travel Party")
    passengers = st.number_input(
        "Number of Travelers", 
        min_value=1, 
        max_value=10, 
        value=TeamConfig.DEFAULT_PASSENGERS
    )
    
    st.markdown("### Budget")
    budget = st.slider(
        "Per Person ($)", 
        min_value=500, 
        max_value=10000, 
        value=TeamConfig.DEFAULT_BUDGET, 
        step=100
    )
    st.caption(f"Total Budget: ${budget * passengers:,}")
    
    st.markdown("### Interests")
    interests = st.text_area(
        "What excites you?", 
        "architecture, food, beaches, culture",
        help="Separate with commas"
    )
    
    st.markdown("---")
    
    plan_button = st.button(
        "Create My Trip", 
        type="primary", 
        use_container_width=True
    )

# Apply clean modern professional theme
st.markdown("""
<style>
    /* Import Modern Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* ===== GLOBAL STYLES ===== */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main Background - Clean White/Beige */
    .main {
        background: linear-gradient(135deg, #FAFAFA 0%, #F5F1E8 100%);
        background-attachment: fixed;
    }
    
    /* ===== SIDEBAR STYLING ===== */
    [data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 2px solid #E0E0E0;
    }
    
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #2C3E50;
        font-weight: 600;
        letter-spacing: -0.5px;
    }
    
    /* Input Boxes - Sharp Clean Design */
    .stTextInput > div > div > input,
    .stTextArea textarea,
    .stSelectbox > div > div,
    .stNumberInput > div > div > input {
        background: #FFFFFF !important;
        border: 2px solid #D1D5DB !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        font-size: 15px !important;
        color: #1F2937 !important;
        transition: all 0.2s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea textarea:focus,
    .stSelectbox > div > div:focus-within,
    .stNumberInput > div > div > input:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
        outline: none !important;
    }
    
    /* Date Input Boxes */
    .stDateInput > div > div > input {
        background: #FFFFFF !important;
        border: 2px solid #D1D5DB !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        color: #1F2937 !important;
    }
    
    /* Number Input Boxes */
    .stNumberInput > div > div > input {
        background: #FFFFFF !important;
        border: 2px solid #D1D5DB !important;
        border-radius: 8px !important;
    }
    
    /* Slider Styling */
    .stSlider > div > div > div {
        background: #E5E7EB !important;
    }
    
    .stSlider > div > div > div > div {
        background: #3B82F6 !important;
    }
    
    /* ===== CARD STYLING - Sharp Professional Boxes ===== */
    .card {
        background: #FFFFFF;
        border: 2px solid #E5E7EB;
        border-radius: 12px;
        padding: 32px;
        margin: 24px 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        transition: all 0.2s ease;
    }
    
    .card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border-color: #D1D5DB;
    }
    
    /* ===== HEADER STYLING ===== */
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        color: #1F2937;
        margin-bottom: 12px;
        letter-spacing: -1.5px;
    }
    
    .subtitle {
        text-align: center;
        color: #6B7280;
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 8px;
    }
    
    /* ===== BUTTON STYLING ===== */
    .stButton > button {
        background: #3B82F6;
        color: #FFFFFF;
        font-weight: 600;
        font-size: 16px;
        border-radius: 10px;
        padding: 14px 32px;
        border: none;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
        transition: all 0.2s ease;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:hover {
        background: #2563EB;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
        transform: translateY(-1px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* ===== FEATURE CARDS ===== */
    .feature-card {
        background: #FFFFFF;
        border: 2px solid #E5E7EB;
        border-radius: 12px;
        padding: 28px 24px;
        text-align: center;
        transition: all 0.2s ease;
        height: 100%;
    }
    
    .feature-card:hover {
        border-color: #3B82F6;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
        transform: translateY(-2px);
    }
    
    .feature-card h3 {
        font-size: 2.5rem;
        margin-bottom: 8px;
    }
    
    .feature-card h4 {
        color: #1F2937;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
    
    .feature-card p {
        color: #6B7280;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    /* ===== TABS STYLING ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent;
        border-bottom: 2px solid #E5E7EB;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #FFFFFF;
        border: 2px solid #E5E7EB;
        border-radius: 8px 8px 0 0;
        padding: 12px 24px;
        color: #6B7280;
        font-weight: 500;
        border-bottom: none;
    }
    
    .stTabs [aria-selected="true"] {
        background: #3B82F6;
        border-color: #3B82F6;
        color: #FFFFFF;
    }
    
    /* ===== METRICS STYLING ===== */
    [data-testid="stMetricValue"] {
        color: #1F2937;
        font-weight: 600;
        font-size: 1.5rem;
    }
    
    [data-testid="stMetricLabel"] {
        color: #6B7280;
        font-weight: 500;
        font-size: 0.95rem;
    }
    
    /* ===== INFO/SUCCESS/ERROR BOXES ===== */
    .stAlert {
        background: #FFFFFF;
        border: 2px solid #E5E7EB;
        border-radius: 10px;
        padding: 16px 20px;
    }
    
    /* Success */
    .stSuccess {
        border-left: 4px solid #10B981;
        background: #F0FDF4;
    }
    
    /* Error */
    .stError {
        border-left: 4px solid #EF4444;
        background: #FEF2F2;
    }
    
    /* Info */
    .stInfo {
        border-left: 4px solid #3B82F6;
        background: #EFF6FF;
    }
    
    /* ===== PROGRESS BAR ===== */
    .stProgress > div > div > div > div {
        background: #3B82F6;
    }
    
    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        background: #FFFFFF;
        border: 2px solid #E5E7EB;
        border-radius: 10px;
        padding: 12px 16px;
        font-weight: 500;
        color: #1F2937;
    }
    
    /* ===== DOWNLOAD BUTTON ===== */
    .stDownloadButton > button {
        background: #10B981;
        color: #FFFFFF;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
        transition: all 0.2s ease;
    }
    
    .stDownloadButton > button:hover {
        background: #059669;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
        transform: translateY(-1px);
    }
    
    /* ===== MARKDOWN TEXT ===== */
    .main h1, .main h2, .main h3 {
        color: #1F2937;
        font-weight: 600;
        letter-spacing: -0.5px;
    }
    
    .main p {
        color: #4B5563;
        line-height: 1.7;
    }
    
    /* ===== DIVIDER ===== */
    hr {
        border: none;
        border-top: 2px solid #E5E7EB;
        margin: 24px 0;
    }
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #F3F4F6;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #D1D5DB;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #9CA3AF;
    }
    
    /* ===== SELECT BOX DROPDOWN ===== */
    [data-baseweb="select"] {
        background: #FFFFFF !important;
    }
    
    /* ===== CAPTION TEXT ===== */
    .stCaptionContainer {
        color: #6B7280;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<h1 class="main-title">{TeamConfig.APP_NAME}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="subtitle">{TeamConfig.TAGLINE}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align: center; color: #6B7280; font-size: 1rem;">by {TeamConfig.TEAM_NAME}</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main content
if plan_button:
    if days <= 0:
        st.error("Please select valid dates!")
    else:
        # Progress
        progress_container = st.container()
        with progress_container:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                status_text.markdown("### Initializing AI Agents...")
                progress_bar.progress(15)
                
                orchestrator = OrchestratorAgent()
                
                status_text.markdown("### Links Agent generating booking URLs...")
                progress_bar.progress(30)
                
                status_text.markdown("### Flight Agent searching best deals...")
                progress_bar.progress(50)
                
                status_text.markdown("### Weather Agent checking forecasts...")
                progress_bar.progress(70)
                
                status_text.markdown("### Travel Agent crafting itinerary...")
                progress_bar.progress(90)
                
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
                
                progress_bar.progress(100)
                status_text.empty()
                progress_bar.empty()
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Success
                st.balloons()
                st.success(f"Your {days}-day journey to **{destination}** is ready!")
                
                # Results in tabs
                tabs = ["Complete Plan", "Trip Summary"]
                if TeamConfig.SHOW_BOOKING_LINKS:
                    tabs.append("Quick Links")
                tabs.append("Download")
                
                tab_objects = st.tabs(tabs)
                
                with tab_objects[0]:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown(plan)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with tab_objects[1]:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    if TeamConfig.SHOW_METRICS:
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("From", origin)
                        with col2:
                            st.metric("To", destination)
                        with col3:
                            st.metric("Duration", f"{days} days")
                        with col4:
                            st.metric("Total Budget", f"${budget * passengers:,}")
                        
                        st.markdown("---")
                        
                        col5, col6 = st.columns(2)
                        with col5:
                            st.metric("Travelers", passengers)
                        with col6:
                            st.metric("Per Person", f"${budget:,}")
                    st.markdown('</div>', unsafe_allow_html=True)
                
                tab_index = 2
                if TeamConfig.SHOW_BOOKING_LINKS:
                    with tab_objects[tab_index]:
                        st.markdown('<div class="card">', unsafe_allow_html=True)
                        st.markdown("### Direct Booking Links")
                        st.info("Click these links to compare prices and book directly")
                        
                        st.markdown("#### Flights")
                        st.markdown(f"- [Google Flights](https://www.google.com/travel/flights?q=flights+from+{origin}+to+{destination})")
                        st.markdown("- [Kayak](https://www.kayak.com)")
                        st.markdown("- [Skyscanner](https://www.skyscanner.com)")
                        
                        st.markdown("#### Hotels")
                        st.markdown("- [Booking.com](https://www.booking.com)")
                        st.markdown("- [Hotels.com](https://www.hotels.com)")
                        st.markdown("- [Airbnb](https://www.airbnb.com)")
                        st.markdown('</div>', unsafe_allow_html=True)
                    tab_index += 1
                
                with tab_objects[tab_index]:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown("### Download Your Travel Plan")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="Download as TXT",
                            data=plan,
                            file_name=f"{TeamConfig.APP_NAME.replace(' ', '_')}_{destination}_{departure_date}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    with col2:
                        st.download_button(
                            label="Download as Markdown",
                            data=plan,
                            file_name=f"{TeamConfig.APP_NAME.replace(' ', '_')}_{destination}_{departure_date}.md",
                            mime="text/markdown",
                            use_container_width=True
                        )
                    
                    st.markdown("---")
                    st.info("**Tip:** Share this plan with your travel companions and start booking!")
                    st.markdown('</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Oops! Something went wrong: {str(e)}")
                st.info("Check your API keys in .env")
                with st.expander("Error Details"):
                    st.code(str(e))

else:
    # Welcome screen
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.info("**Fill in your travel details in the sidebar and let AI create your perfect itinerary!**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature showcase
    st.markdown("## Our AI-Powered Agents")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🔗</h3>
            <h4>Links Agent</h4>
            <p>Direct booking links to flights, hotels, and activities</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>✈️</h3>
            <h4>Flight Agent</h4>
            <p>Best flight options with prices and insider tips</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🌤️</h3>
            <h4>Weather Agent</h4>
            <p>Real-time forecasts and packing recommendations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <h3>🗺️</h3>
            <h4>Travel Agent</h4>
            <p>Personalized day-by-day itineraries</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # How it works
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## How It Works")
    
    steps = st.columns(4)
    
    with steps[0]:
        st.markdown("### 1️⃣")
        st.markdown("**Input Details**")
        st.caption("Enter your travel preferences")
    
    with steps[1]:
        st.markdown("### 2️⃣")
        st.markdown("**AI Analysis**")
        st.caption("4 agents collaborate")
    
    with steps[2]:
        st.markdown("### 3️⃣")
        st.markdown("**Generate Plan**")
        st.caption("Custom itinerary created")
    
    with steps[3]:
        st.markdown("### 4️⃣")
        st.markdown("**Book & Travel**")
        st.caption("Download and enjoy!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(f"""
<p style='text-align: center; color: #6B7280; font-size: 0.9rem;'>
    Made with care by {TeamConfig.TEAM_NAME} | Powered by Multi-Agent AI
</p>
""", unsafe_allow_html=True)