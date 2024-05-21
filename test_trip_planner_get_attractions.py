import unittest
import pandas as pd
from trip_planner import TripPlanner  

class TestGetAttractionsForCity(unittest.TestCase):
    def setUp(self):
        # Set up a TripPlanner object for testing
        self.planner = TripPlanner()

    def test_get_attractions_for_city(self):
        # Define mock attractions data for Paris
        mock_attractions_data = {
            "city": ["Paris", "Paris", "Paris"],
            "name": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
            "price_range": ["$", "$$", "$$"],
            "rating": [4.8, 4.7, 4.6],
            "num_reviews": [10000, 9500, 9000]
        }

        # Set the mock attractions data for the planner's attractions_data attribute
        self.planner.attractions_data = pd.DataFrame(mock_attractions_data)

        # Call the get_attractions_for_city method for Paris
        attractions_for_paris = self.planner.get_attractions_for_city("Paris")

        # Assert that the returned DataFrame has the correct number of rows
        self.assertEqual(len(attractions_for_paris), 3)

        # Assert that the returned DataFrame contains the correct columns
        self.assertListEqual(list(attractions_for_paris.columns), ["city", "name", "price_range", "rating", "num_reviews"])

        # Assert that the returned DataFrame contains data only for Paris
        self.assertTrue((attractions_for_paris["city"] == "Paris").all())

if __name__ == '__main__':
    unittest.main()
