from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load all models at startup
models = {
    "Linear Regression": joblib.load("linear_regression.pkl"),
    "Random Forest": joblib.load("random_forest.pkl"),
    "Decision Tree": joblib.load("decision_tree.pkl")
}

app = FastAPI(title="Medical Insurance Prediction API (All Models)")

class InsuranceInput(BaseModel):
    age: int
    sex: str        # 'male' or 'female'
    bmi: float
    children: int
    smoker: str     # 'yes' or 'no'
    region: str     # 'northeast', 'northwest', 'southeast', 'southwest'

# Preprocessing — matches training encoding
def preprocess(age, sex, bmi, children, smoker, region):
    sex = 0 if sex.lower() == 'male' else 1
    smoker = 1 if smoker.lower() == 'yes' else 0

    region_northwest = 1 if region.lower() == 'northwest' else 0
    region_southeast = 1 if region.lower() == 'southeast' else 0
    region_southwest = 1 if region.lower() == 'southwest' else 0

    features = [
        age,
        sex,
        bmi,
        children,
        smoker,
        region_northwest,
        region_southeast,
        region_southwest
    ]
    return np.array([features])

@app.get("/")
def home():
    return {
        "message": "Welcome to the Medical Insurance Prediction API!",
        "available_models": list(models.keys())
    }

@app.post("/predict_all")
def predict_all(data: InsuranceInput):
    try:
        input_array = preprocess(data.age, data.sex, data.bmi, data.children, data.smoker, data.region)
        results = {name: round(float(model.predict(input_array)[0]), 2) for name, model in models.items()}
        return results
    except Exception as e:
        return {"error": str(e)}
