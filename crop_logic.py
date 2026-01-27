def recommend_crop_from_iot(iot_data):
    soil_moisture = iot_data.get("soil_moisture", 0)
    temperature = iot_data.get("temperature", 0)
    ph = iot_data.get("ph", 7)

    # Simple rule-based logic
    if soil_moisture > 55 and 6 <= ph <= 7 and temperature >= 25:
        return "Rice"
    elif soil_moisture <= 55 and temperature < 25:
        return "Wheat"
    else:
        return "Maize"
