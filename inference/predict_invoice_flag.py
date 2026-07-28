import joblib
import pandas as pd
import numpy as np

MODEL_PATH = "models/invoice_flagging_model.pkl"
SCALER_PATH = "models/invoice_flagging_scaler.pkl"

def load_artifacts():
    """
    Load the trained classification model and its corresponding scaler binary.
    """
    with open(MODEL_PATH, "rb") as f:
        model = joblib.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler = joblib.load(f)
    return model, scaler

def predict_invoice_flags(input_data):
    """
    Predict risk flags for incoming invoices using the scaled feature pipeline.
    """
    model, scaler = load_artifacts()
    
    # 1. Convert live input dictionary to DataFrame
    input_df = pd.DataFrame(input_data)
    
    # 2. Arrange features in the exact structural order the model expects
    feature_cols = [
        'total_brands', 
        'total_item_quantity', 
        'total_item_dollars', 
        'invoice_dollars', 
        'Freight', 
        'avg_receiving_delay'
    ]
    X_inference = input_df[feature_cols]
    
    # 3. Transform inputs using the saved production scaler configuration
    X_scaled = scaler.transform(X_inference)
    
    # 4. Generate predictions and probability arrays
    input_df['Flag_Prediction'] = model.predict(X_scaled)
    input_df['Risk_Probability'] = np.round(model.predict_proba(X_scaled)[:, 1], 4)
    
    return input_df

if __name__ == "__main__":
    # Test batch matching the schema of your database aggregation
    sample_data = {
        "total_brands":,
        "total_item_quantity":,
        "total_item_dollars": [1500.00, 200.00, 12000.00],
        "invoice_dollars": [1580.00, 200.00, 12000.00],  # Row 0 has variance (> $5 mismatch)
        "Freight": [45.00, 12.00, 350.00],
        "avg_receiving_delay": [4.2, 15.5, 2.1]         # Row 1 has high delay (> 10 days)
    }
    
    print("Running invoice risk assessment inference...")
    predictions = predict_invoice_flags(sample_data)
    print("\n", predictions)