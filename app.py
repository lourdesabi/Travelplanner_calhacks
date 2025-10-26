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

# Theme definitions
THEMES = {
    "Purple Gradient": {
        "bg": "linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe)",
        "primary": "#667eea",
        "secondary": "#764ba2",
        "accent": "#f093fb"
    },
    "Ocean Blue": {
        "bg": "linear-gradient(-45deg, #00d2ff, #3a7bd5, #667eea, #928DAB)",
        "primary": "#00d2ff",
        "secondary": "#3a7bd5",
        "accent": "#667eea"
    },
    "Sunset Orange": {
        "bg": "linear-gradient(-45deg, #ff6b6b, #ff8e53, #f093fb, #f5576c)",
        "primary": "#ff6b6b",
        "secondary": "#ff8e53",
        "accent": "#f093fb"
    },
    "Forest Green": {
        "bg": "linear-gradient(-45deg, #11998e, #38ef7d, #0F2027, #71B280)",
        "primary": "#11998e",
        "secondary": "#38ef7d",
        "accent": "#134E5E"
    },
    "Pink Dreams": {
        "bg": "linear-gradient(-45deg, #f093fb, #f5576c, #4facfe, #00f2fe)",
        "primary": "#f093fb",
        "secondary": "#f5576c",
        "accent": "#4facfe"
    },
    "Midnight Dark": {
        "bg": "linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29)",
        "primary": "#302b63",
        "secondary": "#24243e",
        "accent": "#0f0c29"
    }
}

# Sidebar for customization and inputs
with st.sidebar:
    # Theme Selector at the top
    st.markdown("### 🎨 Customize Appearance")
    selected_theme_name = st.selectbox(
        "Choose Theme",
        list(THEMES.keys()),
        index=list(THEMES.keys()).index(TeamConfig.DEFAULT_THEME)
    )
    selected_theme = THEMES[selected_theme_name]
    
    st.markdown("---")
    
    # Trip Planning Section
    st.markdown("## 🎯 Plan Your Journey")
    st.markdown("---")
    
    st.markdown("### 🛫 Flight Details")
    origin = st.text_input("✈️ From", "San Francisco", help="Departure city")
    destination = st.text_input("📍 To", "Barcelona", help="Destination city")
    
    st.markdown("### 📅 Travel Dates")
    col1, col2 = st.columns(2)
    with col1:
        departure_date = st.date_input(
            "🛫 Depart", 
            datetime.now() + timedelta(days=30)
        )
    with col2:
        return_date = st.date_input(
            "🛬 Return", 
            datetime.now() + timedelta(days=30 + TeamConfig.DEFAULT_DAYS)
        )
    
    days = (return_date - departure_date).days
    if days > 0:
        st.success(f"✨ **{days} day adventure**")
    else:
        st.error("⚠️ Return must be after departure")
    
    st.markdown("### 👥 Travel Party")
    passengers = st.number_input(
        "Number of Travelers", 
        min_value=1, 
        max_value=10, 
        value=TeamConfig.DEFAULT_PASSENGERS
    )
    
    st.markdown("### 💰 Budget")
    budget = st.slider(
        "Per Person ($)", 
        min_value=500, 
        max_value=10000, 
        value=TeamConfig.DEFAULT_BUDGET, 
        step=100
    )
    st.caption(f"Total Budget: ${budget * passengers:,}")
    
    st.markdown("### 🎨 Interests")
    interests = st.text_area(
        "What excites you?", 
        "architecture, food, beaches, culture",
        help="Separate with commas"
    )
    
    st.markdown("---")
    
    plan_button = st.button(
        "🚀 Create My Dream Trip", 
        type="primary", 
        use_container_width=True
    )

# Apply selected theme CSS
st.markdown(f"""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    * {{
        font-family: 'Poppins', sans-serif;
    }}
    
    /* Main background with animated gradient */
    .main {{
        background: {selected_theme['bg']};
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }}
    
    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, rgba(44, 62, 80, 0.95) 0%, rgba(52, 73, 94, 0.95) 100%);
        backdrop-filter: blur(10px);
    }}
    
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
        color: #fff;
        font-weight: 600;
    }}
    
    /* Card styling */
    .card {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    
    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.5);
    }}
    
    /* Animated title */
    .main-title {{
        font-size: 4rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #fff, #f0f0f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeInDown 1s ease;
        text-shadow: 2px 2px 20px rgba(0,0,0,0.3);
    }}
    
    @keyframes fadeInDown {{
        from {{
            opacity: 0;
            transform: translateY(-30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .subtitle {{
        text-align: center;
        color: #fff;
        font-size: 1.3rem;
        font-weight: 300;
        margin-top: -20px;
        animation: fadeIn 1.5s ease;
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    
    /* Modern button styling with theme colors */
    .stButton>button {{
        background: linear-gradient(135deg, {selected_theme['primary']} 0%, {selected_theme['secondary']} 100%);
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
        border-radius: 50px;
        padding: 15px 40px;
        border: none;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        transition: all 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    .stButton>button:hover {{
        background: linear-gradient(135deg, {selected_theme['secondary']} 0%, {selected_theme['primary']} 100%);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
        transform: translateY(-3px);
    }}
    
    .stButton>button:active {{
        transform: translateY(-1px);
    }}
    
    /* Input styling */
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stNumberInput>div>div>input {{
        background: rgba(255, 255, 255, 0.9);
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 12px;
        font-size: 1rem;
        transition: all 0.3s ease;
    }}
    
    .stTextInput>div>div>input:focus, .stSelectbox>div>div>select:focus {{
        border-color: {selected_theme['primary']};
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
    }}
    
    /* Date input styling */
    .stDateInput>div>div>input {{
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 10px;
    }}
    
    /* Slider styling with theme colors */
    .stSlider>div>div>div>div {{
        background: linear-gradient(90deg, {selected_theme['primary']} 0%, {selected_theme['secondary']} 100%);
    }}
    
    /* Success message */
    .stSuccess {{
        background: rgba(0, 255, 150, 0.1);
        border-radius: 15px;
        border-left: 5px solid #00ff96;
        padding: 20px;
        animation: slideInLeft 0.5s ease;
    }}
    
    @keyframes slideInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-50px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    /* Feature cards */
    .feature-card {{
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        height: 100%;
    }}
    
    .feature-card:hover {{
        background: rgba(255, 255, 255, 0.25);
        transform: scale(1.05);
    }}
    
    .feature-card h3 {{
        color: #fff;
        font-size: 2rem;
        margin-bottom: 15px;
    }}
    
    .feature-card p {{
        color: #f0f0f0;
        font-size: 1rem;
        line-height: 1.6;
    }}
    
    /* Metric cards */
    [data-testid="stMetricValue"] {{
        font-size: 2rem;
        font-weight: 700;
        color: #fff;
    }}
    
    [data-testid="stMetricLabel"] {{
        font-size: 1rem;
        color: #f0f0f0;
    }}
    
    /* Tab styling with theme colors */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 10px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 10px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        color: #fff;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, {selected_theme['primary']} 0%, {selected_theme['secondary']} 100%);
    }}
    
    /* Progress bar with theme colors */
    .stProgress>div>div>div>div {{
        background: linear-gradient(90deg, {selected_theme['primary']} 0%, {selected_theme['secondary']} 100%);
    }}
    
    /* Info box */
    .stInfo {{
        background: rgba(102, 126, 234, 0.2);
        border-radius: 15px;
        border-left: 5px solid {selected_theme['primary']};
        animation: fadeIn 0.5s ease;
    }}
    
    /* Download button special styling */
    .stDownloadButton>button {{
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        font-weight: 600;
        border-radius: 15px;
        padding: 12px 30px;
        border: none;
        box-shadow: 0 8px 25px rgba(17, 153, 142, 0.3);
        transition: all 0.3s ease;
    }}
    
    .stDownloadButton>button:hover {{
        background: linear-gradient(135deg, #38ef7d 0%, #11998e 100%);
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(17, 153, 142, 0.5);
    }}
    
    /* Expander styling */
    .streamlit-expanderHeader {{
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        color: #fff;
        font-weight: 600;
    }}
    
    /* Hide streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Pulse animation for icons */
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.1); }}
    }}
    
    .pulse-icon {{
        display: inline-block;
        animation: pulse 2s infinite;
    }}
</style>
""", unsafe_allow_html=True)

# Animated Header
st.markdown(f'<h1 class="main-title">✈️ {TeamConfig.APP_NAME}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="subtitle">{TeamConfig.TAGLINE}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align: center; color: rgba(255,255,255,0.7); font-size: 1rem;">by {TeamConfig.TEAM_NAME}</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main content
if plan_button:
    if days <= 0:
        st.error("❌ Please select valid dates!")
    else:
        # Animated progress
        progress_container = st.container()
        with progress_container:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                status_text.markdown("### 🤖 **Initializing AI Agents...**")
                progress_bar.progress(15)
                
                orchestrator = OrchestratorAgent()
                
                status_text.markdown("### 🔗 **Links Agent generating booking URLs...**")
                progress_bar.progress(30)
                
                status_text.markdown("### ✈️ **Flight Agent searching best deals...**")
                progress_bar.progress(50)
                
                status_text.markdown("### 🌤️ **Weather Agent checking forecasts...**")
                progress_bar.progress(70)
                
                status_text.markdown("### 🗺️ **Travel Agent crafting itinerary...**")
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
                
                # Success celebration
                st.balloons()
                st.success(f"✨ Your {days}-day journey to **{destination}** is ready!")
                
                # Results in modern tabs
                tabs = ["📋 Complete Plan", "📊 Trip Summary"]
                if TeamConfig.SHOW_BOOKING_LINKS:
                    tabs.append("🔗 Quick Links")
                tabs.append("📥 Download")
                
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
                            st.metric("🛫 From", origin)
                        with col2:
                            st.metric("📍 To", destination)
                        with col3:
                            st.metric("⏱️ Duration", f"{days} days")
                        with col4:
                            st.metric("💰 Total Budget", f"${budget * passengers:,}")
                        
                        st.markdown("---")
                        
                        col5, col6 = st.columns(2)
                        with col5:
                            st.metric("👥 Travelers", passengers)
                        with col6:
                            st.metric("💵 Per Person", f"${budget:,}")
                    st.markdown('</div>', unsafe_allow_html=True)
                
                tab_index = 2
                if TeamConfig.SHOW_BOOKING_LINKS:
                    with tab_objects[tab_index]:
                        st.markdown('<div class="card">', unsafe_allow_html=True)
                        st.markdown("### 🔗 Direct Booking Links")
                        st.info("💡 Click these links to compare prices and book directly!")
                        
                        st.markdown("#### ✈️ Flights")
                        st.markdown(f"- [Google Flights](https://www.google.com/travel/flights?q=flights+from+{origin}+to+{destination})")
                        st.markdown("- [Kayak](https://www.kayak.com)")
                        st.markdown("- [Skyscanner](https://www.skyscanner.com)")
                        
                        st.markdown("#### 🏨 Hotels")
                        st.markdown("- [Booking.com](https://www.booking.com)")
                        st.markdown("- [Hotels.com](https://www.hotels.com)")
                        st.markdown("- [Airbnb](https://www.airbnb.com)")
                        st.markdown('</div>', unsafe_allow_html=True)
                    tab_index += 1
                
                with tab_objects[tab_index]:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown("### 📥 Download Your Travel Plan")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="📄 Download as TXT",
                            data=plan,
                            file_name=f"{TeamConfig.APP_NAME.replace(' ', '_')}_{destination}_{departure_date}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    with col2:
                        st.download_button(
                            label="📋 Download as Markdown",
                            data=plan,
                            file_name=f"{TeamConfig.APP_NAME.replace(' ', '_')}_{destination}_{departure_date}.md",
                            mime="text/markdown",
                            use_container_width=True
                        )
                    
                    st.markdown("---")
                    st.info("💡 **Tip:** Share this plan with your travel companions and start booking!")
                    st.markdown('</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Oops! Something went wrong: {str(e)}")
                st.info("💡 Check your API keys in .env")
                with st.expander("🔍 Error Details"):
                    st.code(str(e))

else:
    # Welcome screen with feature cards
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.info("👈 **Fill in your travel details and let AI create your perfect itinerary!**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature showcase
    st.markdown("## 🤖 Our AI-Powered Agents")
    
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
    st.markdown("## 🎯 How It Works")
    
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
<p style='text-align: center; color: rgba(255,255,255,0.6); font-size: 0.9rem;'>
    Made with ❤️ by {TeamConfig.TEAM_NAME} | Powered by Multi-Agent AI
</p>
""", unsafe_allow_html=True)