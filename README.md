# Medical Insurance Cost Prediction

This repository contains a machine learning project that predicts medical insurance costs based on user inputs such as age, gender, BMI, number of children, smoking status, and region.

## Features

* Implements multiple machine learning models:

  * Linear Regression
  * Random Forest Regressor
  * Decision Tree Regressor
* Provides a user-friendly Streamlit web interface to interact with the models.
* Exposes a RESTful API to make predictions using the trained models.

## Project Structure

```
├── app.py                  # Streamlit app interface
├── main.py                 # Core logic and model loading
├── api.py                  # RESTful API using FastAPI
├── model/                  # Directory containing trained model pickle files
│   ├── linear_model.pkl
│   ├── random_model.pkl
│   └── descision_model.pkl
├── static/                 # Any frontend assets if needed
├── requirements.txt        # Python dependencies
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/pranjaykumar926/Medical-Insurance-Cost-Prediction.git
cd Medical-Insurance-Cost-Prediction
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Streamlit App

```bash
streamlit run app.py
```

## Running the API Server

```bash
uvicorn api:app --reload
```

The API will be available at `http://127.0.0.1:8000` with automatic documentation at `http://127.0.0.1:8000/docs` (Swagger UI).

## API Endpoints

### GET `/`

Returns a welcome message.

### POST `/predict`

Accepts JSON input and returns the predicted insurance cost.

**Input JSON:**

```json
{
  "age": 29,
  "sex": "male",
  "bmi": 27.9,
  "children": 0,
  "smoker": "yes",
  "region": "southwest",
  "model": "linear"
}
```

**Supported model values:** `linear`, `random`, `descision`

**Output JSON:**

```json
{
  "prediction": 16884.92
}
```

## Author

Pranjay Kumar
[GitHub](https://github.com/pranjaykumar926)

---

Feel free to fork this repository and contribute to the project.
