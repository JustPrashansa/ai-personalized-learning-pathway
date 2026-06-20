import joblib
from utils.persona_mapping import persona_types
kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")
def predict_persona(student_features):
    scaled = scaler.transform([student_features])
    cluster = kmeans.predict(scaled)[0]
    return persona_types[cluster]