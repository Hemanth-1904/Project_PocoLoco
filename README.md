# Project_PocoLoco
This project demonstrates how autonomous AI agents can collaborate and execute complex tasks efficiently.


## Project Structure
The project consists of the following files and directories:

`agents.py :`  Defines Crew AI agents responsible for specific tasks in the travel itinerary planning process, such as gathering user preferences, searching for relevant destinations and activities, and curating the final itinerary.

`tasks.py :`  Defines Crew AI tasks for each agent involved in the travel itinerary planning process, such as collecting user input, fetching travel data from various sources, and generating the itinerary.

`search_tools.py :`  Provides custom search tools using APIs (e.g., SERPER) to gather relevant information for travel planning, such as destinations, attractions, accommodations, and transportation options.

`file_io.py :`  Contains functions for saving the generated travel itinerary in markdown format.

`main.py :`  The main script that instantiates Crew AI agents, tasks, and the language model (e.g., LLaMA 3.1 (70b)). It then forms a Crew object and kicks off the travel itinerary planning process.

`app.py :` Defines and creates the Streamlit application, providing a user-friendly interface for users to input their travel preferences and receive personalized itineraries.

`.env (hidden file) :`  Stores API keys (e.g., SERPER API key, Groq API KEY) used by the project.

`requirements.txt :`  Stores all the python libraries. 

## How it Works

1. **Destination Research:** The `Destination_Research_Agent` analyzes and recommends the most suitable destination for the user's trip, considering factors like famous places, local cuisine, cultural experiences, weather, events, costs, and alignment with their interests.

2. **Accommodation Curation:** The `Accommodation_Agent` provides a curated list of accommodation options with detailed information and current pricing.

3. **Transportation Planning:** The `Transportation_Agent` provides a detailed transportation plan, including modes of travel, schedules, and pricing.

4. **Weather Analysis:** The `Weather_Agent` provides detailed weather information for the trip dates, including forecasts and advisories.

5. **Itinerary Planning:** The `Itinerary_Planner_Agent` creates a detailed daily itinerary that balances must-see attractions with unique local experiences, ensuring a well-rounded and enjoyable trip based on the user's preferences, interests, and the outputs from other agents.

6. **Budget Analysis:** The `Budget_Analyst_Agent` provides a comprehensive budget breakdown for the trip, ensuring transparency and helping the user make informed decisions.

## Running the Project
1. **Fork or Clone the Repository::** 

Fork or clone this repository to your local machine using Git.

2. **Install Requirements:**

Install the necessary libraries.

```bash
pip install -r requirements.txt

```

3. **Set Up Environment Variables:**

Create a `.env` file in your project directory and add any required API keys (e.g., SERPER API key, Groq API KEY).

4. **Run the main file:**

```bash
python main.py
```
4. **Run the streamlit application file:**

```bash
streamlit run app.py
```
This will initiate the Crew AI workflow and generate a perfect trip plan for you in Markdown and text formats.
