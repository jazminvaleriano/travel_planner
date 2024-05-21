# Changes 

All notable changes to TripTrek will be documented in this file.


## [1.0.1] - 2024-05-21
### Added
- Case-insensitive city input handling to improve user experience.

### Changed
- Modified plan_trip method to normalize user input for city names.
- Updated get_attractions_for_city and get_restaurants_for_city methods to perform case-insensitive matching for city names.
- Adjusted the retrieval of the destination country to be case-insensitive.

## [1.0.0] - 2024-05-16
### Added
- Initial prototype of TripPlanner with trip planning functionality, Basic Budget Generator and Expenses Tracker. Current version features:
    - Generate a suggested itinerary in .csv for the duration of your trip including attractions, restaurants, and optionally activities added manually by the user, along with costs estimates.
    - Generate a budget csv file organized by category including both data from the suggested itinerary or entered manually by user.
    - Generate an expenses csv file listing the category and expense.