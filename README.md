# AirportDataAnalysis

## Overview
This project processes and analyzes airport data from a CSV file. It filters airport locations based on specific latitude and longitude ranges, extracts key details, and stores them in separate text files. Additionally, the project visualizes airport locations using Matplotlib and Basemap.

## Features
- Reads and processes airport data from a CSV file.
- Filters airports based on latitude and longitude.
- Generates multiple text files for specific airport data:
  - **Airport Location.txt**: Stores airport names with their latitude and longitude.
  - **Airport Specific.txt**: Contains airports within a specified coordinate range.
  - **Negative Longitude.txt**: Includes airports with negative longitude values.
- Uses Python visualization libraries for mapping airport locations.
- Generates a flowchart of the program logic using `pyflowchart`.

## Requirements
Ensure you have the following Python libraries installed:
```sh
pip install pandas matplotlib basemap pyflowchart
```

## Usage
1. Place your `airports.csv` file in the project directory.
2. Run the main script:
   ```sh
   python "Part A & B.py"
   ```
3. The script will generate text files containing filtered airport data.
4. Run `partb assignment.py` to generate a flowchart of the program logic:
   ```sh
   python "partb assignment.py"
   ```

## File Structure
```
/airport-data-analysis
│── Part A & B.py            # Main script for processing airport data
│── partb assignment.py      # Script for generating a flowchart
│── airports.csv             # Input CSV file (must be provided by the user)
│── Airport Location.txt     # Output text file with airport locations
│── Airport Specific.txt     # Output text file with specific airport data
│── Negative Longitude.txt   # Output text file with negative longitude airports
│── README.md                # Project documentation
```

## License
This project is open-source and available for modification and distribution.

