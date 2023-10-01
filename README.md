# Survey Data Processing Tool

This Python script is designed to process survey data collected in CSV format, perform data transformations, and generate a clean output in CSV format. It is particularly useful for surveys with multiple-choice questions and can be customized to fit various survey structures.

## Features

- **Data Concatenation:** Combines data from multiple CSV files vertically into a single DataFrame.
- **Column Renaming:** Renames survey columns for clarity and ease of reference.
- **Data Reshaping:** Converts wide-format survey data into long format using the `melt` function.
- **Data Cleaning:** Standardizes and cleans response data.
- **Custom Order:** Sets a custom order for survey questions.
- **Option Mapping:** Maps survey response options to specific values.
- **Output Generation:** Generates a cleaned CSV file with processed survey data.

## Usage

1. Clone this repository to your local machine.
2. Run the Python script `main.py`.
3. The cleaned survey data will be saved as `clean_data.csv` in the "Output" directory.


