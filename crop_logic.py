def estimate_yield_category(yield_kg_per_hectare: float) -> dict:
    """
    Categorize yield into Low/Medium/High and provide recommendations.
    Based on general crop yield benchmarks.
    """
    if yield_kg_per_hectare < 2500:
        category = "Low"
        color = "red"
        recommendation = "Consider improving soil nutrients, irrigation, or pest control."
    elif yield_kg_per_hectare < 4500:
        category = "Medium"
        color = "amber"
        recommendation = "Good yield. Minor optimizations could improve results."
    else:
        category = "High"
        color = "green"
        recommendation = "Excellent yield! Current practices are optimal."
    
    return {
        "category": category,
        "color": color,
        "recommendation": recommendation,
        "yield_kg_per_hectare": yield_kg_per_hectare
    }


def get_crop_emoji(crop_type: str) -> str:
    """Return emoji for crop type"""
    emoji_map = {
        "Rice": "🌾",
        "Wheat": "🌾",
        "Maize": "🌽",
        "Cotton": "🏵️",
        "Soybean": "🫘"
    }
    return emoji_map.get(crop_type, "🌱")


def recommend_improvements(data: dict, predicted_yield: float) -> list:
    """
    Suggest improvements based on input parameters.
    """
    suggestions = []
    
    soil_moisture = data.get("soil_moisture", data.get("soil_moisture_%", 0))
    if soil_moisture < 25:
        suggestions.append("Increase soil moisture through better irrigation")
    elif soil_moisture > 45:
        suggestions.append("Reduce irrigation to avoid waterlogging")
    
    soil_ph = data.get("soil_ph", data.get("soil_pH", 7))
    if soil_ph < 5.5:
        suggestions.append("Apply lime to raise soil pH")
    elif soil_ph > 7.5:
        suggestions.append("Apply sulfur to lower soil pH")
    
    ndvi = data.get("ndvi", data.get("NDVI_index", 0.5))
    if ndvi < 0.4:
        suggestions.append("Low vegetation health - check for diseases/pests")
    
    disease = data.get("crop_disease_status", "Mild")
    if disease == "Severe":
        suggestions.append("Apply targeted pesticides for disease control")
    elif disease == "Moderate":
        suggestions.append("Monitor and consider preventive treatment")
    
    if not suggestions:
        suggestions.append("Current conditions are optimal - maintain practices")
    
    return suggestions
