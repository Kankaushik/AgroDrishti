from .iot_dummy import get_dummy_iot_data
from .crop_logic import recommend_crop_from_iot
from .ml_predictor import predict_crop
from .soil_analyzer import analyze_soil

from sqlalchemy.orm import Session
from .db import engine
from .models import CropPrediction

def init_agrodrishti(app):

    @app.get("/api/agrodrishti/recommend")
    def agrodrishti_recommend():

        iot_data = {
            "temperature": 28,
            "humidity": 70,
            "ph": 6.5,
            "rainfall": 120,
            "soil_moisture": 60,
            "soil_ph": 6.8
        }

        crop = predict_crop(iot_data)

        soil_analysis = analyze_soil({
            "soil_moisture": iot_data["soil_moisture"],
            "soil_ph": iot_data["soil_ph"]
        })

        return {
            "iot_mode": "dummy",
            "ml_model": "Random Forest",
            "recommended_crop": crop,
            "sensor_data": iot_data,
            "soil_analysis": soil_analysis
        }
