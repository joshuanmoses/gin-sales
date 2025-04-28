# gin_sales_gpt.py
"""
Gin Sales Predictor
--------------------
Predicts how much gin a distillery would sell based on the temperature of the day.

Author: Joshua N. Moses
Date: 2025
"""

import joblib

def load_model(model_path='gin_sales_model.pkl'):
    """Load the pre-trained gin sales prediction model."""
    return joblib.load(model_path)

def predict_sales(model, temperature):
    """Predict gin sales based on temperature."""
    return model.predict([[temperature]])[0]

def main():
    """Main function to run the sales predictor."""
    model = load_model()

    print("🍸 Welcome to the Gin Sales Predictor! 🍸\n")
    
    while True:
        user_input = input("Enter the temperature in degrees Celsius (or type 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye! Stay refreshed. 🍸")
            break
        
        try:
            temperature = float(user_input)
            prediction = predict_sales(model, temperature)
            print(f"🔮 Predicted Gin Sales: {prediction:.2f} liters\n")
        except ValueError:
            print("⚠️ Please enter a valid numeric temperature.\n")

if __name__ == "__main__":
    main()
