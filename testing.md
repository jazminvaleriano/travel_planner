# Function Description

The `get_attractions_for_city` function collects city-specific attractions data from the `TripPlanner` class's `attractions_data` DataFrame. It filters the DataFrame based on the specified city name and returns attractions unique to that city.

## Possible Unexpected Results

1. **Incorrect City Name**: If the given city name does not exist in the attractions data, the function could return an empty DataFrame or raise an error. This can occur if there is an error in the city name or if the city is not included in the dataset.

2. **Missing Data**: If the attractions data for the chosen city is missing or incomplete, the function could return an incomplete or incorrect result. This can happen if the dataset is not loaded properly or if the attractions data has missing values.

## Testing Approaches

To check that the `get_attractions_for_city` function performs as expected, we can test several scenarios:

1. **Valid City Name**: Run the function using a city name that appears in the attractions database. Check that the given DataFrame has the expected attractions for that city.

2. **Invalid City Name**: Testing the function with a city name that does not appear in the attractions database. Ensure that the function handles this situation carefully, such as by returning an empty DataFrame or reporting an appropriate error.

3. **Missing Data**: Run the function while the attractions data for the provided city is missing or partial. This can be accomplished by setting the `TripPlanner` object's `attractions_data` attribute to an empty DataFrame or one with missing values prior to running the function.
