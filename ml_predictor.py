import os
from joblib import load

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "crop_model.pkl")

model = load(MODEL_PATH)

def predict_crop(iot_data):
    features = [[
        iot_data["temperature"],
        iot_data["humidity"],
        iot_data["ph"],
        iot_data["rainfall"]
        
    ]]
    return model.predict(features)[0]

