# TripTrek

Welcome to the TripTrek project! This repository contains a prototype tool designed to simplify travel planning by generating itineraries, creating a budget and tracking expenses for your next adventure. 

## ⚠️ Important Updates and Instructions (As of May 16th)
Please note that for the moment we're unable to access real-time data from traveling websites for attractions and restaurants worldwide. Consequently, our datasets are currently limited. When testing the tool, please consider the following:
- At this time, TripTrek fully supports Paris, London, and New York only.
- We recommend keeping your trip length under 4 days. We're actively working on a solution to provide better recommendations for longer trips.

If the instructions and recommendations are followed, TripTrek is able to:
- Generate a suggested itinerary in .csv for the duration of your trip including attractions, restaurants, and optionally activities added manually by the user, along with costs estimates.
- Generate a budget csv file organized by category including both data from the suggested itinerary or entered manually by user.
- Generate an expenses csv file listing the category and expense.

## Goal Features
* **Customizable Itineraries**: Users can specify their destination city, travel preferences and schedule. TripTrek Itinerary Generator will organize your activities efficiently, and estimate your trip costs, maximizing your time and enjoyment.
* **Budget Management**: You can use TripTrek to keep track of your trip expenses (such as accommodation costs, transportation, meals, and activities), and stay within budget. 
* **Data visualization and Trip Analysis**: Provide users with visualizations of their trip data, such as a timeline of planned activities or a breakdown of expenses by category. Allow users to analyze their travel patterns and budget usage to optimize future trips.  

_Features to be added only if time allows:_

* **Generate Daily Routes and Estimated Budget**: Say goodbye to the hassle of planning routes between attractions. Our tool automatically generates daily routes, based on distance starting from your initial location (such as your hotel), ensuring a smooth and enjoyable travel experience.
* **Retrieve Top-Rated Touristic Sites**: TripTrek will fetch the top-rated tourist attractions in your selected area, and prioritize them according to the duration of your trip. This ensures that your itinerary includes must-see landmarks and experiences.

## Getting Started


### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. Make sure you have Python Installed
3. Download and install required libs and data:
    ```bash
    pip install requirements.txt
    ```
2. Navigate to the project directory:
   ```bash
   cd travel_planner
   ```

## Usage

To run the interface, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory if you haven't already.
3. Run the following command:
   ```bash
   python src/main.py
   ```
4. Follow the instructions on the terminal

## Contributors

* Merlyne Lawrence [@MerNLP](https://github.com/MerNLP)
* Kamdoum Kemfio Hans [@MerNLP](https://github.com/MerNLP)
* Assadeck Moussa Aitock [@kmaritinion](https://github.com/kmartinion)
* Jazmin Valeriano [@jazminvaleriano](https://github.com/jazminvaleriano)

## Roadmap

If you want to be part of the project as contributor and find out more about the current status, check out ROADMAP.md

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
