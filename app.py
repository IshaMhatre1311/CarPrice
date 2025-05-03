import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
filename = 'car_price_prediction.sav'
model = pickle.load(open(filename, 'rb'))

# Load the LabelEncoder (if used during training)
# ... (Code to load LabelEncoders if necessary)


st.title("Car Price Prediction App")

# Create input fields for user
# Example:
manufacturer = st.selectbox("Manufacturer", options=['Audi', 'BMW', 'Ford', 'Honda', 'Hyundai', 'Mahindra', 'Maruti', 'Mercedes-Benz', 'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen'])
age = st.number_input("Age of the car", min_value=0, max_value=30)
kms_driven = st.number_input("Kilometers Driven", min_value=0)
fuel_type = st.selectbox("Fuel Type", options=['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])
transmission = st.selectbox("Transmission", options=['Manual', 'Automatic'])
owner_type = st.selectbox("Owner Type", options=['First', 'Second', 'Third', 'Fourth & Above'])
mileage = st.number_input("Mileage (Kmpl/Kmkg)", min_value=0.0)
engine = st.number_input("Engine (bhp)", min_value=0.0)
power = st.number_input("Power (CC)", min_value=0.0)
seats = st.number_input("Seats", min_value=0, max_value=10)

# Encode categorical features using LabelEncoder (if used during training)
# ... (Code to transform user inputs using the loaded LabelEncoders)

# Example: (adapt to your actual encoding)
# manufacturer = le_manufacturer.transform([manufacturer])[0]
# fuel_type = le_fuel_type.transform([fuel_type])[0]
# ...

# Create a feature vector for prediction
features = pd.DataFrame({
    'Manufacturer': [manufacturer], 'Age': [age], 'Kilometers_Driven': [kms_driven],
    'Fuel_Type': [fuel_type], 'Transmission': [transmission],
    'Owner_Type': [owner_type], 'Mileage(Kmpl/Kmkg)': [mileage],
    'Engine(bhp)': [engine], 'Power(CC)': [power], 'Seats': [seats]
})

# Make prediction
prediction = model.predict(features)[0]


if st.button("Predict Price"):
    st.write(f"Predicted Car Price: {prediction}")


