import random

crop_data = {
    "drought-resistant": ["Sorghum", "Millet", "Cowpeas"],
    "flood-tolerant": ["Rice", "Sugarcane", "Taro"],
    "heat-resistant": ["Cassava", "Okra", "Amaranth"]
}

def recommend_crop(climate_condition):
    return random.choice(crop_data.get(climate_condition, []))
