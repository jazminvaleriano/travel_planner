import pandas as pd

# Example data retrieved from TripAdvisor API for Paris
# Mock data for attractions in Paris
attractions_data = [
    {
        "name": "Eiffel Tower",
        "city": "Paris",
        "rating": 4.5,
        "num_reviews": 10000,
        "location": {"latitude": 48.8584, "longitude": 2.2945},
        "price_range": "$$ - $$$"
    },
    {
        "name": "Louvre Museum",
        "city": "Paris",
        "rating": 4.8,
        "num_reviews": 19000,
        "location": {"latitude": 48.8606, "longitude": 2.3376},
        "price_range": "$$"
    },
    {
        "name": "Notre-Dame Cathedral",
        "city": "Paris",
        "rating": 4.7,
        "num_reviews": 15000,
        "location": {"latitude": 48.8530, "longitude": 2.3498},
        "price_range": "$"
    },
    {
        "name": "Montmartre",
        "city": "Paris",
        "rating": 4.6,
        "num_reviews": 12000,
        "location": {"latitude": 48.8867, "longitude": 2.3431},
        "price_range": "$"
    },
    {
        "name": "Seine River Cruise",
        "city": "Paris",
        "rating": 4.8,
        "num_reviews": 17000,
        "location": {"latitude": 48.8584, "longitude": 2.3526},
        "price_range": "$$"
    },
    {
        "name": "Musée d'Orsay",
        "city": "Paris",
        "rating": 4.7,
        "num_reviews": 14000,
        "location": {"latitude": 48.8606, "longitude": 2.3264},
        "price_range": "$$"
    },
    {
        "name": "Sainte-Chapelle",
        "city": "Paris",
        "rating": 4.7,
        "num_reviews": 16000,
        "location": {"latitude": 48.8556, "longitude": 2.3458},
        "price_range": "$"
    },
    {
        "name": "Palace of Versailles",
        "city": "Paris",
        "rating": 4.6,
        "num_reviews": 13000,
        "location": {"latitude": 48.8049, "longitude": 2.1204},
        "price_range": "$$ - $$$"
    },
    {
        "name": "Centre Pompidou",
        "city": "Paris",
        "rating": 4.5,
        "num_reviews": 11000,
        "location": {"latitude": 48.8606, "longitude": 2.3522},
        "price_range": "$$"
    },
    {
        "name": "Luxembourg Gardens",
        "city": "Paris",
        "rating": 4.7,
        "num_reviews": 18000,
        "location": {"latitude": 48.8462, "longitude": 2.3372},
        "price_range": "$"
    }
]

# Create DataFrame
attractions_df = pd.DataFrame(attractions_data)

# Save DataFrame to CSV
attractions_df.to_csv("data/attractions.csv", index=False)