from sklearn.ensemble import IsolationForest
import joblib
import pandas as pd
import os

MODEL_PATH = "model.joblib"

def train_model():
    df = pd.read_csv("historical_logs.csv")  # Train on past logs
    model = IsolationForest(contamination=0.01)
    model.fit(df[["timestamp", "status_code"]])
    joblib.dump(model, MODEL_PATH)  # Save model
    return model

def load_model():
    return joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else train_model()

model = load_model()  # Load model at startup

def detect_anomalies(df):
    df["anomaly"] = model.predict(df[["timestamp", "status_code"]])
    return df[df["anomaly"] == -1]
