import pandas as pd
from sklearn.linear_model import LinearRegression
import gradio as gr
import pickle
import numpy as np

# Load or simulate data
def create_synthetic_data():
    temps = np.random.uniform(50, 100, 200)
    sales = 20 + (temps - 50) * 3 + np.random.normal(0, 10, 200)  # Some randomness
    return pd.DataFrame({"Temperature": temps, "Gin_Sales": sales})

df = create_synthetic_data()

# Train model
model = LinearRegression()
model.fit(df[["Temperature"]], df["Gin_Sales"])

# Save model (optional)
with open("gin_sales_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Prediction function
def predict_sales(temp):
    pred = model.predict([[temp]])
    return f"📦 Predicted gin sales: {pred[0]:.2f} liters"

# Launch Gradio interface
gr.Interface(
    fn=predict_sales,
    inputs=gr.Number(label="🌡️ Temperature (°F)"),
    outputs="text",
    title="🍸 Gin Sales Predictor",
    description="Predict how much gin will be sold based on today's temperature."
).launch()
