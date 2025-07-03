import streamlit as st
import numpy as np
import joblib

# Load models
models = {
    'Linear Regression': joblib.load('linear_regression.pkl'),
    'Decision Tree': joblib.load('decision_tree.pkl'),
    'Random Forest': joblib.load('random_forest.pkl')
}

st.title('Medical Insurance Cost Prediction App')
st.subheader('Choose your model and enter your details:')

# User Inputs
age = st.number_input('Age', min_value=1, max_value=100, value=25)
sex = st.selectbox('Sex', ['male', 'female'])
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input('Children', min_value=0, max_value=10, value=0)
smoker = st.selectbox('Smoker', ['yes', 'no'])
region = st.selectbox('Region', ['northeast', 'northwest', 'southeast', 'southwest'])

model_choice = st.selectbox('Select Model:', list(models.keys()))

# Preprocess inputs
sex = 0 if sex == 'male' else 1
smoker = 1 if smoker == 'yes' else 0
region_northwest = 1 if region == 'northwest' else 0
region_southeast = 1 if region == 'southeast' else 0
region_southwest = 1 if region == 'southwest' else 0

X_input = np.array([[age, sex, bmi, children, smoker, region_northwest, region_southeast, region_southwest]])

# Predict
if st.button('Predict Insurance Cost'):
    model = models[model_choice]
    prediction = model.predict(X_input)[0]
    st.success(f'Estimated Insurance Cost using {model_choice}: ${prediction:.2f}')
