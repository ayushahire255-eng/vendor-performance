import sqlite3
import joblib
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, make_scorer, f1_score

def load_invoice_data():
    db_path = r"C:\Users\ADMIN\Downloads\inventory (1).db"
    conn = sqlite3.connect(db_path)
    query = """
    WITH purchases_agg AS (
        SELECT 
            p.PONumber,
            COUNT(DISTINCT p.Brand) AS total_brands,
            SUM(p.Quantity) AS total_item_quantity,
            SUM(p.Dollars) AS total_item_dollars,
            AVG(julianday(p.ReceivingDate) - julianday(p.PODate)) AS avg_receiving_delay
        FROM purchases p
        GROUP BY p.PONumber
    )
    SELECT 
        vi.PONumber,
        vi.Quantity AS invoice_quantity,
        vi.Dollars AS invoice_dollars,
        vi.Freight,
        pa.total_brands,
        pa.total_item_quantity,
        pa.total_item_dollars,
        pa.avg_receiving_delay
    FROM vendor_invoice vi
    INNER JOIN purchases_agg pa ON vi.PONumber = pa.PONumber;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def create_invoice_risk_label(row):
    if abs(row["invoice_dollars"] - row["total_item_dollars"]) > 5:
        return 1
    if row["avg_receiving_delay"] > 10:
        return 1
    return 0

def main():
    model_dir = Path("models")
    model_dir.mkdir(exist_ok=True)
    
    print("Loading database and running queries...")
    df = load_invoice_data()
    
    df["flag_invoice"] = df.apply(create_invoice_risk_label, axis=1)
    feature_cols = ['total_brands', 'total_item_quantity', 'total_item_dollars', 'invoice_dollars', 'Freight', 'avg_receiving_delay']
    X = df[feature_cols]
    y = df['flag_invoice']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    joblib.dump(scaler, model_dir / 'scaler.pkl')
    print("Successfully saved data scaler.")
    
    # Fully filled parameters grid embedded inside the file
    param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 4, 5, 6],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "criterion": ["gini", "entropy"]
    }
    
    print("Running Grid Search CV optimizations...")
    rf = RandomForestClassifier(random_state=42, n_jobs=-1)
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, scoring=make_scorer(f1_score), cv=5, n_jobs=-1, verbose=1)
    grid_search.fit(X_train_scaled, y_train)
    best_rf_model = grid_search.best_estimator_
    
    print("\nEvaluating model performance...")
    preds = best_rf_model.predict(X_test_scaled)
    print(f"Accuracy Score: {accuracy_score(y_test, preds):.4f}")
    print(classification_report(y_test, preds))
    
    joblib.dump(best_rf_model, model_dir / 'predict_flag_invoice.pkl')
    print("Successfully saved final production classifier file asset.")

if __name__ == "__main__":
    main()