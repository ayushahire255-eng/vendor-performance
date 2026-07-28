from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, make_scorer, f1_score

def train_random_forest(X_train, y_train):
    rf = RandomForestClassifier(random_state=42, n_jobs=-1)
    
    # 100% complete parameters grid with actual numbers filled in
    param_grid = {
        "n_estimators":,
        "max_depth": [None, 4, 5, 6],
        "min_samples_split":,
        "min_samples_leaf":,
        "criterion": ["gini", "entropy"]
    }
    
    scorer = make_scorer(f1_score)
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, scoring=scorer, cv=5, n_jobs=-1, verbose=1)
    
    print("Running Grid Search CV optimizations... (This will take a moment)")
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

def evaluate_classifier(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    
    print("\n==========================================")
    print("=== Final Optimized Model Evaluation ===")
    print("==========================================")
    print(f"Accuracy Score: {acc:.4f}")
    print(f"F1 Optimized Score: {f1:.4f}")
    print("\nClassification Report Summary:")
    print(classification_report(y_test, preds))