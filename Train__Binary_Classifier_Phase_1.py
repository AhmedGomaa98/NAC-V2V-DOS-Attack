import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib 

# 1. Load the dataset
print("Loading Capital Attack Dataset for Phase 1...")
df = pd.read_csv("capital_attack_dataset.csv")

# 2. Data Cleaning
df['car_type'] = pd.factorize(df['car_type'])[0]

# 3. Select Features and Target for Phase 1
# WE DROPPED 'data_corrupted' HERE TO PREVENT 100% LEAKAGE AND FORCE REALISTIC ERRORS
X = df[['car_type', 'speed', 'r_incoming', 'position_error']]

# Phase 1 Target: Binary (0: Normal, 1: Under Attack)
y = df['attack_class'].apply(lambda x: 1 if x > 0 else 0)

# 4. Split data (80% train - 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Inject dynamic testing noise to simulate NAC real-world network drops ---
X_test = X_test.copy()
X_test['r_incoming'] += np.random.randint(-4, 5, size=len(X_test))
X_test['position_error'] += np.random.uniform(-0.1, 0.1, size=len(X_test))

# 5. Train Phase 1 Classifier with strict regularization (max_depth=4)
print("Training Phase 1 Security Perimeter Engine...")
clf_p1 = ExtraTreesClassifier(n_estimators=100, max_depth=4, min_samples_leaf=15, random_state=42)
clf_p1.fit(X_train, y_train)

# 6. Evaluate Phase 1 Results
y_pred = clf_p1.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nSuccess! Phase 1 Triage Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Phase 1 Classification Report:\n", classification_report(y_test, y_pred, target_names=['Normal', 'Under Attack']))

print("\nPhase 1 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 7. Save Phase 1 Model
joblib.dump(clf_p1, 'vanet_phase1_detector.pkl')
print("Model saved as vanet_phase1_detector.pkl")
