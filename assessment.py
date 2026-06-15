import streamlit as st
import numpy as np
import joblib

def show_assessment():
    st.markdown("""
    <div class="main-header">
        <h1>📋 Health Assessment</h1>
        <p>Fill in your health details below. Our AI will analyze your heart disease risk.</p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("⚠️ This tool is for awareness only — not a substitute for professional medical advice.")
    st.markdown("---")

    model = joblib.load('heart_model.pkl')

    st.subheader("❤️ Physical Health Details")

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 20, 80, 35)
        trestbps = st.slider("Blood Pressure (mm Hg)", 80, 200, 120)
        chol = st.slider("Cholesterol (mg/dl)", 100, 400, 200)
        thalch = st.slider("Max Heart Rate", 60, 220, 150)
        oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)
    with col2:
        sex = st.selectbox("Gender", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", ["No Pain", "Mild", "Moderate", "Severe"])
        fbs = st.selectbox("Fasting Blood Sugar > 120?", ["No", "Yes"])
        exang = st.selectbox("Exercise Induced Angina?", ["No", "Yes"])
        restecg = st.selectbox("Resting ECG", ["Normal", "Abnormal", "Hypertrophy"])

    col3, col4 = st.columns(2)
    with col3:
        slope = st.selectbox("Slope of ST Segment", ["Upsloping", "Flat", "Downsloping"])
        ca = st.selectbox("Major Vessels (0-3)", [0, 1, 2, 3])
    with col4:
        thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

    sex_val = 1 if sex == "Male" else 0
    cp_val = ["No Pain", "Mild", "Moderate", "Severe"].index(cp)
    fbs_val = 1 if fbs == "Yes" else 0
    exang_val = 1 if exang == "Yes" else 0
    restecg_val = ["Normal", "Abnormal", "Hypertrophy"].index(restecg)
    slope_val = ["Upsloping", "Flat", "Downsloping"].index(slope)
    thal_val = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal) + 1

    st.markdown("---")

    if st.button("🔍 Analyse My Health", use_container_width=True):
        features = np.array([[age, sex_val, cp_val, trestbps, chol,
                              fbs_val, restecg_val, thalch, exang_val,
                              oldpeak, slope_val, ca, thal_val]])

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]
        risk_score = round(max(probability) * 100, 1)
        risk = "High" if prediction == 1 else "Low"

        st.session_state['results'] = {
            'age': age, 'sex': sex, 'chol': chol,
            'trestbps': trestbps, 'thalach': thalch,
            'risk': risk, 'risk_score': risk_score,
            'prediction': prediction
        }

        st.markdown("---")
        st.subheader("🎯 Your AI Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Heart Risk", risk)
        col2.metric("Risk Score", f"{risk_score}%")
        col3.metric("Age", age)

        if risk == "High":
            st.error("⚠️ High risk detected! Please consult a doctor.")
        else:
            st.success("✅ Low risk. Keep maintaining your health!")

        st.info("📊 Go to **Dashboard** for detailed charts and **Action Plan** for recommendations!")