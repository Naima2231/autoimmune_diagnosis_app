# ✅ app.py - Streamlit App
import streamlit as st
import joblib
import numpy as np

# Load the trained model (make sure this file exists in the same folder)
model = joblib.load("autoimmune_diagnosis_model.pkl")

# Define input fields for lab test values and symptoms
st.title("Autoimmune Disease Diagnosis App")
st.write("Enter the patient's lab results and symptoms below:")

# Lab test inputs
crp = st.number_input("CRP (mg/L)", min_value=0.0, value=5.0)
esr = st.number_input("ESR (mm/hr)", min_value=0.0, value=10.0)
rf = st.number_input("RF (IU/mL)", min_value=0.0, value=10.0)
ana = st.number_input("ANA (titer ratio or numeric value)", min_value=0.0, value=0.0)
anti_ccp = st.number_input("Anti-CCP (U/mL)", min_value=0.0, value=5.0)

# Symptom checkboxes
joint_pain = st.checkbox("Joint Pain")
fatigue = st.checkbox("Fatigue")
butterfly_rash = st.checkbox("Butterfly Rash")
fever = st.checkbox("Fever")
morning_stiffness = st.checkbox("Morning Stiffness")
photosensitivity = st.checkbox("Photosensitivity")
dry_eyes = st.checkbox("Dry Eyes")
dry_mouth = st.checkbox("Dry Mouth")
skin_hardening = st.checkbox("Skin Hardening")
muscle_weakness = st.checkbox("Muscle Weakness")
vision_problems = st.checkbox("Vision Problems")

if st.button("Predict Diagnosis"):
    input_data = np.array([[crp, esr, rf, ana, anti_ccp,
                            joint_pain, fatigue, butterfly_rash, fever,
                            morning_stiffness, photosensitivity,
                            dry_eyes, dry_mouth, skin_hardening,
                            muscle_weakness, vision_problems]])
    # Assuming you used LabelEncoder during training:
from sklearn.preprocessing import LabelEncoder

# Re-create the encoder and fit on original disease labels
label_encoder = LabelEncoder()
label_encoder.fit(['SLE', 'RA', 'MS', "Sjogren's", 'SSc', 'Healthy'])

# Make prediction
prediction = model.predict(input_df)[0]

# Decode the numeric prediction back to disease name
predicted_disease = label_encoder.inverse_transform([prediction])[0]

st.success(f"Predicted Diagnosis: {predicted_disease}")
