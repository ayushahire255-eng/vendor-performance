import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Vendor Performance Portal",
    page_icon="📊",
    layout="wide"
)

# --- BACKEND ARTIFACT LOADERS ---
@st.cache_resource
def load_freight_benchmarks():
    path = Path("models/predict_freight_model.pkl")
    return joblib.load(path) if path.exists() else None

@st.cache_resource
def load_audit_artifacts():
    model_path = Path("models/predict_flag_invoice.pkl")
    scaler_path = Path("models/scaler.pkl")
    if not model_path.exists() or not scaler_path.exists():
        return None, None
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    with open(scaler_path, "rb") as f:
        scaler = joblib.load(f)
    return model, scaler

freight_calc = load_freight_benchmarks()
audit_calc, audit_scaler = load_audit_artifacts()

# ==============================================================================
# 🎛️ VERTICAL SIDEBAR NAVIGATION ARCHITECTURE
# ==============================================================================
with st.sidebar:
    st.title("⚙️ Control Center")
    st.markdown("Select an analytical operational layer:")
    
    # This radio box creates the vertical tab menu selection interface on the left side
    navigation_selection = st.radio(
        "Navigation",
        [
            "🚚 Freight Cost Analytics",
            "🛡️ Invoice Risk Profiling",
            "📈 Executive Trend Dashboard"
        ],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("🔒 System Security: Data Extraction isolated securely via SQLite pipelines.")

# ==============================================================================
# MAIN PAGE AREA - DYNAMICALLY CHANGES BASED ON VERTICAL SELECTION
# ==============================================================================
st.title("📊 Vendor Performance Portal")
st.markdown("### Automated Ledger Analytics & Operational Discrepancy Profiling")
st.markdown("---")

# ------------------------------------------------------------------------------
# TRACK 1: LOGISTICS COST ANALYSIS
# ------------------------------------------------------------------------------
if navigation_selection == "🚚 Freight Cost Analytics":
    st.header("🚚 Logistics Freight Expenditure Benchmarking")
    st.markdown("Project baseline logistics costs based on transactional parameters to identify overcharging risks.")
    
    if freight_calc is None:
        st.error("❌ System Link Incomplete: Missing reference benchmark at `models/predict_freight_model.pkl`.")
    else:
        with st.form("freight_form"):
            dollars_input = st.number_input("Invoice Base Valuation ($)", min_value=0.0, value=1500.0, step=50.0)
            submit_freight = st.form_submit_button("Calculate Cost Benchmarks", type="primary")
            
        if submit_freight:
            payload = pd.DataFrame({"Dollars": [dollars_input]})
            raw_prediction = freight_calc.predict(payload)
            st.success("Ledger analysis calculation completed successfully!")
            st.metric(label="Calculated Freight Allocation Reference", value=f"${round(float(raw_prediction), 2)}")

# ------------------------------------------------------------------------------
# TRACK 2: AUDIT RISK DETECTION
# ------------------------------------------------------------------------------
elif navigation_selection == "🛡️ Invoice Risk Profiling":
    st.header("🛡️ Procurement Audit Discrepancy Profiling")
    st.markdown("Input vendor ledger metrics to screen compliance scores and isolate transactions needing review.")
    
    if audit_calc is None or audit_scaler is None:
        st.error("❌ System Link Incomplete: Missing reference profiles inside your `models/` directory.")
    else:
        with st.form("flagging_form"):
            col1, col2 = st.columns(2)
            with col1:
                total_brands = st.number_input("Total Distinct Brands on PO", min_value=1, value=2, step=1)
                total_item_quantity = st.number_input("Total Item Quantity Ordered", min_value=1, value=50, step=5)
                total_item_dollars = st.number_input("Procurement Order Valuation ($)", min_value=0.0, value=1500.0, step=50.0)
            with col2:
                invoice_dollars = st.number_input("Disbursed Vendor Invoice Value ($)", min_value=0.0, value=1580.0, step=50.0)
                freight = st.number_input("Invoiced Logistics Charges ($)", min_value=0.0, value=45.0, step=5.5)
                avg_receiving_delay = st.number_input("Mean Warehouse Processing Latency (Days)", min_value=0.0, value=4.2, step=0.5)
                
            submit_flagging = st.form_submit_button("Analyze Invoice Integrity", type="primary")
            
        if submit_flagging:
            feature_cols = ['total_brands', 'total_item_quantity', 'total_item_dollars', 'invoice_dollars', 'Freight', 'avg_receiving_delay']
            payload = pd.DataFrame([[total_brands, total_item_quantity, total_item_dollars, invoice_dollars, freight, avg_receiving_delay]], columns=feature_cols)
            
            scaled_features = audit_scaler.transform(payload)
            prediction_flag = audit_calc.predict(scaled_features)
            probability_metrics = audit_calc.predict_proba(scaled_features)
            
            st.markdown("---")
            st.subheader("Automated Compliance Diagnostic Results")
            
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                if int(prediction_flag) == 1:
                    st.error("🚨 HIGH RISK FLAGGED: Transaction contains structural discrepancies. Manual Audit Recommended.")
                else:
                    st.success("✅ COMPLIANCE PASS: Document parameters sit within acceptable operational thresholds.")
            with res_col2:
                st.metric(label="Calculated Ledger Risk Probability", value=f"{round(float(probability_metrics[0][1]) * 100, 2)}%")

# ------------------------------------------------------------------------------
# TRACK 3: ANALYTICS VISUALIZATION DASHBOARD
# ------------------------------------------------------------------------------
elif navigation_selection == "📈 Executive Trend Dashboard":
    st.header("📈 Procurement Metrics & Cost Leakage Analysis")
    st.markdown("Interactive trending charts mapping supply chain key performance indicators (KPIs).")
    
    vis_col1, vis_col2 = st.columns(2)
    with vis_col1:
        st.subheader("📊 Projected Logistics Costs vs Invoice Valuation")
        mock_invoice_range = np.linspace(100, 10000, 50)
        if freight_calc is not None:
            mock_preds = freight_calc.predict(pd.DataFrame({"Dollars": mock_invoice_range}))
            chart_data = pd.DataFrame({"Invoice Base ($)": mock_invoice_range, "Benchmark Freight Cost ($)": mock_preds})
            st.line_chart(chart_data.set_index("Invoice Base ($)"))
            
    with vis_col2:
        st.subheader("⏳ Inbound Shipping Latency Distribution")
        delay_categories = ["Fast-Track (<3 days)", "Standard Turnaround (3-7 days)", "Bottleneck Delay (>10 days)"]
        mock_volumes = [142, 385, 64]
        bar_chart_data = pd.DataFrame({"Operational Status": delay_categories, "Invoice Count": mock_volumes})
        st.bar_chart(bar_chart_data.set_index("Operational Status"))