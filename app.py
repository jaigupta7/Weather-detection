import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="Weather App", page_icon="🌦")

st.title("🌍 Location Based Weather App")

# JavaScript to get browser location
components.html(
    """
    <script>
    function getLocation() {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                const url = `/?lat=${lat}&lon=${lon}`;
                window.location.href = url;
            }
        );
    }
    </script>

    <button onclick="getLocation()">📍 Allow Location Access</button>
    """,
    height=100
)

# Read latitude & longitude from URL
lat = st.query_params.get("lat")
lon = st.query_params.get("lon")

if lat and lon:
    st.success("📍 Location detected!")
    st.write(f"Latitude: {lat}")
    st.write(f"Longitude: {lon}")

    # Call Open-Meteo API
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    response = requests.get(weather_url).json()
    weather = response["current_weather"]

    st.subheader("🌦 Current Weather")
    st.metric("Temperature (°C)", weather["temperature"])
    st.metric("Wind Speed (km/h)", weather["windspeed"])
    st.write("Weather Code:", weather["weathercode"])
