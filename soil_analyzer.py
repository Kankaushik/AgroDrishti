def analyze_soil(soil_data):
    moisture = soil_data.get("soil_moisture")
    ph = soil_data.get("soil_ph")

    # Moisture analysis
    if moisture < 30:
        moisture_status = "Low"
        moisture_advice = "Irrigation required"
    elif 30 <= moisture <= 60:
        moisture_status = "Optimal"
        moisture_advice = "Soil moisture is adequate"
    else:
        moisture_status = "High"
        moisture_advice = "Drainage recommended"

    # pH analysis
    if ph < 5.5:
        ph_status = "Acidic"
        ph_advice = "Consider liming to raise soil pH"
    elif 5.5 <= ph <= 7.5:
        ph_status = "Neutral"
        ph_advice = "Soil pH is ideal for most crops"
    else:
        ph_status = "Alkaline"
        ph_advice = "Consider gypsum or organic matter"

    return {
        "soil_moisture_status": moisture_status,
        "soil_moisture_advice": moisture_advice,
        "soil_ph_status": ph_status,
        "soil_ph_advice": ph_advice
    }
