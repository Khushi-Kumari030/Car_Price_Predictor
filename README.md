# 🚗 Car Price Estimator App

This project is an end-to-end machine learning application that predicts the selling price of used cars based on features such as brand, fuel type, transmission type, mileage, engine capacity, and more. The application includes a web-based interface built with Streamlit where users can input car details and get an estimated resale price instantly.

---

## 📌 Project Overview

The goal of this project is to build a regression model that can accurately estimate the resale price of a used car based on key technical and categorical features. The model is deployed as an interactive Streamlit app, allowing users to test predictions live.

---

## 📊 Dataset Source

The dataset used in this project is publicly available on [Kaggle - CarDekho Car Details Dataset](https://www.kaggle.com/datasets). It contains various features such as:

- `brand`
- `car_name`
- `model`
- `fuel_type`
- `seller_type`
- `transmission_type`
- `vehicle_age`
- `km_driven`
- `mileage`
- `engine`
- `max_power`
- `seats`
- `selling_price` (target)

---

## 🧹 Data Preprocessing

Several preprocessing steps were applied to clean and prepare the dataset:

- Filtered uncommon fuel types and removed outliers using boxplot logic.
- Feature Selection based on multicollinearity.
- Ensured multicollinearity was checked using VIF analysis.
- Converted categorical variables (`fuel_type`, `brand`, etc.) using `OneHotEncoding`.

---

## 🧠 Model Used

- **Model**: `XGBoostRegressor`  
- **Why XGBoost?**: XGBoost is known for its performance and ability to handle feature interactions and non-linearities well.
- **Feature Engineering**: Numerical + encoded categorical variables using `ColumnTransformer`.

---

## ✅ Evaluation Results

| Metric    | Value |
|-----------|-------|
| R² Score  | ~0.87 |
| Model     | XGBoost Regressor |
| Input Features | brand, fuel_type, seller_type, transmission_type, km_driven, mileage, engine, seats |

> The model showed strong performance with an R² score of approximately **0.87** on the test set.

---

## 🌐 Streamlit App

The app allows users to input:
- **Dropdowns**: `brand`, `fuel_type`
- **Checklists**: `seller_type`, `transmission_type`
- **Sliders**: `mileage`, `km_driven`, `engine`, `seats`

### 🔧 To Run the App Locally:

1. **Install dependencies**

```bash
pip install -r requirements.txt
