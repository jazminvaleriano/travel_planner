# Changes 

All notable changes to TripTrek will be documented in this file.

## [1.0.2] - 2024-05-22
### Added
- Data visualizer for users to analyze their travel patterns and budget usage to optimize future trips.

### Changed 
- Modified main.py to import data visualizer.


## [1.0.1] - 2024-05-21
### Added
- Case-insensitive city input handling to improve user experience.
- Added a column to the budget DataFrame to calculate and display the budget per day.
- Included Trip Day in the budget and expenses DataFrames, using data from itinerary.csv.


### Changed
- Modified plan_trip method to normalize user input for city names.
- Updated get_attractions_for_city and get_restaurants_for_city methods to perform case-insensitive matching for city names.
- Adjusted the retrieval of the destination country to be case-insensitive.
- Modified create_budget method to include 'Budget Per Day' and 'Trip Day' columns in the budget DataFrame.
    - In the `create_budget` method, the logic was added to create a `Trip Day` column based on the unique trip days from `itinerary.csv`. This includes creating a DataFrame for each day with the budget per day for activities, food, and transportation.
    - If the itinerary does not exist, the user is asked to manually input the budget for activities, food, and transportation. The budget per day is then calculated and added to the `budget_days` list.
- Updated track_expense method to include 'Trip Day' for each expense tracked.



## [1.0.0] - 2024-05-16
### Added
- Initial prototype of TripPlanner with trip planning functionality, Basic Budget Generator and Expenses Tracker. Current version features:
    - Generate a suggested itinerary in .csv for the duration of your trip including attractions, restaurants, and optionally activities added manually by the user, along with costs estimates.
    - Generate a budget csv file organized by category including both data from the suggested itinerary or entered manually by user.
    - Generate an expenses csv file listing the category and expense.
