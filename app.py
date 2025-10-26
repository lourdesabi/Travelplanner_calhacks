import streamlit as st
import sys
sys.path.append('agents')

from orchestrator import OrchestratorAgent
from team_config import TeamConfig
from team_config import TeamConfig
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title=TeamConfig.APP_NAME,
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)
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
    st.markdown("## Plan Your Journey")
    st.markdown("---")
    
    st.markdown("### Flight Details")
    origin = st.text_input("From", "San Francisco", help="Departure city")
    destination = st.text_input("To", "Barcelona", help="Destination city")
    st.markdown("### Flight Details")
    origin = st.text_input("From", "San Francisco", help="Departure city")
    destination = st.text_input("To", "Barcelona", help="Destination city")
    
    st.markdown("### Travel Dates")
    st.markdown("### Travel Dates")
    col1, col2 = st.columns(2)
    with col1:
        departure_date = st.date_input(
            "Departure", 
            datetime.now() + timedelta(days=30)
        )
    with col2:
        return_date = st.date_input(
            "Return", 
            datetime.now() + timedelta(days=30 + TeamConfig.DEFAULT_DAYS)
        )
        return_date = st.date_input(
            "Return", 
            datetime.now() + timedelta(days=30 + TeamConfig.DEFAULT_DAYS)
        )
    
    days = (return_date - departure_date).days
    if days > 0:
        st.success(f"{days} day adventure")
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
    st.caption(f"Total: ${budget * passengers:,}")
    
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

# Beautiful Natural Theme
st.markdown("""
<style>
    /* Import Elegant Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    /* ===== GLOBAL STYLES ===== */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main Background - Soft Natural Gradient */
    .main {
        background: linear-gradient(135deg, #F8F9FA 0%, #E8F5E9 30%, #E3F2FD 70%, #FFF8E1 100%);
        background-attachment: fixed;
    }
    
    /* ===== SIDEBAR - Elegant Design ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #F1F8F4 100%);
        border-right: 3px solid #C8E6C9;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.03);
    }
    
    [data-testid="stSidebar"] h2 {
        color: #2E7D32;
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 1.8rem;
        letter-spacing: -0.5px;
        margin-bottom: 20px;
    }
    
    [data-testid="stSidebar"] h3 {
        color: #388E3C;
        font-weight: 600;
        font-size: 1.1rem;
        margin-top: 24px;
        margin-bottom: 12px;
        letter-spacing: 0.3px;
    }
    
    /* ===== BEAUTIFUL INPUT BOXES - BIGGER & PRETTIER ===== */
    .stTextInput > div > div > input,
    .stTextArea textarea {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FFF9 100%) !important;
        border: 2.5px solid #A5D6A7 !important;
        border-radius: 16px !important;
        padding: 18px 24px !important;
        font-size: 16px !important;
        color: #1B5E20 !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.08) !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea textarea:focus {
        border-color: #66BB6A !important;
        box-shadow: 0 4px 16px rgba(76, 175, 80, 0.2), 0 0 0 4px rgba(102, 187, 106, 0.1) !important;
        outline: none !important;
        transform: translateY(-1px);
        background: #FFFFFF !important;
    }
    
    /* Text Area - Extra Height */
    .stTextArea textarea {
        min-height: 120px !important;
    }
    
    /* Date Inputs - Beautiful Design */
    .stDateInput > div > div > input {
        background: linear-gradient(135deg, #FFFFFF 0%, #E3F2FD 100%) !important;
        border: 2.5px solid #90CAF9 !important;
        border-radius: 14px !important;
        padding: 16px 20px !important;
        color: #0D47A1 !important;
        font-weight: 500 !important;
        font-size: 15px !important;
        box-shadow: 0 2px 8px rgba(33, 150, 243, 0.08) !important;
        transition: all 0.3s ease !important;
    }
    
    .stDateInput > div > div > input:focus {
        border-color: #42A5F5 !important;
        box-shadow: 0 4px 16px rgba(33, 150, 243, 0.2), 0 0 0 4px rgba(66, 165, 245, 0.1) !important;
    }
    
    /* Number Input - Bigger & Prettier */
    .stNumberInput > div > div > input {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF3E0 100%) !important;
        border: 2.5px solid #FFCC80 !important;
        border-radius: 14px !important;
        padding: 16px 20px !important;
        font-size: 16px !important;
        color: #E65100 !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 8px rgba(255, 152, 0, 0.08) !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #FFB74D !important;
        box-shadow: 0 4px 16px rgba(255, 152, 0, 0.2), 0 0 0 4px rgba(255, 183, 77, 0.1) !important;
    }
    
    /* Slider - Beautiful Green Theme */
    .stSlider {
        padding: 20px 0 !important;
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #C8E6C9 0%, #A5D6A7 100%) !important;
        height: 8px !important;
        border-radius: 10px !important;
    }
    
    .stSlider > div > div > div > div {
        background: linear-gradient(135deg, #66BB6A 0%, #4CAF50 100%) !important;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3) !important;
    }
    
    .stSlider > div > div > div > div > div {
        background: #FFFFFF !important;
        border: 3px solid #4CAF50 !important;
        width: 24px !important;
        height: 24px !important;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4) !important;
    }
    
    /* ===== ELEGANT CARDS ===== */
    .card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F9FFF9 100%);
        border: 2px solid #E8F5E9;
        border-radius: 20px;
        padding: 40px;
        margin: 28px 0;
        box-shadow: 0 8px 32px rgba(76, 175, 80, 0.08), 0 2px 8px rgba(0, 0, 0, 0.02);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 12px 48px rgba(76, 175, 80, 0.12), 0 4px 16px rgba(0, 0, 0, 0.04);
        border-color: #C8E6C9;
        transform: translateY(-2px);
    }
    
    /* ===== BEAUTIFUL HEADER ===== */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 4.5rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #2E7D32 0%, #388E3C 50%, #43A047 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 16px;
        letter-spacing: -2px;
        text-shadow: 0 2px 20px rgba(76, 175, 80, 0.1);
    }
    
    .subtitle {
        text-align: center;
        color: #558B2F;
        font-size: 1.4rem;
        font-weight: 400;
        margin-bottom: 12px;
        letter-spacing: 0.5px;
    }
    
    /* ===== STUNNING BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #66BB6A 0%, #4CAF50 50%, #388E3C 100%);
        color: #FFFFFF;
        font-weight: 600;
        font-size: 17px;
        border-radius: 14px;
        padding: 18px 40px;
        border: none;
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.35);
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
        text-transform: none;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #81C784 0%, #66BB6A 50%, #4CAF50 100%);
        box-shadow: 0 8px 28px rgba(76, 175, 80, 0.45);
        transform: translateY(-2px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* ===== FEATURE CARDS - ELEGANT ===== */
    .feature-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F1F8F4 100%);
        border: 2px solid #C8E6C9;
        border-radius: 20px;
        padding: 36px 28px;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
        box-shadow: 0 4px 16px rgba(76, 175, 80, 0.08);
    }
    
    .feature-card:hover {
        border-color: #81C784;
        box-shadow: 0 8px 32px rgba(76, 175, 80, 0.2);
        transform: translateY(-4px);
        background: linear-gradient(135deg, #FFFFFF 0%, #E8F5E9 100%);
    }
    
    .feature-card h3 {
        font-size: 3rem;
        margin-bottom: 16px;
        filter: drop-shadow(0 2px 4px rgba(76, 175, 80, 0.2));
    }
    
    .feature-card h4 {
        color: #2E7D32;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 12px;
        font-family: 'Playfair Display', serif;
    }
    
    .feature-card p {
        color: #558B2F;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* ===== BEAUTIFUL TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: transparent;
        border-bottom: 3px solid #E8F5E9;
        padding-bottom: 4px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #FFFFFF 0%, #F1F8F4 100%);
        border: 2px solid #C8E6C9;
        border-radius: 12px 12px 0 0;
        padding: 16px 32px;
        color: #388E3C;
        font-weight: 500;
        font-size: 15px;
        border-bottom: none;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #F1F8F4 0%, #E8F5E9 100%);
        border-color: #81C784;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #66BB6A 0%, #4CAF50 100%);
        border-color: #4CAF50;
        color: #FFFFFF;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
    }
    
    /* ===== METRICS - ELEGANT DISPLAY ===== */
    [data-testid="stMetricValue"] {
        color: #2E7D32;
        font-weight: 700;
        font-size: 2rem;
        font-family: 'Playfair Display', serif;
    }
    
    [data-testid="stMetricLabel"] {
        color: #558B2F;
        font-weight: 500;
        font-size: 1.05rem;
        letter-spacing: 0.3px;
    }
    
    /* ===== BEAUTIFUL ALERTS ===== */
    .stAlert {
        border-radius: 14px;
        padding: 20px 24px;
        border-width: 2px;
        border-style: solid;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #F1F8F4 0%, #E8F5E9 100%);
        border-color: #81C784;
        color: #2E7D32;
    }
    
    .stError {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%);
        border-color: #FFB74D;
        color: #E65100;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        border-color: #64B5F6;
        color: #0D47A1;
    }
    
    /* ===== PROGRESS BAR - BEAUTIFUL GREEN ===== */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #66BB6A 0%, #4CAF50 100%);
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
    }
    
    /* ===== DOWNLOAD BUTTON - ELEGANT ===== */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #42A5F5 0%, #1E88E5 100%);
        color: #FFFFFF;
        border: none;
        border-radius: 12px;
        padding: 16px 28px;
        font-weight: 600;
        font-size: 15px;
        box-shadow: 0 4px 16px rgba(33, 150, 243, 0.3);
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #64B5F6 0%, #42A5F5 100%);
        box-shadow: 0 6px 24px rgba(33, 150, 243, 0.4);
        transform: translateY(-2px);
    }
    
    /* ===== MARKDOWN OUTPUT - BEAUTIFUL FORMATTING ===== */
    .main h1 {
        color: #2E7D32;
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        letter-spacing: -1px;
        margin-top: 32px;
        margin-bottom: 20px;
        border-bottom: 3px solid #C8E6C9;
        padding-bottom: 12px;
    }
    
    .main h2 {
        color: #388E3C;
        font-family: 'Playfair Display', serif;
        font-weight: 600;
        letter-spacing: -0.5px;
        margin-top: 28px;
        margin-bottom: 16px;
    }
    
    .main h3 {
        color: #43A047;
        font-weight: 600;
        margin-top: 24px;
        margin-bottom: 12px;
    }
    
    .main p {
        color: #37474F;
        line-height: 1.8;
        font-size: 16px;
        margin-bottom: 16px;
    }
    
    .main ul, .main ol {
        color: #37474F;
        line-height: 1.8;
        margin-bottom: 16px;
    }
    
    .main li {
        margin-bottom: 8px;
    }
    
    .main strong {
        color: #2E7D32;
        font-weight: 600;
    }
    
    .main em {
        color: #558B2F;
    }
    
    .main code {
        background: #F1F8F4;
        color: #2E7D32;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 14px;
        border: 1px solid #C8E6C9;
    }
    
    /* ===== DIVIDER - ELEGANT ===== */
    hr {
        border: none;
        border-top: 2px solid #E8F5E9;
        margin: 32px 0;
    }
    
    /* ===== SCROLLBAR - NATURAL ===== */
    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #F1F8F4;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #81C784 0%, #66BB6A 100%);
        border-radius: 10px;
        border: 2px solid #F1F8F4;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #66BB6A 0%, #4CAF50 100%);
    }
    
    /* ===== CAPTION TEXT ===== */
    .stCaptionContainer {
        color: #558B2F;
        font-size: 0.95rem;
        font-weight: 500;
    }
    
    /* ===== SELECT BOX - BEAUTIFUL ===== */
    [data-baseweb="select"] > div {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FFF9 100%) !important;
        border: 2.5px solid #A5D6A7 !important;
        border-radius: 14px !important;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.08) !important;
    }
    
    /* ===== EXPANDER - NATURAL ===== */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #FFFFFF 0%, #F1F8F4 100%);
        border: 2px solid #C8E6C9;
        border-radius: 12px;
        padding: 16px 20px;
        font-weight: 500;
        color: #2E7D32;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: #81C784;
        background: linear-gradient(135deg, #F1F8F4 0%, #E8F5E9 100%);
    }
</style>
""", unsafe_allow_html=True)

# Beautiful Header
st.markdown(f'<h1 class="main-title">{TeamConfig.APP_NAME}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="subtitle">{TeamConfig.TAGLINE}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align: center; color: #558B2F; font-size: 1.05rem; font-weight: 500;">by {TeamConfig.TEAM_NAME}</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main content
if plan_button:
    if days <= 0:
        st.error("Please select valid dates")
    else:
        # Progress
        progress_container = st.container()
        with progress_container:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                status_text.markdown("### Initializing AI Agents")
                progress_bar.progress(15)
                
                orchestrator = OrchestratorAgent()
                
                status_text.markdown("### Generating booking links")
                progress_bar.progress(30)
                
                status_text.markdown("### Searching best flight deals")
                progress_bar.progress(50)
                
                status_text.markdown("### Checking weather forecasts")
                progress_bar.progress(70)
                
                status_text.markdown("### Crafting your perfect itinerary")
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
                st.success(f"Your {days}-day journey to {destination} is ready")
                
                # Results in tabs
                tabs = ["Complete Plan", "Trip Summary"]
                if TeamConfig.SHOW_BOOKING_LINKS:
                    tabs.append("Booking Links")
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
                            st.metric("Budget", f"${budget * passengers:,}")
                        
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
                        st.info("Compare prices and book directly through these trusted platforms")
                        
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
                            label="Download as Text",
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
                    st.info("Share this plan with your travel companions")
                    st.markdown('</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
                st.info("Check your API keys in .env file")
                with st.expander("Error Details"):
                    st.code(str(e))

else:
    # Welcome screen
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.info("Fill in your travel details in the sidebar and let AI create your perfect itinerary")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature showcase
    st.markdown("## AI-Powered Travel Planning")
    
    col1, col2, col3, col4 = st.columns(4)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🔗</h3>
            <h4>Smart Links</h4>
            <p>Direct booking links to the best flight and hotel platforms</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>✈️</h3>
            <h4>Flight Finder</h4>
            <p>Best flight options with prices and travel tips</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🌤️</h3>
            <h4>Weather Intel</h4>
            <p>Real-time forecasts and packing recommendations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <h3>🗺️</h3>
            <h4>Custom Itinerary</h4>
            <p>Personalized day-by-day travel plans</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # How it works
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("## How It Works")
    
    steps = st.columns(4)
    
    with steps[0]:
        st.markdown("### 1")
        st.markdown("**Input Details**")
        st.caption("Share your travel preferences")
    
    with steps[1]:
        st.markdown("### 2")
        st.markdown("**AI Analysis**")
        st.caption("Four agents collaborate")
    
    with steps[2]:
        st.markdown("### 3")
        st.markdown("**Generate Plan**")
        st.caption("Custom itinerary created")
    
    with steps[3]:
        st.markdown("### 4")
        st.markdown("**Book & Travel**")
        st.caption("Download and enjoy")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(f"""
<p style='text-align: center; color: #558B2F; font-size: 0.95rem; font-weight: 500;'>
    Created with care by {TeamConfig.TEAM_NAME} · Powered by Multi-Agent AI
</p>
""", unsafe_allow_html=True)
