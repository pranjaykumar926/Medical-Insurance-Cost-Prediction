# Medical Insurance Cost Prediction

This project presents a machine learning solution to predict medical insurance charges based on personal attributes such as age, BMI, gender, smoking status, and geographical region. By leveraging statistical learning and regression techniques, the model provides accurate cost estimations to support insurance risk assessment, personal budgeting, and healthcare analytics.

---

## Project Objectives

The primary objective is to develop a regression-based predictive model that estimates individual medical insurance costs using structured health and demographic data. The project also explores the relative impact of various features—such as smoking habits and BMI—on healthcare expenses.

---

## Repository Contents

```
Medical-Insurance-Cost-Prediction/
├── insurance.csv                           # Dataset for training and evaluation
├── Medical_Insurance_Cost_Prediction.ipynb # End-to-end implementation in Jupyter Notebook
├── Major (3).pdf                           # Formal project report
├── README.md                               # Project documentation (this file)
```

---

## Dataset Overview

The dataset consists of 1,300+ observations with the following attributes:

| Feature    | Description                                     |
| ---------- | ----------------------------------------------- |
| `age`      | Age of the individual                           |
| `sex`      | Gender (male/female)                            |
| `bmi`      | Body Mass Index                                 |
| `children` | Number of dependent children                    |
| `smoker`   | Smoking status (yes/no)                         |
| `region`   | Residential region in the United States         |
| `charges`  | Annual medical insurance cost (target variable) |

---

## Methodology

### Data Exploration

* Assessment of null values and data types
* Statistical summaries and distribution analysis
* Outlier detection using boxplots (especially for smoking status)
* Correlation matrix to evaluate feature relevance

### Model Implementation

Several supervised regression algorithms were implemented:

* **Linear Regression**
* **Lasso Regression**
* **Polynomial Regression** (to model non-linear relationships)
* **Random Forest Regressor**

> The most effective model achieved an **R² score exceeding 0.85**, indicating strong predictive performance.

### Evaluation Metrics

Model performance was assessed using the following metrics:

* R² Score (Coefficient of Determination)
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* K-Fold Cross-Validation for generalizability

---

## Technology Stack

* **Language:** Python 3.8+
* **Libraries:**

  * Data manipulation: `pandas`, `numpy`
  * Visualization: `matplotlib`, `seaborn`
  * Machine learning: `scikit-learn`
* **Environment:** Jupyter Notebook

---

## Use Cases

This predictive model has applications in:

* **Insurance underwriting**: Assisting insurance companies in calculating fair premiums.
* **Personal finance**: Enabling individuals to estimate potential healthcare costs.
* **Healthcare analytics**: Supporting research into cost-driving factors in health expenditures.

---

## Visual Outputs

Included visualizations:

* Correlation heatmaps to identify key drivers of cost
* Distribution and density plots for numeric features
* Boxplots to highlight cost differences between smokers and non-smokers
* Actual vs. predicted charge comparison plots

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/pranjaykumar926/Medical-Insurance-Cost-Prediction.git
   cd Medical-Insurance-Cost-Prediction
   ```

2. **Install required packages**

   It is recommended to use a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

   *(Alternatively, manually install: pandas, numpy, matplotlib, seaborn, scikit-learn, jupyter)*

3. **Launch Jupyter Notebook**

   ```bash
   jupyter notebook Medical_Insurance_Cost_Prediction.ipynb
   ```

---

## Future Work

* Integration of deep learning models for improved non-linear representation
* Deployment via Flask or Streamlit as an interactive web application
* Extension into mobile platforms for broader accessibility

---

## Author

**Pranjay Kumar**
GitHub: [@pranjaykumar926](https://github.com/pranjaykumar926)

---

## License

This project is available under the [MIT License](LICENSE).

---

## Contributions & Feedback

Feedback and contributions are welcome. Please open an issue or submit a pull request for enhancements.
