from flask import request, jsonify
from ml_predictor import (
    predict_yield, get_crop_types, get_regions, 
    get_irrigation_types, get_fertilizer_types, get_disease_statuses
)
from crop_logic import estimate_yield_category, get_crop_emoji, recommend_improvements
from soil_analyzer import analyze_soil

from sqlalchemy.orm import Session
from db import engine
from models import CropPrediction

def init_agrodrishti(app):

    @app.get("/api/agrodrishti/options")
    def agrodrishti_options():
        """Return available options for dropdowns"""
        return jsonify({
            "crop_types": get_crop_types(),
            "regions": get_regions(),
            "irrigation_types": get_irrigation_types(),
            "fertilizer_types": get_fertilizer_types(),
            "disease_statuses": get_disease_statuses()
        })

    @app.post("/api/agrodrishti/predict")
    def agrodrishti_predict():
        """
        Predict crop yield based on input parameters.
        
        Expected JSON body:
        {
            "crop_type": "Rice",
            "region": "North India",
            "soil_moisture": 35.5,
            "soil_ph": 6.5,
            "temperature": 28,
            "rainfall": 120,
            "humidity": 70,
            "sunlight_hours": 7,
            "irrigation_type": "Drip",
            "fertilizer_type": "Organic",
            "pesticide_usage": 10,
            "total_days": 120,
            "ndvi": 0.65,
            "crop_disease_status": "Mild"
        }
        """
        data = request.get_json(silent=True) or {}
        
        # Map incoming keys to expected format
        input_data = {
            "crop_type": data.get("crop_type", "Rice"),
            "region": data.get("region", "North India"),
            "soil_moisture_%": data.get("soil_moisture", data.get("soil_moisture_%", 30)),
            "soil_pH": data.get("soil_ph", data.get("soil_pH", 6.5)),
            "temperature_C": data.get("temperature", data.get("temperature_C", 28)),
            "rainfall_mm": data.get("rainfall", data.get("rainfall_mm", 100)),
            "humidity_%": data.get("humidity", data.get("humidity_%", 65)),
            "sunlight_hours": data.get("sunlight_hours", data.get("sunlight", 7)),
            "irrigation_type": data.get("irrigation_type", "Drip"),
            "fertilizer_type": data.get("fertilizer_type", "Organic"),
            "pesticide_usage_ml": data.get("pesticide_usage", data.get("pesticide_usage_ml", 10)),
            "total_days": data.get("total_days", data.get("days", 120)),
            "NDVI_index": data.get("ndvi", data.get("NDVI_index", 0.6)),
            "crop_disease_status": data.get("crop_disease_status", "Mild")
        }
        
        # Make prediction
        predicted_yield = predict_yield(input_data)
        yield_info = estimate_yield_category(predicted_yield)
        improvements = recommend_improvements(input_data, predicted_yield)
        crop_emoji = get_crop_emoji(input_data["crop_type"])
        
        # Soil analysis
        soil_analysis = analyze_soil({
            "soil_moisture": input_data["soil_moisture_%"],
            "soil_ph": input_data["soil_pH"]
        })
        
        return jsonify({
            "success": True,
            "prediction": {
                "yield_kg_per_hectare": predicted_yield,
                "yield_category": yield_info["category"],
                "yield_color": yield_info["color"],
                "crop_type": input_data["crop_type"],
                "crop_emoji": crop_emoji,
                "recommendation": yield_info["recommendation"]
            },
            "improvements": improvements,
            "soil_analysis": soil_analysis,
            "input_data": input_data,
            "model": "Random Forest Regressor"
        })

    @app.get("/api/agrodrishti/recommend")
    def agrodrishti_recommend():
        """Legacy endpoint - returns sample prediction with default values"""
        
        default_data = {
            "crop_type": "Rice",
            "region": "North India",
            "soil_moisture_%": 35,
            "soil_pH": 6.5,
            "temperature_C": 28,
            "rainfall_mm": 120,
            "humidity_%": 70,
            "sunlight_hours": 7,
            "irrigation_type": "Drip",
            "fertilizer_type": "Organic",
            "pesticide_usage_ml": 10,
            "total_days": 120,
            "NDVI_index": 0.65,
            "crop_disease_status": "Mild"
        }
        
        predicted_yield = predict_yield(default_data)
        yield_info = estimate_yield_category(predicted_yield)
        
        soil_analysis = analyze_soil({
            "soil_moisture": default_data["soil_moisture_%"],
            "soil_ph": default_data["soil_pH"]
        })

        return jsonify({
            "iot_mode": "smart_farming",
            "ml_model": "Random Forest Regressor",
            "predicted_yield": predicted_yield,
            "yield_category": yield_info["category"],
            "crop_type": default_data["crop_type"],
            "sensor_data": default_data,
            "soil_analysis": soil_analysis
        })
