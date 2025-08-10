import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load models
models = {
    'Linear Regression': joblib.load('linear_regression.pkl'),
    'Decision Tree': joblib.load('decision_tree.pkl'),
    'Random Forest': joblib.load('random_forest.pkl')
}

st.set_page_config(page_title="Medical Insurance Cost Prediction", page_icon="💊", layout="centered")
st.title('💊 Medical Insurance Cost Prediction')
st.markdown("Enter your details below to estimate insurance costs using different models.")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    age = st.number_input('Age', min_value=1, max_value=100, value=25, help="Enter your age in years")
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0, help="Body Mass Index")
    children = st.number_input('Number of Children', min_value=0, max_value=10, value=0, help="Dependents under insurance")

with col2:
    sex = st.selectbox('Sex', ['male', 'female'])
    smoker = st.selectbox('Smoker', ['yes', 'no'])
    region = st.selectbox('Region', ['northeast', 'northwest', 'southeast', 'southwest'])

# Preprocess inputs
sex = 0 if sex == 'male' else 1
smoker = 1 if smoker == 'yes' else 0
region_northwest = 1 if region == 'northwest' else 0
region_southeast = 1 if region == 'southeast' else 0
region_southwest = 1 if region == 'southwest' else 0

X_input = np.array([[age, sex, bmi, children, smoker, region_northwest, region_southeast, region_southwest]])

# Predict with all models
if st.button('🔍 Predict Insurance Cost'):
    results = {}
    for name, model in models.items():
        prediction = model.predict(X_input)[0]
        results[name] = round(prediction, 2)

    # Show predictions in table
    st.subheader("Predicted Insurance Costs")
    results_df = pd.DataFrame(list(results.items()), columns=["Model", "Predicted Cost ($)"])
    st.table(results_df)

    # Show bar chart
    st.subheader("Comparison of Predictions")
    st.bar_chart(results_df.set_index("Model"))
