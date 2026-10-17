import streamlit as st

st.set_page_config(page_title="Weather-Based Crop Recommendation", page_icon="🌱", layout="centered")

st.title("🌦️ Weather-Based Crop Recommendation System")
st.write("Enter the local weather and soil details to get a simple crop suggestion.")
st.info("This is a beginner training demo using rule-based logic, not a trained machine-learning model. Actual crop choice also depends on season, location, soil nutrients, irrigation, and local agricultural advice.")

temperature = st.slider("Temperature (°C)", min_value=0, max_value=50, value=28)
humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=65)
rainfall = st.number_input("Expected rainfall (mm)", min_value=0.0, max_value=2000.0, value=600.0, step=25.0)
soil = st.selectbox("Soil type", ["Loamy", "Clayey", "Sandy", "Black"])

def recommend_crop(temp, hum, rain, soil_type):
    # Simple illustrative rules for an AI-training demonstration.
    if rain >= 800 and hum >= 65 and temp >= 20 and soil_type in ["Clayey", "Loamy"]:
        return "Rice 🌾", "Rice generally suits warm conditions with plentiful water and water-retentive soil."
    if 10 <= temp <= 25 and rain >= 250 and soil_type in ["Loamy", "Clayey", "Black"]:
        return "Wheat 🌾", "Wheat is commonly grown in cooler conditions with moderate water availability."
    if 20 <= temp <= 35 and 30 <= rain <= 1000 and soil_type in ["Loamy", "Sandy", "Black"]:
        return "Maize 🌽", "Maize can suit warm conditions and a range of well-drained soils."
    if temp >= 25 and rain < 500 and soil_type in ["Sandy", "Loamy", "Black"]:
        return "Millet (Bajra) 🌱", "Millets are often more suitable than water-demanding crops in hot, drier conditions."
    if temp >= 20 and rain >= 300 and hum >= 40:
        return "Pulses (e.g., mung bean) 🌿", "Some pulses can suit warm conditions; exact suitability depends on season and region."
    return "No clear match", "These simple rules did not find a strong match. Check local crop calendars and ask an agricultural expert."

if st.button("Recommend Crop", type="primary", use_container_width=True):
    crop, reason = recommend_crop(temperature, humidity, rainfall, soil)
    st.subheader("Recommendation")
    st.success(crop)
    st.write(reason)
    st.caption("Demo result only. Do not use this simple prototype as the sole basis for farm decisions.")

st.divider()
st.caption("AI Training Mini Project • Python + Streamlit")
