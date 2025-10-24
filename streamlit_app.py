import os
import numpy as np
import requests
import streamlit as st

# Set page config
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        max-width: 600px;
        padding: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .prediction {
        font-size: 1.5rem;
        color: #4CAF50;
        font-weight: bold;
        margin-top: 1rem;
        padding: 1rem;
        background-color: #f0f8ff;
        border-radius: 5px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.title("💰 Salary Prediction")
st.markdown("Enter years of experience to predict the expected salary.")

# API Configuration
API_URL = os.getenv('API_URL', 'http://localhost:5000') + '/predict'

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        years_exp = st.number_input(
            "Years of Experience",
            min_value=0.0,
            max_value=50.0,
            value=5.0,
            step=0.5,
            format="%.1f"
        )
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        submit_button = st.form_submit_button("Predict Salary")

# Handle form submission
if submit_button:
    try:
        # Make API request
        response = requests.post(
            API_URL,
            json={"years_experience": [years_exp]},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            predicted_salary = result['predicted_salaries'][0]
            st.balloons()
            st.markdown(
                f"<div class='prediction'>"
                f"Predicted Salary: ${predicted_salary:,.2f}"
                f"</div>",
                unsafe_allow_html=True
            )
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")

    except Exception as e:
        st.error(f"Failed to connect to the prediction service. Error: {str(e)}")

# Add some space at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Note: This is a prediction based on the trained model. Actual salaries may vary.")