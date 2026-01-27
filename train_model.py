import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Features and label
X = df[["temperature", "humidity", "ph", "rainfall"]]
y = df["label"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
dump(model, "crop_model.pkl")

print("Model trained using dataset and saved as crop_model.pkl")
