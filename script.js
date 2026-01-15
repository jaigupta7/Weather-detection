function getLocation() {
  if (!navigator.geolocation) {
    alert("Geolocation not supported");
    return;
  }

  navigator.geolocation.getCurrentPosition(success, error);
}

function success(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;

  fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`)
    .then(res => res.json())
    .then(data => {
      const weather = data.current_weather;
      document.getElementById("result").innerHTML = `
        <h3>🌦 Weather</h3>
        <p>Temperature: ${weather.temperature} °C</p>
        <p>Wind Speed: ${weather.windspeed} km/h</p>
      `;
    });
}

function error() {
  alert("Location access denied");
}
