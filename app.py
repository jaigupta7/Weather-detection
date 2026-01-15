import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="Weather App", layout="wide")

st.title("🌍 Location Based Weather App")
st.write("Click the button below to allow location access and get weather info.")

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

    <div style="text-align:center; margin-top:30px;">
        <button onclick="getLocation()"
            style="
                padding: 15px 25px;
                font-size: 18px;
                border-radius: 10px;
                background-color: #1f77b4;
                color: white;
                border: none;
                cursor: pointer;">
            📍 Allow Location Access
        </button>
    </div>
    """,
    height=150
)

lat = st.query_params.get("lat")
lon = st.query_params.get("lon")

if lat and lon:
    st.success("📍 Location detected successfully!")
    st.write(f"Latitude: {lat}")
    st.write(f"Longitude: {lon}")

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    data = requests.get(weather_url).json()
    weather = data["current_weather"]

    st.subheader("🌦 Current Weather")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature (°C)", weather["temperature"])
    col2.metric("Wind Speed (km/h)", weather["windspeed"])
    col3.metric("Weather Code", weather["weathercode"])
