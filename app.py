import streamlit as st

st.set_page_config(
    page_title="HealthSense AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    * { font-family: 'Inter', sans-serif; }

    .stApp {
        background: linear-gradient(135deg, #e8f4fd 0%, #dbeafe 50%, #eff6ff 100%);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f2d6e 0%, #1a4fa0 40%, #2563eb 100%);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    [data-testid="stSidebar"] .stRadio label {
        background: rgba(255,255,255,0.08);
        border-radius: 8px;
        padding: 6px 12px;
        margin: 2px 0;
        transition: all 0.2s;
    }
    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255,255,255,0.18);
    }

    /* Main header */
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #2563eb 50%, #3b82f6 100%);
        padding: 35px 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px rgba(37, 99, 235, 0.35);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .main-header h1 {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .main-header p {
        font-size: 1rem;
        opacity: 0.85;
        margin-top: 8px;
    }

    /* Feature cards */
    .feature-card {
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(10px);
        padding: 24px 20px;
        border-radius: 16px;
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-top: 4px solid #3b82f6;
        margin: 10px 0;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.1);
        text-align: center;
        transition: transform 0.2s;
    }
    .feature-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(37, 99, 235, 0.2);
    }
    .feature-card h4 {
        color: #1e40af;
        font-weight: 600;
    }
    .feature-card p {
        color: #64748b;
        font-size: 0.9rem;
    }

    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #2563eb, #60a5fa);
        padding: 20px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin: 5px;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
    }

    /* Result cards */
    .result-card {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        padding: 24px;
        border-radius: 16px;
        border: 1px solid rgba(59, 130, 246, 0.15);
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.08);
        margin: 10px 0;
    }

    /* Streamlit elements */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #3b82f6);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #2563eb);
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.4);
        transform: translateY(-1px);
    }

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.85);
        border-radius: 14px;
        padding: 16px;
        border: 1px solid rgba(59,130,246,0.2);
        box-shadow: 0 2px 12px rgba(37,99,235,0.08);
    }
    div[data-testid="stMetric"] label {
        color: #2563eb !important;
        font-weight: 600;
    }

    .stTextInput > div > input, .stTextArea > div > textarea {
        border-radius: 10px;
        border: 1.5px solid #93c5fd;
        background: rgba(255,255,255,0.9);
    }
    .stTextInput > div > input:focus, .stTextArea > div > textarea:focus {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37,99,235,0.15);
    }

    .stSelectbox > div, .stSlider {
        border-radius: 10px;
    }

    h1, h2, h3 { color: #1e40af; }
    h4, h5 { color: #2563eb; }
</style>
""", unsafe_allow_html=True)

from home import show_home
from assessment import show_assessment
from dashboard import show_dashboard
from assistant import show_assistant
from action_plan import show_action_plan

st.sidebar.markdown("# 🏥 HealthSense AI")
st.sidebar.markdown("### Your Personal Health Assistant")
st.sidebar.markdown("---")
st.sidebar.markdown("**SDG 3 — Good Health and Well-Being**")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "📋 Health Assessment",
    "📊 Dashboard",
    "💬 AI Assistant",
    "📅 Action Plan"
])

st.sidebar.markdown("---")
st.sidebar.markdown("**Model:** Random Forest")
st.sidebar.markdown("**Accuracy:** 85.87%")
st.sidebar.markdown("**Dataset:** Heart Disease UCI")
st.sidebar.markdown("⚠️ *Not a medical diagnosis*")

if page == "🏠 Home":
    show_home()
elif page == "📋 Health Assessment":
    show_assessment()
elif page == "📊 Dashboard":
    show_dashboard()
elif page == "💬 AI Assistant":
    show_assistant()
elif page == "📅 Action Plan":
    show_action_plan()