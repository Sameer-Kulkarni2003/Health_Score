import streamlit as st
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
    }
    h1 {
        color: #1E90FF;
        font-size: 36px;
    }
    h2 {
        color: #00FF7F;
        font-size: 26px;
    }
    .stSelectbox, .stTextInput, .stMultiSelect {
        background-color: #333333;
        color: white;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #1E90FF;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .predicted-score-box {
        background-color: #333333;
        color: #00FF7F;
        font-size: 20px;
        padding: 10px;
        border-radius: 10px;
    }
    .assessment-box {
        background-color: #FFA07A;
        color: black;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
    }
    .explanation-box {
        background-color: #00CED1;
        color: white;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.markdown(
    "<h1><img src='https://img.icons8.com/office/40/000000/medical-doctor.png'/> Medical Health Score Predictor</h1>",
    unsafe_allow_html=True,
)
st.write(
    "This application predicts your health risk score based on your general health information. Please fill in the details below."
)

# User input section
st.markdown("<h2>Provide Your Information</h2>", unsafe_allow_html=True)

gender = st.selectbox("Select Gender", ["Male", "Female"])
blood_group = st.selectbox(
    "Select Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
)
age = st.number_input("Enter Age", min_value=0, max_value=120, value=21)
height = st.number_input("Enter Height (cm)", min_value=50, max_value=250, value=180)
weight = st.number_input("Enter Weight (kg)", min_value=10, max_value=200, value=80)

symptoms = st.multiselect(
    "Select your symptoms",
    [
        "stomach ache",
        "sore throat",
        "headache",
        "nausea",
        "cough",
        "fever",
        "fatigue",
        "chest pain",
        "back pain",
        "joint pain",
        "rash",
        "shortness of breath",
        "dizziness",
        "vomiting",
        "diarrhea",
        "constipation",
        "muscle pain",
        "abdominal pain",
        "cold",
        "itching",
        "dry throat",
        "chills",
        "sweating",
        "loss of appetite",
    ],
)

past_conditions = st.multiselect(
    "Select any past medical conditions",
    [
        "asthma",
        "hypertension",
        "diabetes",
        "arthritis",
        "heart disease",
        "stroke",
        "cancer",
        "COPD",
        "chronic kidney disease",
        "liver disease",
        "alzheimer's disease",
        "parkinson's disease",
        "epilepsy",
        "anemia",
        "depression",
        "anxiety",
        "obesity",
        "osteoporosis",
        "multiple sclerosis",
        "None",
    ],
)

# Reason dictionaries for symptoms and past conditions
symptom_reasons = {
    "stomach ache": "could indicate gastrointestinal issues such as indigestion or ulcers.",
    # Add other symptoms and their explanations here...
}

condition_reasons = {
    "asthma": "causes chronic inflammation in the airways, leading to breathing difficulties.",
    # Add other conditions and their explanations here...
}

# Predict health risk score button
if st.button("Predict Health Score"):
    # Example prediction logic
    risk_score = np.random.uniform(0, 5)  # Dummy risk score

    # Display prediction result
    st.markdown(
        f"<div class='predicted-score-box'>Predicted Health Risk Score: {risk_score:.2f}</div>",
        unsafe_allow_html=True,
    )

    # Display assessment based on score
    if risk_score < 1.5:
        st.markdown(
            "<div class='assessment-box'>You are at low risk of health issues.</div>",
            unsafe_allow_html=True,
        )
    elif 1.5 <= risk_score < 3.5:
        st.markdown(
            "<div class='assessment-box'>You are at moderate risk of health issues. It might be advisable to consult a healthcare provider.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='assessment-box'>You are at high risk of health issues. Immediate medical attention is recommended!</div>",
            unsafe_allow_html=True,
        )

    # Display explanations for symptoms
    if symptoms:
        st.markdown("<h2>Symptoms Explanations</h2>", unsafe_allow_html=True)
        for symptom in symptoms:
            explanation = symptom_reasons.get(symptom, "No explanation available.")
            st.markdown(
                f"<div class='explanation-box'>{symptom.capitalize()} {explanation}</div>",
                unsafe_allow_html=True,
            )

    # Display explanations for past conditions
    if past_conditions:
        st.markdown("<h2>Past Conditions Explanations</h2>", unsafe_allow_html=True)
        for condition in past_conditions:
            explanation = condition_reasons.get(condition, "No explanation available.")
            st.markdown(
                f"<div class='explanation-box'>{condition.capitalize()} {explanation}</div>",
                unsafe_allow_html=True,
            )

# Footer
st.markdown(
    "<h6 style='color: white;'>Disclaimer: This app is not a substitute for professional medical advice. Please consult a healthcare provider for any health-related concerns.</h6>",
    unsafe_allow_html=True,
)
