import pandas as pd

# Mock data for restaurants in Paris
restaurants_data = [
    {
        "name": "Le Bernardin",
        "city": "Paris",
        "rating": 4.8,
        "num_reviews": 5000,
        "location": {"latitude": 48.8663, "longitude": 2.3232},
        "price_range": "$$$"
    },
    {
        "name": "L'Astrance",
        "city": "Paris",
        "rating": 4.9,
        "num_reviews": 6000,
        "location": {"latitude": 48.8555, "longitude": 2.3156},
        "price_range": "$$$$"
    },
    {
        "name": "Le Jules Verne",
        "city": "Paris",
        "rating": 4.7,
        "num_reviews": 4500,
        "location": {"latitude": 48.8583, "longitude": 2.2939},
        "price_range": "$$$"
    },
    {
        "name": "Guy Savoy",
        "city": "Paris",
        "rating": 4.8,
        "num_reviews": 5500,
        "location": {"latitude": 48.8639, "longitude": 2.3471},
        "price_range": "$"
    },
    {
        "name": "Alain Ducasse at Plaza Athénée",
        "city": "Paris",
        "rating": 4.9,
        "num_reviews": 6500,
        "location": {"latitude": 48.8671, "longitude": 2.3037},
        "price_range": "$$$$"
    },
    {
        "name": "Arpège",
        "city": "Paris",
        "rating": 4.7,
        "num_reviews": 4800,
        "location": {"latitude": 48.8569, "longitude": 2.3156},
        "price_range": "$$$$"
    },
    {
        "name": "Pierre Gagnaire",
        "city": "Paris",
        "rating": 4.8,
        "num_reviews": 5200,
        "location": {"latitude": 48.8693, "longitude": 2.3085},
        "price_range": "$"
    },
    {
        "name": "Septime",
        "city": "Paris",
        "rating": 4.6,
        "num_reviews": 4200,
        "location": {"latitude": 48.8523, "longitude": 2.3783},
        "price_range": "$$"
    },
    {
        "name": "Le Cinq",
        "city": "Paris",
        "rating": 4.7,
        "num_reviews": 4900,
        "location": {"latitude": 48.8708, "longitude": 2.3036},
        "price_range": "$$$"
    },
    {
        "name": "L'Arpège",
        "city": "Paris",
        "rating": 4.7,
        "num_reviews": 4600,
        "location": {"latitude": 48.8563, "longitude": 2.3083},
        "price_range": "$$$"
    }
]

# Create DataFrame
restaurants_df = pd.DataFrame(restaurants_data)

# Save DataFrame to CSV
restaurants_df.to_csv("data/restaurants.csv", index=False)
