import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Supply Chain Analytics Dashboard",
    page_icon="📦",
    layout="wide"
)

# --- DIRECT MODEL LOADING FOR ACCURACY ---
@st.cache_resource
def load_freight_model():
    model_path = Path("models/predict_freight_model.pkl")
    if not model_path.exists():
        return None
    with open(model_path, "rb") as f:
        return joblib.load(f)

@st.cache_resource
def load_flagging_artifacts():
    model_path = Path("models/predict_flag_invoice.pkl")
    scaler_path = Path("models/scaler.pkl")
    if not model_path.exists() or not scaler_path.exists():
        return None, None
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    with open(scaler_path, "rb") as f:
        scaler = joblib.load(f)
    return model, scaler

freight_model = load_freight_model()
flag_model, flag_scaler = load_flagging_artifacts()

# --- UI HEADER ---
st.title("📦 Supply Chain Predictive Diagnostics")
st.markdown("Run live inference using your production machine learning workflows.")

# --- NAVIGATION SIDEBAR ---
app_mode = st.sidebar.selectbox(
    "Choose Analytics Tool",
    ["Freight Cost Estimator", "Invoice Risk Flagging"]
)

# ==============================================================================
# WORKFLOW 1: FREIGHT COST ESTIMATOR
# ==============================================================================
if app_mode == "Freight Cost Estimator":
    st.header("🚚 Freight Cost Estimator (Regression)")
    
    if freight_model is None:
        st.error("❌ Missing production file: `models/predict_freight_model.pkl`. Please run your training pipeline first.")
    else:
        st.info("Input the invoice dollar metric below to project the freight baseline cost.")
        dollars_input = st.number_input("Invoice Dollars ($)", min_value=0.0, value=1500.0, step=50.0)
        
        if st.button("Predict Freight Cost", type="primary"):
            input_df = pd.DataFrame({"Dollars": [dollars_input]})
            prediction = freight_model.predict(input_df)[0]
            
            st.success("Prediction calculated successfully!")
            st.metric(label="Estimated Freight Cost", value=f"${round(prediction, 2)}")

# ==============================================================================
# WORKFLOW 2: INVOICE RISK FLAGGING
# ==============================================================================
elif app_mode == "Invoice Risk Flagging":
    st.header("🛡️ Invoice Risk Detection & Flagging (Classification)")
    
    if flag_model is None or flag_scaler is None:
        st.error("❌ Missing production artifacts in your `models/` directory.")
    else:
        st.markdown("### Input Live Inbound Invoice Metrics")
        col1, col2 = st.columns(2)
        with col1:
            total_brands = st.number_input("Total Distinct Brands on PO", min_value=1, value=2, step=1)
            total_item_quantity = st.number_input("Total Ordered Item Quantity", min_value=1, value=50, step=5)
            total_item_dollars = st.number_input("Total Ordered System Value ($)", min_value=0.0, value=1500.0, step=50.0)
        with col2:
            invoice_dollars = st.number_input("Vendor Invoice Disbursed Dollars ($)", min_value=0.0, value=1580.0, step=50.0)
            freight = st.number_input("Invoiced Freight Charges ($)", min_value=0.0, value=45.0, step=5.0)
            avg_receiving_delay = st.number_input("Average Receiving Window Delay (Days)", min_value=0.0, value=4.2, step=0.5)
            
        if st.button("Evaluate Invoice Integrity", type="primary"):
            raw_data = {
                'total_brands': [total_brands],
                'total_item_quantity': [total_item_quantity],
                'total_item_dollars': [total_item_dollars],
                'invoice_dollars': [invoice_dollars],
                'Freight': [freight],
                'avg_receiving_delay': [avg_receiving_delay]
            }
            input_df = pd.DataFrame(raw_data)
            feature_cols = ['total_brands', 'total_item_quantity', 'total_item_dollars', 'invoice_dollars', 'Freight', 'avg_receiving_delay']
            X_inference = input_df[feature_cols]
            
            X_scaled = flag_scaler.transform(X_inference)
            prediction_flag = flag_model.predict(X_scaled)[0]
            probability_score = flag_model.predict_proba(X_scaled)[0][1]
            
            st.markdown("---")
            st.subheader("Diagnostic Assessment Results")
            
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                if prediction_flag == 1:
                    st.error("🚨 CRITICAL WARNING: Invoice Flagged as High Risk")
                else:
                    st.success("✅ PASS: Invoice Cleared / Standard Activity Profile")
            with res_col2:
                st.metric(label="Calculated Audit Probability Score", value=f"{round(probability_score * 100, 2)}%")