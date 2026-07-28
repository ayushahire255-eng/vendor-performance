import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"

def load_model(model_path: str = MODEL_PATH):
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model
    
def predict_invoice_flag(input_data):
    model = load_model()
    
    # 1. Convert input data to DataFrame
    input_df = pd.DataFrame(input_data)
    
    # 2. Force the model to only read the 'Dollars' column to match train.py exactly
    X_inference = input_df[['Dollars']]
    
    # 3. Predict the actual freight cost
    input_df['Predicted_Freight'] = model.predict(X_inference).round(2)
    return input_df

if __name__ == "__main__":
    # Test dataset
    sample_data = {
        "Dollars": [18500, 9000, 3000, 200]
    }
    
    prediction = predict_freight_cost(sample_data)
    print(prediction)