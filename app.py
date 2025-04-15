import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load("autoimmune_diagnosis_model.pkl")  # Your updated model filename

# Re-create label encoder and fit the correct class order
label_encoder = LabelEncoder()
label_encoder.fit(['Healthy', 'MS', 'RA', 'SLE', 'SSc', "Sjogren's"])

# Title
st.title("🧠 Autoimmune Disease Diagnosis App")
st.markdown("Enter symptoms and lab test results to predict the most likely autoimmune disease.")

# Lab test input
st.header("🔬 Lab Test Results")
CRP = st.number_input("CRP", min_value=0.0)
ESR = st.number_input("ESR", min_value=0.0)
RF = st.number_input("Rheumatoid Factor (RF)", min_value=0.0)
ANA = st.number_input("ANA", min_value=0.0)
Anti_CCP = st.number_input("Anti-CCP", min_value=0.0)

# Symptom input
st.header("🩺 Symptoms")
Joint_Pain = st.checkbox("Joint Pain")
Fatigue = st.checkbox("Fatigue")
Butterfly_Rash = st.checkbox("Butterfly Rash")
Fever = st.checkbox("Fever")
Morning_Stiffness = st.checkbox("Morning Stiffness")
Photosensitivity = st.checkbox("Photosensitivity")
Dry_Eyes = st.checkbox("Dry Eyes")
Dry_Mouth = st.checkbox("Dry Mouth")
Skin_Hardening = st.checkbox("Skin Hardening")
Muscle_Weakness = st.checkbox("Muscle Weakness")
Vision_Problems = st.checkbox("Vision Problems")

# Predict button
if st.button("🔎 Predict Disease"):
    input_data = {
        'CRP': CRP,
        'ESR': ESR,
        'RF': RF,
        'ANA': ANA,
        'Anti_CCP': Anti_CCP,
        'Joint_Pain': Joint_Pain,
        'Fatigue': Fatigue,
        'Butterfly_Rash': Butterfly_Rash,
        'Fever': Fever,
        'Morning_Stiffness': Morning_Stiffness,
        'Photosensitivity': Photosensitivity,
        'Dry_Eyes': Dry_Eyes,
        'Dry_Mouth': Dry_Mouth,
        'Skin_Hardening': Skin_Hardening,
        'Muscle_Weakness': Muscle_Weakness,
        'Vision_Problems': Vision_Problems
    }

    input_df = pd.DataFrame([input_data])

    # Convert True/False to 1/0
    symptom_cols = [
        'Joint_Pain', 'Fatigue', 'Butterfly_Rash', 'Fever', 'Morning_Stiffness',
        'Photosensitivity', 'Dry_Eyes', 'Dry_Mouth', 'Skin_Hardening',
        'Muscle_Weakness', 'Vision_Problems'
    ]
    input_df[symptom_cols] = input_df[symptom_cols].astype(int)

    # Predict
    prediction = model.predict(input_df)[0]
    predicted_disease = label_encoder.inverse_transform([prediction])[0]

    st.success(f"✅ **Predicted Diagnosis:** {predicted_disease}")
