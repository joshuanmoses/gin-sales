import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import gradio as gr

# 🧠 Model container (global so we can load after file upload)
model = None
features = None

def load_data(file):
    global model, features

    # Load Excel or CSV
    if file.name.endswith('.csv'):
        df = pd.read_csv(file.name)
    else:
        df = pd.read_excel(file.name)

    # Check required columns
    required_cols = {'Temperature', 'Gin_Sales'}
    if not required_cols.issubset(df.columns):
        return "❌ Spreadsheet must include columns: Temperature, Gin_Sales"

    # Drop rows with missing values
    df = df.dropna(subset=['Temperature', 'Gin_Sales'])

    # Train model
    X = df[['Temperature']]
    y = df['Gin_Sales']
    model = LinearRegression()
    model.fit(X, y)

    features = df.columns.tolist()
    return f"✅ Model trained on {len(df)} records."

def predict_sales(temp):
    if model is None:
        return "⚠️ Please upload a spreadsheet first."
    pred = model.predict([[temp]])[0]
    return f"📦 Predicted gin sales: {pred:.2f} units"

# 🎛️ Gradio UI
upload = gr.File(label="📄 Upload Spreadsheet (CSV/XLSX)")
temp_input = gr.Number(label="🌡️ Temperature (°F)")
output = gr.Textbox(label="🔮 Prediction")

iface = gr.Interface(
    fn=predict_sales,
    inputs=temp_input,
    outputs=output,
    title="🍸 Gin Sales Predictor GPT",
    description="Upload your historical gin sales data to train the model, then input a temperature to predict future sales.",
    live=False
)

iface.load(fn=None, inputs=None, outputs=None)  # Just to trigger UI render
iface.upload(load_data, inputs=upload, outputs="text")

iface.launch()
