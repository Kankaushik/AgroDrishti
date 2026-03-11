import os
from joblib import load

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "yield_model.pkl")
ENCODERS_PATH = os.path.join(BASE_DIR, "yield_encoders.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "yield_features.pkl")

model = load(MODEL_PATH)
encoders = load(ENCODERS_PATH)
feature_cols = load(FEATURES_PATH)

# Numeric and categorical feature names
NUMERIC_FEATURES = [
    "soil_moisture_%", "soil_pH", "temperature_C", "rainfall_mm",
    "humidity_%", "sunlight_hours", "pesticide_usage_ml", "total_days", "NDVI_index"
]
CATEGORICAL_FEATURES = [
    "region", "crop_type", "irrigation_type", "fertilizer_type", "crop_disease_status"
]


def predict_yield(data: dict) -> float:
    """
    Predict crop yield (kg/hectare) from input data.
    
    Expected keys in data:
    - soil_moisture, soil_ph, temperature, rainfall, humidity, sunlight_hours
    - pesticide_usage, total_days, ndvi
    - region, crop_type, irrigation_type, fertilizer_type, crop_disease_status
    """
    # Map input keys to feature names
    features = []
    
    # Numeric features (with flexible key mapping)
    key_map = {
        "soil_moisture_%": ["soil_moisture_%", "soil_moisture"],
        "soil_pH": ["soil_pH", "soil_ph", "ph"],
        "temperature_C": ["temperature_C", "temperature"],
        "rainfall_mm": ["rainfall_mm", "rainfall"],
        "humidity_%": ["humidity_%", "humidity"],
        "sunlight_hours": ["sunlight_hours", "sunlight"],
        "pesticide_usage_ml": ["pesticide_usage_ml", "pesticide_usage", "pesticide"],
        "total_days": ["total_days", "days"],
        "NDVI_index": ["NDVI_index", "ndvi", "NDVI"]
    }
    
    for feat in NUMERIC_FEATURES:
        val = None
        for key in key_map.get(feat, [feat]):
            if key in data:
                val = float(data[key])
                break
        features.append(val if val is not None else 0.0)
    
    # Categorical features (encode using saved encoders)
    for cat in CATEGORICAL_FEATURES:
        val = data.get(cat, "")
        if val in encoders[cat].classes_:
            encoded = encoders[cat].transform([val])[0]
        else:
            # Use first class as fallback
            encoded = 0
        features.append(encoded)
    
    prediction = model.predict([features])[0]
    return round(prediction, 2)


def get_crop_types():
    """Return list of available crop types from encoder"""
    return list(encoders["crop_type"].classes_)


def get_regions():
    """Return list of available regions from encoder"""
    return list(encoders["region"].classes_)


def get_irrigation_types():
    """Return list of available irrigation types"""
    return list(encoders["irrigation_type"].classes_)


def get_fertilizer_types():
    """Return list of available fertilizer types"""
    return list(encoders["fertilizer_type"].classes_)


def get_disease_statuses():
    """Return list of available disease statuses"""
    return list(encoders["crop_disease_status"].classes_)

