import streamlit as st

def show_action_plan():
    st.markdown("""
    <div class="main-header">
        <h1>📅 Personalized Action Plan</h1>
        <p>Your customized 7-day health improvement plan</p>
    </div>
    """, unsafe_allow_html=True)

    if 'results' not in st.session_state:
        st.warning("⚠️ Please complete the Health Assessment first!")
        return

    r = st.session_state['results']
    risk = r['risk']

    if risk == "High":
        st.error(f"⚠️ Overall Status: High Risk | Score: {r['risk_score']}%")
    else:
        st.success(f"✅ Overall Status: Low Risk | Score: {r['risk_score']}%")

    st.markdown("---")
    st.subheader("🗓️ Your 7-Day Health Plan")

    if risk == "High":
        plan = {
            "Monday": "🚶 30 min morning walk + drink 8 glasses of water",
            "Tuesday": "🥗 Eat low cholesterol diet + avoid fried foods",
            "Wednesday": "😴 Sleep by 10pm + no screens 1 hour before bed",
            "Thursday": "🧘 Do 15 min meditation to reduce stress",
            "Friday": "🚴 30 min cycling or any physical activity",
            "Saturday": "👨‍⚕️ Research nearby cardiologist for checkup",
            "Sunday": "📖 Read about heart healthy lifestyle habits"
        }
    else:
        plan = {
            "Monday": "🚶 20 min morning walk + drink 8 glasses of water",
            "Tuesday": "🥗 Eat balanced diet with fruits and vegetables",
            "Wednesday": "😴 Sleep by 10:30pm + no screens 1 hour before bed",
            "Thursday": "🧘 Do 10 min meditation or deep breathing",
            "Friday": "🏃 Physical activity of your choice + call a friend",
            "Saturday": "🎯 Plan healthy meals for next week",
            "Sunday": "📖 Read about maintaining a healthy lifestyle"
        }

    for day, activity in plan.items():
        st.info(f"**{day}:** {activity}")

    st.markdown("---")
    st.subheader("💡 Key Health Recommendations")

    if r['chol'] > 200:
        st.warning("🔴 High Cholesterol — reduce saturated fats and eat more fiber")
    if r['trestbps'] > 130:
        st.warning("🔴 High Blood Pressure — reduce salt intake and exercise regularly")
    if r['thalach'] < 100:
        st.warning("🔴 Low Max Heart Rate — consult a doctor")

    st.success("✅ Keep up with regular health checkups and maintain a healthy lifestyle!")
    st.caption("⚠️ This is not a medical diagnosis. Always consult a doctor.")