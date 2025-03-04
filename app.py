from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from geopy.distance import geodesic

# Load the trained model
with open("model_xgb.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

# Function to calculate distance
def calculate_distance(pickup_lat, pickup_long, dropoff_lat, dropoff_long):
    return geodesic((pickup_lat, pickup_long), (dropoff_lat, dropoff_long)).km

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Get user input
            pickup_longitude = float(request.form["pickup_longitude"])
            pickup_latitude = float(request.form["pickup_latitude"])
            dropoff_longitude = float(request.form["dropoff_longitude"])
            dropoff_latitude = float(request.form["dropoff_latitude"])
            passenger_count = int(request.form["passenger_count"])
            pickup_datetime = request.form["pickup_datetime"]
            
            # Convert pickup time to features
            pickup_datetime = pd.to_datetime(pickup_datetime)
            distance = calculate_distance(pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude)
            hour = pickup_datetime.hour
            day = pickup_datetime.day
            month = pickup_datetime.month
            day_of_week = pickup_datetime.dayofweek
            is_weekend = 1 if day_of_week > 4 else 0
            is_rush_hour = 1 if hour in [7, 8, 9, 16, 17, 18] else 0

            # Prepare input for model
            features = np.array([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, 
                                  passenger_count, distance, hour, day, month, day_of_week, is_weekend, is_rush_hour]])
            
            # Predict the price
            predicted_price = model.predict(features)[0]
            
            return render_template("index.html", prediction=round(predicted_price, 2))

        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)



