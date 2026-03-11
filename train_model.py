import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from joblib import dump

# Load cleaned dataset
df = pd.read_csv("Smart_Farming_Crop_Yield_2024.csv")

# Define features
NUMERIC_FEATURES = [
    "soil_moisture_%", "soil_pH", "temperature_C", "rainfall_mm",
    "humidity_%", "sunlight_hours", "pesticide_usage_ml", "total_days", "NDVI_index"
]
CATEGORICAL_FEATURES = [
    "region", "crop_type", "irrigation_type", "fertilizer_type", "crop_disease_status"
]

# Encode categorical features
encoders = {}
for col in CATEGORICAL_FEATURES:
    le = LabelEncoder()
    df[col + "_encoded"] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# Build feature matrix
feature_cols = NUMERIC_FEATURES + [c + "_encoded" for c in CATEGORICAL_FEATURES]
X = df[feature_cols]
y = df["yield_kg_per_hectare"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train regression model
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Model Performance: MAE={mae:.2f} kg/ha, R2={r2:.4f}")

# Save model and encoders
dump(model, "yield_model.pkl")
dump(encoders, "yield_encoders.pkl")
dump(feature_cols, "yield_features.pkl")

print("Yield prediction model saved as yield_model.pkl")
print("Encoders saved as yield_encoders.pkl")
print("Feature list saved as yield_features.pkl")
