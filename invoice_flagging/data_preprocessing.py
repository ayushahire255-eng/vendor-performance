import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_invoice_data():
    # 1. Connected directly to your local Windows database location
    db_path = r"C:\Users\ADMIN\Downloads\inventory (1).db"
    conn = sqlite3.connect(db_path)
    
    # 2. Combined SQL aggregation query adjusted for your database tables
    query = """
    WITH purchase_agg AS (
        SELECT 
            p.PO_Number,
            COUNT(DISTINCT p.Brand) AS total_brands,
            SUM(p.Quantity) AS total_item_quantity,
            SUM(p.Dollars) AS total_item_dollars,
            AVG(julianday(p.ReceivingDate) - julianday(p.PODate)) AS avg_receiving_delay
        FROM purchase p
        GROUP BY p.PO_Number
    )
    SELECT 
        vi.PO_Number,
        vi.Quantity AS invoice_quantity,
        vi.Dollars AS invoice_dollars,
        vi.Freight,
        pa.total_brands,
        pa.total_item_quantity,
        pa.total_item_dollars,
        pa.avg_receiving_delay
    FROM vendor_invoice vi
    INNER JOIN purchase_agg pa ON vi.PO_Number = pa.PO_Number;
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def create_invoice_risk_label(row):
    # Rule-based labeling logic from the classification section
    if abs(row["invoice_dollars"] - row["total_item_dollars"]) > 5:
        return 1
    if row["avg_receiving_delay"] > 10:
        return 1
    return 0

def prepare_features(df: pd.DataFrame):
    # Apply labeling to generate target variable y
    df["flag_invoice"] = df.apply(create_invoice_risk_label, axis=1)
    
    # Isolate inputs (X) and target (y)
    feature_cols = ['total_brands', 'total_item_quantity', 'total_item_dollars', 'invoice_dollars', 'Freight', 'avg_receiving_delay']
    X = df[feature_cols]
    y = df['flag_invoice']
    return X, y

def split_and_scale_data(X, y):
    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler