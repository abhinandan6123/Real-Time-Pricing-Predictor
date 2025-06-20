

---

# 🚖 Real-Time Pricing Predictor

[🔗 Live Website](https://real-time-pricing-predictor.onrender.com)

An end-to-end machine learning web application that predicts **real-time ride prices** based on various trip-related factors. Inspired by pricing models of platforms like **Ola**, **Uber**, and **Rapido**, this project merges **data science** and **web development** into a live, deployable product.

---

## 🧠 Overview

This project includes the complete **ML lifecycle**:

* Data Cleaning & Feature Engineering
* Exploratory Data Analysis (EDA)
* Model Selection & Hyperparameter Tuning
* Model Deployment with Flask
* UI Integration & Cloud Hosting

---

## 🚀 Features

* 🔍 Predicts ride price based on:

  * Pickup & Dropoff details
  * Time, day, and distance
  * Passenger count and rush hour flags
* 📊 Real-time pricing via user-friendly interface
* 🧠 High-accuracy **XGBoost** model
* 🌐 Deployed and live on **Render**

---

## 📥 Input Fields

The model currently uses:

* `pickup_longitude`, `pickup_latitude`
* `dropoff_longitude`, `dropoff_latitude`
* `passenger_count`, `distance`
* `hour`, `day`, `month`, `day_of_week`
* `is_weekend`, `is_rush_hour`

---

## 💡 Upcoming Enhancements

🔄 We’re continuously improving this project! Planned features:

* 🗺️ **Map Integration**: Allow users to select pickup & dropoff using an interactive map
* 🚗 **Vehicle Type Selection**: Pricing adjustments based on type (e.g., bike, sedan, SUV)
* 📍 **Direct Location Input**: Replace latitude/longitude with human-friendly address or location names
* 🌐 **Geo-APIs**: Auto-fetch coordinates via Google Maps or OpenStreetMap
* 💬 **Real-time fare estimate comparison** (Premium)

---

## 🛠️ Tech Stack

* **Python**, **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
* **XGBoost**, **Scikit-learn**, **Optuna**
* **Flask** for backend APIs
* **HTML**, **CSS**, **JavaScript** for frontend
* **Render** for deployment

---

## 🧪 Model Performance

* ✅ Final Model: **XGBoost Regressor**
* 📈 Accuracy:

  * R² Score: `0.96+`
  * MAE: Very low
* 🎯 Optimized using **Optuna** with 20+ trials

---

## 📂 Project Structure

```
real-time-pricing-predictor/
│
├── templates/              # HTML files
├── static/                 # CSS, JS, images
├── model/                  # Trained model (xgb_model.json)
├── app.py                  # Main Flask application
├── requirements.txt        # Package dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Run Locally

```bash
git clone https://github.com/your-username/real-time-pricing-predictor.git
cd real-time-pricing-predictor
pip install -r requirements.txt
python app.py
```

Then go to `http://localhost:5000` in your browser.

---

## 🌍 Deployment

✅ **Live & hosted on Render**
🔗 [Live Demo](https://real-time-pricing-predictor.onrender.com)

---

## 👨‍💻 Developed By

**Venkata Abhinandan Kancharla**
Aspiring Machine Learning Engineer
🔗 [Portfolio](https://abhikancharla.vercel.app) | [LinkedIn](https://linkedin.com/in/abhinandan6123) | [GitHub](https://github.com/abhinandan6123)

---

## 🏷️ Tags

`Machine Learning` `Ride Pricing` `Deployment` `XGBoost` `Flask` `Real-Time Prediction` `End-to-End Project` `Retail Tech` `Smart Mobility`

---

Let me know if you want this in markdown file format or with GitHub-style badges and a screenshot preview at the top!
