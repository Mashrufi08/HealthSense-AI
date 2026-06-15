import streamlit as st

def show_home():
    st.markdown("""
    <div class="main-header">
        <h1>🏥 HealthSense AI</h1>
        <h3>AI-Powered Health Risk Analyzer</h3>
        <p>Powered by Machine Learning | SDG 3 — Good Health and Well-Being</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Welcome to **HealthSense AI** — an intelligent health assessment platform 
    powered by Machine Learning to help you understand your health risks early
    and take preventive action before conditions become serious.
    """)

    st.markdown("---")
    st.subheader("🚀 What Can HealthSense AI Do?")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h2>📋</h2>
            <h4>Health Assessment</h4>
            <p>AI-powered physical health risk analysis using your health data</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h2>📊</h2>
            <h4>Visual Dashboard</h4>
            <p>Charts and insights from your health data</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h2>💬</h2>
            <h4>AI Assistant</h4>
            <p>Ask health questions, get personalized answers</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="feature-card">
            <h2>📅</h2>
            <h4>Action Plan</h4>
            <p>Your personalized 7-day health improvement plan</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📊 How It Works")
    col1, col2, col3, col4 = st.columns(4)
    col1.info("1️⃣ **Fill** your health details")
    col2.info("2️⃣ **AI analyzes** your data")
    col3.info("3️⃣ **View** results & charts")
    col4.info("4️⃣ **Follow** your action plan")

    st.markdown("---")
    st.subheader("📈 Project Statistics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Model Accuracy", "85.87%")
    col2.metric("Dataset", "UCI Heart Disease")
    col3.metric("ML Algorithm", "Random Forest")
    col4.metric("SDG Goal", "Good Health")

    st.markdown("---")
    st.subheader("❓ Why Early Detection Matters")
    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ **Without Early Detection:**")
        st.write("• Diseases progress unnoticed")
        st.write("• Higher treatment costs")
        st.write("• Reduced quality of life")
        st.write("• Serious health complications")
    with col2:
        st.success("✅ **With HealthSense AI:**")
        st.write("• Early risk detection")
        st.write("• Personalized recommendations")
        st.write("• Preventive healthcare")
        st.write("• Better health outcomes")

    st.markdown("---")
    st.caption("⚠️ HealthSense AI is for awareness only — not a substitute for professional medical advice.")