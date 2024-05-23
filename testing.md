# Function Description

The `get_attractions_for_city` function collects city-specific attractions data from the `TripPlanner` class's `attractions_data` DataFrame. It filters the DataFrame based on the specified city name and returns attractions unique to that city.

## Possible Unexpected Results

1. **Incorrect City Name**: If the given city name does not exist in the attractions data, the function could return an empty DataFrame or raise an error. This can occur if there is an error in the city name or if the city is not included in the dataset.

2. **Case Sensitivity**: If the city name is provided with a different case (e.g., "paris" instead of "Paris"), the function might fail to match the city name and return an empty DataFrame if case sensitivity is not handled correctly.

3. **Empty Dataset**: If the attractions data for the chosen city is missing or incomplete, the function could return an empty DataFrame. This can happen if the dataset is not loaded properly or if the attractions data has missing values.

## Testing Approaches

To check that the `get_attractions_for_city` function performs as expected, we can test several scenarios:

1. **Valid City Name**: Run the function using a city name that appears in the attractions database. Check that the returned DataFrame has the expected attractions for that city.

2. **Invalid City Name**: Test the function with a city name that does not appear in the attractions database. Ensure that the function handles this situation carefully, such as by returning an empty DataFrame.

3. **Empty Dataset**: Run the function while the attractions data is set to an empty DataFrame. Verify that the function returns an empty DataFrame.

4. **Case Insensitivity**: Test the function by providing a city name with different case variations. Check that the function still returns the correct results regardless of the case used.
