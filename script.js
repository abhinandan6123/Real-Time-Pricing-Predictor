document.getElementById("predictForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const formData = {
        pickup_datetime: document.getElementById("pickup_datetime").value,
        pickup_latitude: parseFloat(document.getElementById("pickup_latitude").value),
        pickup_longitude: parseFloat(document.getElementById("pickup_longitude").value),
        dropoff_latitude: parseFloat(document.getElementById("dropoff_latitude").value),
        dropoff_longitude: parseFloat(document.getElementById("dropoff_longitude").value),
        passenger_count: parseInt(document.getElementById("passenger_count").value),
    };

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    });

    const data = await response.json();
    document.getElementById("fare").textContent = `$${data.predicted_fare}`;
});
