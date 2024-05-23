# Changes 

All notable changes to TripTrek will be documented in this file.

## [1.0.1] - 2024-05-22

### Added
- Data visualization option enabled on `data_visualization.py` for users to analyze travel expense patterns. The plots added include:
    - Breakdown of expenses by category. 
    - Timeline of activities.
    - Daily spending by category. 
    - Daily over / under budget. 
    - Budget vs actual spending 
    - _Note:_ Some graphs still need adjustments in the previous steps to be optimal e.g. expenses need to be summarized by day/category for the graph to be correctly displayed. 
- Exceptions to ensure that users can only input cities that are available in the data/restaurants.csv file, and to validate expense categories. 
- Unit tests (described in testing.md)
- Case-insensitive input handling to improve user experience.
- Added a column to the budget DataFrame to calculate and display the budget per day, and sum it by category.


### Changed
- Modified plan_trip method to normalize user input for city names. 
- Updated get_attractions_for_city, get_restaurants_for_city, and get_country methods to perform case-insensitive matching for city names.
- Modified create_budget method to include 'Budget' and 'Trip Day' columns in the budget DataFrame.
    - In the `create_budget` method, the logic was added to create a `Trip Day` column based on the unique trip days from `itinerary.csv`. This includes creating a DataFrame for each day with the budget per day for activities, food, and transportation.
    - If the itinerary does not exist, the user is asked to manually input the budget for activities, food, and transportation. The budget per day is then calculated and added to the `budget_days` list.
- Refactoring, removed unnecessary or redundant code, fixed inconsistencies, and improved code organization for budget_manager and trip_planner.

## [1.0.0] - 2024-05-16
### Added
- Initial prototype of TripPlanner with trip planning functionality, Basic Budget Generator and Expenses Tracker. Current version features:
    - Generate a suggested itinerary in .csv for the duration of your trip including attractions, restaurants, and optionally activities added manually by the user, along with costs estimates.
    - Generate a budget csv file organized by category including both data from the suggested itinerary or entered manually by user.
    - Generate an expenses csv file listing the category and expense.
