# 🩺🔥 Medical Insurance Cost Prediction 💰⚡

Predicting healthcare expenses just got smarter! This project uses Machine Learning to forecast **medical insurance charges** based on personal attributes like age, BMI, and lifestyle choices. 💡🧠

---

## 🚀💻 Project Overview

This repository presents a **regression-based ML model** designed to predict medical insurance costs. By analyzing factors such as smoking habits, BMI, and demographics, the model helps insurers and individuals estimate healthcare expenses with high accuracy. 📉📈

---

## 📁🗂️ Files & Structure

```
📆 Medical-Insurance-Cost-Prediction/
📅 insurance.csv                # Dataset used for training and testing
📅 Medical_Insurance_Cost_Prediction.ipynb  # Jupyter Notebook with the full pipeline
📅 Major (3).pdf                # Project report/documentation
📅 README.md                    # You're here!
```

---

## 📊🧾 Dataset Description

The dataset contains **1,300+** records of individuals with the following features:

| 🔠 Feature | 🧩 Description                               |
| ---------- | -------------------------------------------- |
| `age`      | Age of the policyholder 👴👩                 |
| `sex`      | Gender (male/female) ⚧️                      |
| `bmi`      | Body Mass Index 🧮                           |
| `children` | Number of dependent children 👶              |
| `smoker`   | Smoking status (yes/no) 🚬❌                  |
| `region`   | Residential region in the US 🗺️             |
| `charges`  | Medical insurance costs (target variable) 🩺 |

---

## 🔍📊 Exploratory Data Analysis (EDA)

✔️ Null Value Check ✅
✔️ Distribution Plots 📉📊
✔️ Correlation Heatmap 🔥
✔️ Boxplots to highlight outliers (especially for smokers vs non-smokers) 📦🚬

---

## ⚙️🧰 Model Building

Implemented regression models to predict `charges`:

* ✅ Linear Regression ➖
* ✅ Lasso Regression 🧪
* ✅ Random Forest Regressor 🌲
* ✅ Polynomial Regression (for capturing non-linearity) 📈

🏆 **Best Model Achieved R² Score > 0.85** 🎯💯

---

## 📈🧪 Model Evaluation

* 📊 R² Score
* 📉 Mean Absolute Error (MAE)
* 📉 Mean Squared Error (MSE)
* 📉 Root Mean Squared Error (RMSE)
* 🔁 Cross-validation for reliability

---

## 🛠️👨‍💻 Tech Stack

* 🐍 **Python**
* 🧮 **Pandas** & **NumPy**
* 📊 **Matplotlib** & **Seaborn**
* 🤖 **Scikit-learn**
* 📓 **Jupyter Notebook**

---

## 📌💼 Use Case

* 📊 **Insurance companies** can use this model to determine premiums. 💸
* 🧑‍💻 **Individuals** can estimate expected charges based on their health/lifestyle. 🧘‍♀️
* 🩺 **Healthcare analysts** can identify cost trends and outliers. 📉📈

---

## 📷🎨 Sample Visualizations

* 🧯 Correlation heatmap showing relationships between variables
* 📊 Bar plots: Smokers vs Non-Smokers
* 📈 Predicted vs Actual Charges comparison

---

## 📌🖥️ How to Run

1. 🔽 Clone the repo:

   ```bash
   git clone https://github.com/pranjaykumar926/Medical-Insurance-Cost-Prediction.git
   cd Medical-Insurance-Cost-Prediction
   ```

2. 🚀 Open the Jupyter notebook:

   ```bash
   jupyter notebook Medical_Insurance_Cost_Prediction.ipynb
   ```

---

## 🧠🚀 Future Improvements

* 🔮 Integrate deep learning models for more complex feature interactions.
* 🌐 Deploy as a web app using Flask or Streamlit.
* 📱 Build a mobile-friendly interface for user predictions.

---

## 🙌👨‍💻 Author

**Pranjay Kumar**
🔗 [GitHub](https://github.com/pranjaykumar926)

---

## 🌟💖 Show Your Support

If you found this useful, please ⭐ star the repo and share it! 🔁🙌
