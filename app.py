
import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# Load model and scaler
model = tf.keras.models.load_model("model.h5")
scaler = joblib.load("scaler.pkl")

st.title("📊 Financial Needs Predictor")

# Inputs
product = st.selectbox("Product", ['Rice', 'Wheat', 'Corn', 'Soybean'])
season = st.selectbox("Seasonal Factor", ['Low', 'Medium', 'High'])
crop = st.selectbox("Crop Type", ['Wheat', 'Corn', 'Soybean'])

features = [
    st.slider("Market Price per Ton", 100, 1000),
    st.slider("Demand Index", 0, 500),
    st.slider("Supply Index", 0, 500),
    st.slider("Competitor Price", 100, 1000),
    st.slider("Economic Indicator", 0.0, 2.0),
    st.slider("Weather Score", 0, 100),
    st.slider("Consumer Trend", 0, 200),
    st.slider("Soil pH", 3.0, 9.0),
    st.slider("Soil Moisture", 0, 100),
    st.slider("Temperature", 10, 40),
    st.slider("Rainfall", 0, 300),
    st.slider("Fertilizer Usage", 0, 200),
    st.slider("Pesticide Usage", 0, 50),
    st.slider("Crop Yield", 0.0, 10.0),
    st.slider("Sustainability Score", 0, 100)
]

# Dummy encodings for categories
product_dict = {'Rice': 0, 'Wheat': 1, 'Corn': 2, 'Soybean': 3}
season_dict = {'Low': 0, 'Medium': 1, 'High': 2}
crop_dict = {'Wheat': 0, 'Corn': 1, 'Soybean': 2}

encoded = [product_dict[product], season_dict[season], crop_dict[crop]] + features
X_input = scaler.transform([encoded]).reshape(1, 1, -1)

if st.button("Predict Loan Need"):
    prediction = model.predict(X_input)[0][0]
    result = "✅ Loan/Insurance Required" if prediction > 0.5 else "❌ No Immediate Need"
    st.success(f"Prediction: {result}")
