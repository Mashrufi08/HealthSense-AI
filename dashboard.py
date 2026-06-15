import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def show_dashboard():
    st.markdown("""
    <div class="main-header">
        <h1>📊 Health Dashboard</h1>
        <p>Visual analytics and insights about your health</p>
    </div>
    """, unsafe_allow_html=True)

    if 'results' not in st.session_state:
        st.warning("⚠️ Please complete the Health Assessment first!")
        return

    r = st.session_state['results']

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Heart Risk", r['risk'])
    col2.metric("Risk Score", f"{r['risk_score']}%")
    col3.metric("Cholesterol", r['chol'])
    col4.metric("Blood Pressure", r['trestbps'])

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("❤️ Heart Risk Gauge")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=r['risk_score'],
            title={'text': "Risk Score (%)"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#1a6fd4"},
                'steps': [
                    {'range': [0, 40], 'color': "lightgreen"},
                    {'range': [40, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "red"}
                ]
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🥧 Risk Distribution")
        labels = ['Low Risk', 'High Risk']
        values = [100 - r['risk_score'], r['risk_score']]
        fig2 = px.pie(
            values=values, names=labels,
            color_discrete_sequence=['#4CAF50', '#e74c3c']
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")
    st.subheader("📈 Health Metrics Overview")
    categories = ['Blood Pressure', 'Cholesterol', 'Heart Rate', 'Age Factor']
    values = [
        min(r['trestbps']/200*100, 100),
        min(r['chol']/400*100, 100),
        min(r['thalach']/220*100, 100),
        min(r['age']/80*100, 100)
    ]
    fig3 = go.Figure(go.Bar(
        x=categories, y=values,
        marker_color=['red' if v > 70 else 'orange' if v > 40 else 'green' for v in values]
    ))
    fig3.update_layout(yaxis_title="Risk Level (%)", title="Key Health Metrics")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("🕸️ Health Profile Radar")
    fig4 = go.Figure(go.Scatterpolar(
        r=values, theta=categories,
        fill='toself', line_color='#1a6fd4'
    ))
    fig4.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])))
    st.plotly_chart(fig4, use_container_width=True)