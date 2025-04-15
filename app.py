import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load pre-trained model
model = joblib.load("your_model_file.pkl")  # Replace with your model file path

# Define the feature names for symptoms and lab results
feature_names = ['CRP', 'ESR', 'RF', 'ANA', 'Anti_CCP', 'Joint_Pain', 'Fatigue', 
                 'Butterfly_Rash', 'Fever', 'Morning_Stiffness', 'Photosensitivity', 
                 'Dry_Eyes', 'Dry_Mouth', 'Skin_Hardening', 'Muscle_Weakness', 
                 'Vision_Problems']

# Create the user input form
def user_input():
    st.title("Autoimmune Disease Diagnosis")
    st.write("Please enter the patient's symptoms and lab results:")

    # Input fields for the symptoms and lab results
    data = {}
    for feature in feature_names:
        data[feature] = st.number_input(f"{feature}:", min_value=0, max_value=100, step=1)

    # Convert user input into dataframe
    input_df = pd.DataFrame([data])
    return input_df

# Prediction function
def predict(input_data):
    prediction = model.predict(input_data)
    return prediction

# Display user input and prediction
input_data = user_input()
if st.button("Predict"):
    result = predict(input_data)
    st.write(f"Predicted Disease: {result[0]}")

