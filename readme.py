# 📦 Vendor Invoice Intelligence Portal

An AI-driven predictive supply chain intelligence pipeline featuring a multi-model dashboard designed to forecast freight logistics costs and detect high-risk or anomalous vendor financial transactions.

---

## 📂 Project Architecture

```text
├── freight_cost_prediction/
│   ├── train.py                 # Core orchestration script for model training 
│   ├── data_preprocessing.py    # Freight SQL pipeline & simple feature mapping
│   └── model_evaluation.py      # Regression model tuning suite
├── invoice_flagging/
│   ├── train.py                 # Classification training script
│   ├── data_preprocessing.py    # Complex SQL joins, risk-labeling rules & scaling
│   └── model_evaluation.py      # Classification tuning & hyperparameter grids
├── inference/
│   ├── predict_freight.py       # Isolated production regression model runtime 
│   └── predict_invoice_flag.py  # Isolated production classification model runtime
├── models/
│   ├── predict_freight_model.pkl   # Serialized champion regression model 
│   ├── invoice_flagging_model.pkl  # Serialized champion classification model
│   └── invoice_flagging_scaler.pkl # Serialized production StandardScaler object
├── app.py                       # Modular multi-page Streamlit web dashboard interface
└── README.md                    # Operational project handbook
```

---

## 🛠️ Step 1: Environment Installation

Ensure Python 3.8+ is installed on your local operating system. Install all necessary machine learning dependencies via your command-line terminal interface:

```bash
pip install pandas numpy scikit-learn joblib streamlit sqlite3
```

---

## ⚙️ Step 2: Training the Models

Before running inference routines or launching the front-end interface, execute both localized machine learning scripts sequentially to generate the underlying tracking binaries within your tracking directories.

### 1. Train Freight Regression Engine
```bash
python freight_cost_prediction/train.py
```
* **Process:** Connects to the inventory SQLite database, isolates spatial feature layers, isolates the target vector, evaluates multiple regressors, and serializes the winning framework configuration directly into `models/predict_freight_model.pkl`.

### 2. Train Invoice Risk Classifier
```bash
python invoice_flagging/train.py
```
* **Process:** Compiles granular SQL multi-table join rules, computes mathematical deviations between system thresholds and raw distributions, executes hyperparameter search patterns, and saves both the optimal network model and standard scaling transformer configurations down to your production file paths.

---

## 🚀 Step 3: Running Production Inference

Validate model inputs using isolated standalone local scripts before passing elements out to UI endpoints:

### Run Freight Predictive Inference
```bash
python inference/predict_freight.py
```

### Run Automated Risk Auditing Inference
```bash
python inference/predict_invoice_flag.py
```

---

## 🖥️ Step 4: Launching the Web Interface Portal

Initialize the Streamlit multi-model environment engine directly out of your primary root workspace directory path:

```bash
streamlit run app.py
```

* This action initializes a local web server (typically running over `localhost:8501`) mapping complete features out to user widgets for interactive evaluation.

---

## 🛡️ Live Auditing Rules Applied (Invoice Flagging Tool)
* **Financial Delta Verification:** Flags any transaction where absolute ledger mismatch values breach the strict **$5 boundary gap limits**.
* **Logistics Window Latency Check:** Flags processing timelines indicating tracking pipeline structural backlogs processing over **10 operational lag days**.
*