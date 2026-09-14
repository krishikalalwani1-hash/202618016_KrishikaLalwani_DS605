
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

# --- 1. SET UP PAGE STYLING ---
st.set_page_config(page_title="NYC Airbnb Price Predictor", page_icon="🏢", layout="centered")

st.title("🏢 New York City Airbnb Price Predictor")
st.write("Enter the details of an NYC property below to instantly generate a machine-learning predicted nightly price.")

# --- 2. LOAD THE TRAINED PIPELINE ---
@st.cache_resource
def load_pipeline():
    return joblib.load('airbnb_model_pipeline.pkl')

try:
    model_pipeline = load_pipeline()
except FileNotFoundError:
    st.error("❌ 'airbnb_model_pipeline.pkl' not found! Make sure you run your model training file to save it first.")
    st.stop()

# --- 3. CREATE THE USER FORM INTERFACE ---
st.header("📋 Listing Specifications")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        # Spatial coordinate selections using realistic NYC data bounds
        latitude = st.number_input("Latitude", min_value=40.40, max_value=40.95, value=40.7128, format="%.4f")
        minimum_nights = st.number_input("Minimum Nights Required", min_value=1, max_value=365, value=2)
        reviews_per_month = st.number_input("Average Reviews per Month", min_value=0.0, max_value=20.0, value=1.5, format="%.2f")
        
        # Categorical dropdown selector selections
        neighbourhood_group = st.selectbox(
            "Borough (Neighbourhood Group)", 
            ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
        )

    with col2:
        longitude = st.number_input("Longitude", min_value=-74.25, max_value=-73.70, value=-74.0060, format="%.4f")
        number_of_reviews = st.number_input("Total Number of Reviews", min_value=0, max_value=1000, value=25)
        calculated_host_listings_count = st.number_input("Host Total Listings Count", min_value=1, max_value=300, value=1)
        
        room_type = st.selectbox(
            "Room Type", 
            ['Entire home/apt', 'Private room', 'Shared room']
        )
        
    availability_365 = st.slider("Yearly Availability (Days open per year)", min_value=0, max_value=365, value=180)
    
    # Form Submit Action Button
    submit_button = st.form_submit_button(label="🔮 Predict Nightly Price")

# --- 4. EXECUTE LIVE AUTOMATED INFERENCE ---
if submit_button:
    # Package inputs into a pandas dataframe mirroring the training layout precisely
    user_input_df = pd.DataFrame([{
        'latitude': latitude,
        'longitude': longitude,
        'minimum_nights': minimum_nights,
        'number_of_reviews': number_of_reviews,
        'reviews_per_month': reviews_per_month,
        'calculated_host_listings_count': calculated_host_listings_count,
        'availability_365': availability_365,
        'neighbourhood_group': neighbourhood_group,
        'room_type': room_type
    }])
    
    # Single-line prediction through pipeline workflow
    predicted_log = model_pipeline.predict(user_input_df)
    
    # Reverse log scaling to extract final clean dollar float value out of array
    final_usd_price = np.expm1(predicted_log)[0]
    
    # Display the final prediction output prominently to the user
    st.success(f"### 🎉 Estimated Price: **${final_usd_price:.2f}** per night")
