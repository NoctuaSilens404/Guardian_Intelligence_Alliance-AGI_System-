import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "datos_fatiga.csv")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "modelos")
MODEL_PATH = os.path.join(MODEL_DIR, "modelo_riesgo_fatiga.pkl")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")

FEATURES = ["pulso", "temperatura", "spo2", "horas_trabajadas"]

def entrenar():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna()

    X = df[FEATURES]
    y = df["etiqueta_riesgo"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_scaled, y)

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(f"Modelo guardado en {MODEL_PATH}")

if __name__ == "__main__":
    entrenar()
