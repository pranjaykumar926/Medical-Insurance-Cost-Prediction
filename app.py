import streamlit as st
import pandas as pd
import requests

# Replace with your deployed API URL
API_URL = "http://127.0.0.1:8000/predict_all"

st.set_page_config(page_title="Medical Insurance Cost Prediction", page_icon="💊", layout="centered")
st.title('💊 Medical Insurance Cost Prediction')
st.markdown("Enter your details below to estimate insurance costs using different models.")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    age = st.number_input('Age', min_value=1, max_value=100, value=25)
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0)
    children = st.number_input('Number of Children', min_value=0, max_value=10, value=0)

with col2:
    sex = st.selectbox('Sex', ['male', 'female'])
    smoker = st.selectbox('Smoker', ['yes', 'no'])
    region = st.selectbox('Region', ['northeast', 'northwest', 'southeast', 'southwest'])

if st.button('🔍 Predict Insurance Cost'):
    payload = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            results = response.json()
            results_df = pd.DataFrame(list(results.items()), columns=["Model", "Predicted Cost ($)"])
            st.subheader("Predicted Insurance Costs")
            st.table(results_df)
            st.subheader("Comparison of Predictions")
            st.bar_chart(results_df.set_index("Model"))
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"API request failed: {e}")
