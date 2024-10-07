import streamlit as st
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd

# Load your trained model
model = pd.read_pickle('your_model.pkl')  # Replace 'your_model.pkl' with your actual model file

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Set black background for the whole page */
    .main {
        background-color: #000000;
    }
    /* Style the header */
    h1 {
        color: #1E90FF;  /* DodgerBlue color for heading */
        font-size: 36px;
    }
    h2 {
        color: #00FF7F;  /* SpringGreen for subheadings */
        font-size: 26px;
    }
    /* Style the select box */
    .stSelectbox, .stTextInput {
        background-color: #333333; /* Dark background for inputs */
        color: white;  /* White text */
        border-radius: 10px;
    }
    /* Style the button */
    .stButton button {
        background-color: #1E90FF;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    /* Change the color of the prediction box */
    .predicted-score-box {
        background-color: #333333;
        color: #00FF7F;  /* SpringGreen for the score */
        font-size: 20px;
        padding: 10px;
        border-radius: 10px;
    }
    /* Style for assessment messages */
    .assessment-box {
        background-color: #FFA07A;  /* LightSalmon for warning */
        color: black;
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
    }
    .explanation-box {
        background-color: #00CED1;  /* DarkTurquoise for explanations */
        color: white;
        padding: 10px;
        border-radius: 10px;
    }
    /* Style multi-select boxes */
    .stMultiSelect {
        background-color: #333333;
        color: white;
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

# Model performance metrics (replace with your actual metrics)
st.markdown("<h2>Model Performance</h2>", unsafe_allow_html=True)
st.write("Mean Squared Error: 0.63176")
st.write("R-squared: 0.89648")

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

# Reason dictionaries
symptom_reasons = {
    "stomach ache": "could indicate gastrointestinal issues such as indigestion or ulcers.",
    "sore throat": "is often caused by viral infections such as the common cold or flu.",
    "headache": "can result from stress, dehydration, or even vision problems.",
    "nausea": "is commonly linked to digestive issues, food poisoning, or early pregnancy.",
    "cough": "could be due to respiratory infections or allergies.",
    "fever": "is typically a sign of infection or inflammation in the body.",
    "fatigue": "can be related to lack of sleep, anemia, or thyroid disorders.",
    "chest pain": "is a serious symptom that could indicate heart disease or lung problems.",
    "back pain": "can arise from poor posture, muscle strain, or spinal issues.",
    "joint pain": "is often associated with arthritis or injury.",
    "rash": "could be a sign of an allergic reaction or skin infection.",
    "shortness of breath": "is a concerning symptom often related to heart or lung problems.",
    "dizziness": "can be caused by dehydration, inner ear issues, or low blood pressure.",
    "vomiting": "is frequently related to infections, food poisoning, or gastrointestinal problems.",
    "diarrhea": "is usually linked to infections, food intolerance, or gastrointestinal disorders.",
    "constipation": "is often due to a lack of fiber in the diet or dehydration.",
    "muscle pain": "may be caused by overuse, injury, or conditions such as fibromyalgia.",
    "abdominal pain": "can signal gastrointestinal issues such as ulcers or infections.",
    "cold": "is usually due to viral infections like the common cold or flu.",
    "itching": "can indicate allergic reactions, skin conditions, or infections.",
    "dry throat": "is commonly due to dehydration or exposure to dry air.",
    "chills": "often accompany fever and indicate infection or immune response.",
    "sweating": "can be due to fever, stress, or hormonal imbalances.",
    "loss of appetite": "is a common sign of digestive disorders or infections.",
}

condition_reasons = {
    "asthma": "causes chronic inflammation in the airways, leading to breathing difficulties.",
    "hypertension": "increases the risk of heart disease, stroke, and kidney problems.",
    "diabetes": "affects blood sugar regulation and can lead to complications like neuropathy and kidney damage.",
    "arthritis": "causes joint inflammation, pain, and decreased mobility over time.",
    "heart disease": "restricts blood flow, increasing the risk of heart attacks and heart failure.",
    "stroke": "results from reduced blood flow to the brain, leading to brain cell damage.",
    "cancer": "involves abnormal cell growth that can spread to other parts of the body.",
    "COPD": "damages the lungs and leads to breathing difficulties over time.",
    "chronic kidney disease": "impairs the kidneys' ability to filter waste, leading to toxic buildup in the body.",
    "liver disease": "reduces the liver's ability to detoxify the body, process nutrients, and produce vital proteins.",
    "alzheimer's disease": "leads to memory loss and cognitive decline over time.",
    "parkinson's disease": "causes movement disorders due to reduced dopamine production in the brain.",
    "epilepsy": "is characterized by recurrent seizures due to