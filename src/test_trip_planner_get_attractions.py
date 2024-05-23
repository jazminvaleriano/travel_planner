import unittest
import pandas as pd
from trip_planner import TripPlanner

class TestGetAttractionsForCity(unittest.TestCase):
    def setUp(self):
        # Set up a TripPlanner object for testing
        self.planner = TripPlanner()

    def test_get_attractions_for_city_standard(self):
        # Test standard case for getting attractions in Paris
        mock_attractions_data = {
            "city": ["Paris", "Paris", "Paris"],
            "name": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
            "price_range": ["$", "$$", "$$"],
            "rating": [4.8, 4.7, 4.6],
            "num_reviews": [10000, 9500, 9000]
        }
        self.planner.attractions_data = pd.DataFrame(mock_attractions_data)

        # Call the get_attractions_for_city method for Paris
        attractions_for_paris = self.planner.get_attractions_for_city("Paris")

        # Assert that the returned DataFrame has the correct number of rows
        self.assertEqual(len(attractions_for_paris), 3)

        # Assert that the returned DataFrame contains the correct columns
        self.assertListEqual(list(attractions_for_paris.columns), ["city", "name", "price_range", "rating", "num_reviews"])

        # Assert that the returned DataFrame contains data only for Paris
        self.assertTrue((attractions_for_paris["city"] == "Paris").all())

    def test_get_attractions_for_city_not_found(self):
        # Test case when the city is not found in the dataset
        mock_attractions_data = {
            "city": ["Paris", "Paris", "Paris"],
            "name": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
            "price_range": ["$", "$$", "$$"],
            "rating": [4.8, 4.7, 4.6],
            "num_reviews": [10000, 9500, 9000]
        }
        self.planner.attractions_data = pd.DataFrame(mock_attractions_data)

        # Call the get_attractions_for_city method for a city not in the dataset
        attractions_for_berlin = self.planner.get_attractions_for_city("Berlin")

        # Assert that the returned DataFrame is empty
        self.assertTrue(attractions_for_berlin.empty)

    def test_get_attractions_for_city_empty_dataset(self):
        # Test case when the dataset is empty
        self.planner.attractions_data = pd.DataFrame(columns=["city", "name", "price_range", "rating", "num_reviews"])

        # Call the get_attractions_for_city method
        attractions = self.planner.get_attractions_for_city("Paris")

        # Assert that the returned DataFrame is empty
        self.assertTrue(attractions.empty)

    def test_get_attractions_for_city_case_insensitive(self):
        # Test case insensitivity for city names
        mock_attractions_data = {
            "city": ["Paris", "Paris", "Paris"],
            "name": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
            "price_range": ["$", "$$", "$$"],
            "rating": [4.8, 4.7, 4.6],
            "num_reviews": [10000, 9500, 9000]
        }
        self.planner.attractions_data = pd.DataFrame(mock_attractions_data)

        # Call the get_attractions_for_city method with a different case for the city name
        attractions_for_paris_lower = self.planner.get_attractions_for_city("paris")

        # Assert that the returned DataFrame is not empty
        self.assertFalse(attractions_for_paris_lower.empty)

if __name__ == '__main__':
    unittest.main()
