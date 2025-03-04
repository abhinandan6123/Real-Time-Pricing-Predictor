const [form, setForm] = useState({
    pickup_datetime: "",
    pickup_longitude: "",
    pickup_latitude: "",
    dropoff_longitude: "",
    dropoff_latitude: "",
    passenger_count: "1",
  });
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    const data = await response.json();
    setFare(data.predicted_fare);
  };
  