import numpy as np
import pandas as pd
import joblib  # Updated import
from flask import Flask, request, jsonify, render_template

# Initialize Flask app
app = Flask(__name__)

# Load the trained Stacking Model
model_path = "stacking_model.pkl"  # Update this with your trained model path
model = joblib.load(model_path)  # Use joblib to load the model

# Define route for UI
@app.route("/")
def home():
    return render_template("index.html")

# API route for price prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extracting user input from form
        data = request.form

        # Convert form inputs to float values
        features = np.array([
            float(data["Delivery_Distance_km"]),
            float(data["Package_Weight_kg"]),
            float(data["Delivery_Time_Est_min"]),
            float(data["Order_Value"]),
            float(data["Platform_Fees"]),
            float(data["Time_of_Day"]),
            float(data["Day_of_Week"]),
            float(data["Weather_Condition"]),
            float(data["Traffic_Index"]),
            float(data["Delivery_Location_Type"]),
            float(data["Discount_Applied"]),
            float(data["Surge_Multiplier"]),
            float(data["Fuel_Cost"])
        ]).reshape(1, -1)

        # Predict the best price
        predicted_price = model.predict(features)[0]

        # Return the result to the frontend
        return jsonify({"predicted_price": round(predicted_price, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)




