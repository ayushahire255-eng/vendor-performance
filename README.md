# 🚀 Vendor Performance Analytics & Invoice Risk Prediction

An end-to-end Data Analytics and Machine Learning project that analyzes vendor purchasing performance, predicts high-risk invoices, and provides business insights using SQL, Python, Power BI, Machine Learning, and Streamlit.

---

# 📌 Project Overview

Procurement teams process thousands of purchase orders and vendor invoices every year. Manual invoice verification is time-consuming and error-prone.

This project builds a complete analytics pipeline to:

- Analyze vendor purchasing performance
- Monitor procurement spending
- Predict high-risk invoices using Machine Learning
- Visualize procurement KPIs in Power BI
- Deploy the prediction model using Streamlit

---

# 🎯 Business Problem

Organizations often face:

- High procurement costs
- Delayed invoice verification
- Manual fraud detection
- Vendor performance issues
- Poor visibility into purchasing trends

The objective is to support procurement teams with data-driven insights and automated invoice risk prediction.

---

# 🏗 Project Architecture

```
SQLite Database
        │
        ▼
SQL Queries
        │
        ▼
Python Data Processing
        │
        ▼
Machine Learning Model
(Random Forest Classifier)
        │
        ▼
Streamlit Prediction App
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Decision Support
```

---

# 📊 Dataset

The project uses an inventory procurement database containing:

- Purchases
- Vendor Invoice
- Purchase Prices
- Beginning Inventory
- Ending Inventory

The data was exported from SQLite into CSV files for Power BI reporting.

---

# 🛠 Technologies Used

- Python
- SQL (SQLite)
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Power BI
- Streamlit
- Git & GitHub

---

# 🤖 Machine Learning Model

## Problem Type

Binary Classification

Target Variable

Invoice Flag

Algorithms Tested

- Linear Regression
- Decision Tree
- Random Forest

Selected Model

✅ Random Forest Classifier

Reason:
It achieved the best predictive performance after hyperparameter tuning using GridSearchCV.

---

# 📈 Model Performance

| Metric | Value |
|---------|--------|
| Accuracy | **95.49%** |
| Precision (Class 0) | 94% |
| Precision (Class 1) | 100% |
| Recall (Class 0) | 100% |
| Recall (Class 1) | 87% |
| F1 Score (Class 0) | 97% |
| F1 Score (Class 1) | 93% |

---

# 📉 Confusion Matrix

![Confusion Matrix](confusion_matrix.png) 
<img width="1523" height="1298" alt="confusion_matrix" src="https://github.com/user-attachments/assets/e7cdf180-937a-4755-a49a-7c5d886150d4" />


The model correctly classified **1,059 out of 1,109 invoices** while maintaining high precision for risky invoices.

---

# 📊 Power BI Dashboard

The dashboard consists of three pages.

## Page 1 – Vendor Performance Overview

- Total Purchase Orders
- Total Procurement Spend
- Vendor Count
- Freight Cost
- Top Vendors
- Monthly Purchase Trend

---

## Page 2 – Vendor Insights

- Vendor Spend Distribution
- Vendor Purchase Analysis
- Freight Analysis
- Procurement Trends
- Vendor Comparison

---

## Page 3 – Machine Learning Insights

- Model Accuracy
- Precision
- Recall
- F1 Score
- Random Forest Details
- Confusion Matrix
- Business Recommendations

---

# 🌐 Streamlit Application

The Streamlit application allows users to:

- Enter procurement information
- Predict invoice risk
- Estimate freight cost
- View analytics
- Support procurement decision-making

---

# 💼 Business Recommendations

- Prioritize manual review of high-risk invoices.
- Monitor vendors with unusually high freight costs.
- Reduce manual invoice verification effort using ML predictions.
- Continuously retrain the model with new procurement data.
- Combine dashboard insights with ML predictions for better procurement decisions.

---

# 📂 Project Structure

```
Vendor-Performance/
│
├── data/
├── invoice_flagging/
├── freight_cost_prediction/
├── models/
├── notebooks/
├── app.py
├── export_to_csv.py
├── purchases.csv
├── vendor_invoice.csv
├── purchase_prices.csv
├── begin_inventory.csv
├── end_inventory.csv
├── Vendor_Performance_Dashboard.pbix
├── confusion_matrix.png
├── requirements.txt
└── README.md
```

---

# ▶️ Run Locally

Clone the repository

```bash
git clone https://github.com/ayushahire255-eng/vendor-performance.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 📸 Screenshots

## Power BI Dashboard

> Add screenshots of:
- Dashboard Page 1 <img width="1325" height="746" alt="Screenshot 2026-07-30 155017" src="https://github.com/user-attachments/assets/e8ce85ae-7200-4093-8941-f6c14d36f6c8" />

- Dashboard Page 2 <img width="1311" height="737" alt="Screenshot 2026-07-30 155037" src="https://github.com/user-attachments/assets/c1bf1f7e-e3d5-4acb-b49c-b24e701b212d" />

- Dashboard Page 3 <img width="1313" height="740" alt="Screenshot 2026-07-30 155100" src="https://github.com/user-attachments/assets/4f794371-d00d-407f-b742-936a4a4d93d6" />


---

## Streamlit App

> Add screenshots of:
- Home Page <img width="1158" height="658" alt="Screenshot 2026-07-30 155451" src="https://github.com/user-attachments/assets/29839dfe-abdb-4d8e-823f-b813688bf1a2" />

- Prediction Page <img width="1908" height="799" alt="Screenshot 2026-07-30 155606" src="https://github.com/user-attachments/assets/736dc411-75f9-45e7-8151-2e557b9f2ab7" />

- Analytics Page <img width="1919" height="890" alt="Screenshot 2026-07-30 155630" src="https://github.com/user-attachments/assets/dda94d16-a4f0-45b2-811c-7a0bfae964e8" />


---

# 📌 Future Improvements

- Deploy on Azure
- Connect to SQL Server
- Automate model retraining
- Add real-time data pipeline
- Implement explainable AI (SHAP)

---

# 👨‍💻 Author

**Ayush Ahire**

GitHub:
https://github.com/ayushahire255-eng

---

## ⭐ If you found this project useful, consider giving it a star!
