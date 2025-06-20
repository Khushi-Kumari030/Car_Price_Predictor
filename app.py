import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load saved model pipeline
with open("car_price_pipeline.pkl", "rb") as f:
    pipe = pickle.load(f)

# Load dataset used for UI options
df = pd.read_csv("car_data_for_ui.csv")

st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title("🚘 Car Price Prediction App")

# Dropdown inputs
brand = st.selectbox("Brand", sorted(df['brand'].dropna().unique()))
fuel_type = st.selectbox("Fuel Type", sorted(df['fuel_type'].dropna().unique()))

# Radio buttons (checkbox style, but single-select as per model input)
seller_type = st.radio("Seller Type", sorted(df['seller_type'].dropna().unique()))
transmission_type = st.radio("Transmission Type", sorted(df['transmission_type'].dropna().unique()))

# Sliders for numerical input
seats = st.slider("Number of Seats", int(df['seats'].min()), int(df['seats'].max()), step=1)
km_driven = st.slider("Kilometers Driven", int(df['km_driven'].min()), int(df['km_driven'].max()), step=500)
mileage = st.slider("Mileage (km/l)", float(df['mileage'].min()), float(df['mileage'].max()), step=0.1)
engine = st.slider("Engine Capacity (CC)", float(df['engine'].min()), float(df['engine'].max()), step=10.0)

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame({
        'brand': [brand],
        'fuel_type': [fuel_type],
        'seller_type': [seller_type],
        'transmission_type': [transmission_type],
        'seats': [seats],
        'km_driven': [km_driven],
        'mileage': [mileage],
        'engine': [engine]
    })

    # Predict
    prediction = pipe.predict(input_df)[0]
    st.success(f"💰 Estimated Selling Price: ₹ {prediction:,.2f}")
