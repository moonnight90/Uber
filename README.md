# Uber Price Estimator

This repository contains a Python script for estimating Uber prices between pickup and destination locations. The script utilizes the Uber API to fetch price estimates and saves the data to an SQLite database named "vehicles_data.sqlite3". The script also uses pandas library to read the input locations from a CSV file.


## Environment Setup

Before running the script, please make sure you have Python installed on your computer.

## Prerequisites

- Python: If you don't have Python installed, you can download it from the official Python website [python.org](https://www.python.org/). Follow the installation instructions specific to your operating system.

## Installation

To set up the environment for running the script, follow these steps:

1. Open the terminal or command prompt in the main directory of your project.

2. It is recommended to create a virtual environment for your project to keep the dependencies isolated. Run the following command to create a virtual environment (optional):

   ```
   python -m venv env
   ```

   Activate the virtual environment:
   - For Windows:
     ```
     .\env\Scripts\activate
     ```

     For macOS/Linux:
     ```
     source env/bin/activate
     ```

3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
   This command will install all the necessary packages listed in the `requirements.txt` file.

## Input Configuration

To configure the input for the script, follow these steps:

1. Locate the `input.csv` file in your project directory and open it using a text editor or spreadsheet application.

2. The `input.csv` file likely contains columns such as `origination` and `destination`. Replace the existing values in these columns with your desired origination and destination locations. You can add additional columns or modify the existing ones according to your specific use case.

3. Save the changes to the `input.csv` file.

# Running the Script

To execute the script, follow these steps:

1. Open the terminal or command prompt in the main directory of your project.

2. Make sure you have activated the virtual environment if you created one.

3. Run the script by entering one of the following commands, depending on your operating system:
   - For Windows:
     ```
     python main.py
     ```

   - For macOS/Linux:
     ```
     python3 main.py
     ```

   This command will execute the `main.py` script and initiate the processing of your input data.

## Output

Once the script finishes running, results generated will be displayed in the terminal or command prompt. The script will generate database file in project directory `vehicles_data.sqlite3`.

## How it Works

1. The script defines a function called `create_vehicle_table` that creates a table in the SQLite database to store vehicle-related data. The function takes the vehicle type as an argument and defines the table schema with columns for various fields such as date of entry, time of entry, origination address, destination address, minimum price, and maximum price.

2. Another function called `insert_data` is defined to insert data into the respective vehicle table. The function takes the vehicle type, origination address, destination address, minimum price, and maximum price as arguments. The current date and time are automatically added to the entry.

3. The `get_table_names` function retrieves the names of the existing tables in the SQLite database. This information is used to prevent duplicate table creations.

4. The `Uber` class encapsulates the functionality related to fetching Uber price estimates. It initializes a session object with the necessary headers for API requests.

5. The `split_price` method is used to extract the minimum and maximum prices from the fare string returned by the Uber API.

6. The `get_suggestions` method sends a POST request to the Uber API to get location suggestions based on the query. It returns the ID and provider information for the first suggestion, if available.

7. The `get_detail` method fetches detailed information about a location based on its ID and provider. It sends a POST request to the Uber API and retrieves latitude, longitude, and full address details.

8. The `load_estimate` method sends a POST request to the Uber API to fetch the price estimates for a given pickup and destination. It yields each vehicle type and the corresponding fare string.

9. The `run` method orchestrates the estimation process. It calls the appropriate methods to retrieve suggestions and details for the pickup and destination locations. It then calls the `load_estimate` method to fetch price estimates for each vehicle type. The estimated prices and location details are stored in the SQLite database.

10. In the main section of the script, the input locations are read from the "input.csv" file using pandas. A connection is established with the SQLite database, and existing table names are retrieved. The `run` method of the `Uber`

 class is called for each location to estimate Uber prices and store them in the database.

Congratulations! You have successfully set up the environment, configured the input, and executed the script. Now you can enjoy the informative and beautiful output provided by the script. Feel free to explore and modify the code to suit your needs.
