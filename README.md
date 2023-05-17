# Environment Setup

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

# Input Configuration

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

# Output

Once the script finishes running, results generated will be displayed in the terminal or command prompt. The script will generate database file in main directory `vehicles_data.sqlite3`.

Congratulations! You have successfully set up the environment, configured the input, and executed the script. Now you can enjoy the informative and beautiful output provided by the script. Feel free to explore and modify the code to suit your needs.
