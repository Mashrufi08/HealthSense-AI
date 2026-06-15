import streamlit as st

def show_assistant():
    st.markdown("""
    <div class="main-header">
        <h1>💬 AI Health Assistant</h1>
        <p>Ask me anything about your health results or general wellness</p>
    </div>
    """, unsafe_allow_html=True)

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    def get_response(question):
        q = question.lower()
        if 'hello' in q or 'hi' in q:
            return "👋 Hello! I'm your AI Health Assistant. Ask me anything about your health!"
        elif 'cholesterol' in q:
            return "🩸 High cholesterol increases heart disease risk. Keep it below 200 mg/dl through a healthy diet, regular exercise, and avoiding saturated fats."
        elif 'blood pressure' in q:
            return "💉 Normal blood pressure is 120/80 mmHg. High BP increases heart disease and stroke risk. Reduce salt, exercise regularly, and manage stress."
        elif 'heart' in q:
            return "❤️ Heart disease risk can be reduced by exercising regularly, eating healthy, avoiding smoking, and managing stress."
        elif 'diet' in q or 'food' in q:
            return "🥗 Eat more fruits, vegetables, whole grains and lean proteins. Avoid processed, fried and sugary foods."
        elif 'exercise' in q:
            return "🏃 Aim for 30 minutes of moderate exercise 5 days a week. Walking, cycling and swimming are great for heart health!"
        elif 'sleep' in q:
            return "😴 Adults need 7-9 hours of sleep daily. Poor sleep increases risk of heart disease, obesity and diabetes."
        elif 'stress' in q:
            return "🧘 Chronic stress raises blood pressure. Try meditation, deep breathing, yoga or talking to someone you trust."
        elif 'risk' in q:
            if 'results' in st.session_state:
                r = st.session_state['results']
                return f"Based on your assessment, your heart risk is **{r['risk']}** with a score of **{r['risk_score']}%**. {'Please consult a doctor!' if r['risk'] == 'High' else 'Keep maintaining your healthy lifestyle!'}"
            return "Please complete the Health Assessment first to see your risk results!"
        elif 'water' in q:
            return "💧 Drink at least 2-3 litres of water daily. Staying hydrated supports heart health and overall wellbeing."
        else:
            return "🏥 I can help with questions about cholesterol, blood pressure, diet, exercise, sleep, stress and heart health. What would you like to know?"

    st.subheader("💡 Quick Questions")
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("❤️ Heart health?"):
        st.session_state['chat_history'].append({'role': 'user', 'message': 'heart health tips'})
        st.session_state['chat_history'].append({'role': 'assistant', 'message': get_response('heart')})
        st.rerun()
    if col2.button("🥗 Diet tips?"):
        st.session_state['chat_history'].append({'role': 'user', 'message': 'diet tips'})
        st.session_state['chat_history'].append({'role': 'assistant', 'message': get_response('diet')})
        st.rerun()
    if col3.button("🏃 Exercise tips?"):
        st.session_state['chat_history'].append({'role': 'user', 'message': 'exercise tips'})
        st.session_state['chat_history'].append({'role': 'assistant', 'message': get_response('exercise')})
        st.rerun()
    if col4.button("😴 Sleep tips?"):
        st.session_state['chat_history'].append({'role': 'user', 'message': 'sleep tips'})
        st.session_state['chat_history'].append({'role': 'assistant', 'message': get_response('sleep')})
        st.rerun()

    st.markdown("---")
    for chat in st.session_state['chat_history']:
        if chat['role'] == 'user':
            st.chat_message("user").write(chat['message'])
        else:
            st.chat_message("assistant").write(chat['message'])

    user_input = st.chat_input("Ask a health question...")
    if user_input:
        st.session_state['chat_history'].append({'role': 'user', 'message': user_input})
        response = get_response(user_input)
        st.session_state['chat_history'].append({'role': 'assistant', 'message': response})
        st.rerun()