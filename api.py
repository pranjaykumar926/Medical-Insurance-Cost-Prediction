from fastapi import FastAPI, Query
from pydantic import BaseModel
import numpy as np
import joblib
import os

# Load all models once at startup
models = {
    "linear_regression": joblib.load("linear_regression.pkl"),
    "random_forest": joblib.load("random_forest.pkl"),
    "decision_tree": joblib.load("decision_tree.pkl")
}

app = FastAPI(title="Medical Insurance Prediction API (All Models)")

class InsuranceInput(BaseModel):
    age: int
    sex: str        # 'male' or 'female'
    bmi: float
    children: int
    smoker: str     # 'yes' or 'no'
    region: str     # 'northeast', 'northwest', 'southeast', 'southwest'

def preprocess(input_data: InsuranceInput):
    sex = 1 if input_data.sex.lower() == 'male' else 0
    smoker = 1 if input_data.smoker.lower() == 'yes' else 0

    region_map = {
        'northeast': [1, 0, 0, 0],
        'northwest': [0, 1, 0, 0],
        'southeast': [0, 0, 1, 0],
        'southwest': [0, 0, 0, 1],
    }
    region_encoded = region_map.get(input_data.region.lower(), [0, 0, 0, 0])

    features = [
        input_data.age,
        input_data.bmi,
        input_data.children,
        sex,
        smoker
    ] + region_encoded

    return np.array([features])

@app.get("/")
def home():
    return {
        "message": "Welcome to the Medical Insurance Prediction API!",
        "available_models": list(models.keys())
    }

@app.post("/predict")
def predict(data: InsuranceInput, model: str = Query("random_forest", enum=models.keys())):
    try:
        input_array = preprocess(data)
        prediction = models[model].predict(input_array)[0]
        return {
            "model_used": model,
            "predicted_insurance_cost": round(float(prediction), 2)
        }
    except Exception as e:
        return {"error": str(e)}
