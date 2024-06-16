# Newnham Recreation Centre Dashboard
This project is a data analysis and visualization application for the Newnham Recreation Centre. It is built using Streamlit and leverages various Python libraries such as pandas and matplotlib for data processing and visualization.


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Data Privacy Considerations](#data-privacy-considerations)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgements)


## Overview
The Newnham Recreation Centre Dashboard provides insights into member demographics, activity trends, facility usage patterns, and member preferences. The application allows users to visualize and analyze data through various interactive plots.


## Features
- **Member Demographics**: View distributions of members by campus, gender, age group, and registration trends.
- **Member Activity Trends**: Analyze entry trends by day of the week and by time of day.
- **Facility Usage Patterns**: Explore overall usage trends, peak usage times, and usage distribution by day of the week.
- **Member Preferences**: Examine preferred facilities by gender and age group.


## Data Privacy Considerations
To protect member privacy, all data analysis for this project was conducted locally on secure servers using anonymized data. Results were stored in CSV files under the `data` directory, ensuring that no personally identifiable information is exposed or transmitted outside of controlled environments.


## Requirements
- Python 3.7 or higher
- Streamlit
- Pandas
- Matplotlib
- openpyxl
- dotenv


## Project Structure
```
.
├── analysis
│ ├── facility_usage.py
│ ├── member_activity.py
│ ├── member_distribution.py
│ ├── member_segmentation.py
├── utils
│ ├── data_loader.py
│ └── preprocess_data.py
├── data
│ ├── age_distribution.csv
│ ├── campus_distribution.csv
│ ├── entry_trends_day.csv
│ ├── entry_trends_time.csv
│ ├── facility_age.csv
│ ├── facility_distribution.csv
│ ├── facility_gender.csv
│ ├── facility_usage.csv
│ ├── gender_distribution.csv
│ ├── peak_times.csv
│ └── registration_date_trends.csv
├── app.py
├── preprocess.py
├── requirements.txt
├── .env
└── README.md
```
- **analysis**: Contains modules for generating various plots and visualizations.
- **utils**: Contains the data loading utility.
- **data**: Directory where preprocessed data files are stored, including CSV files generated from member and entry records.
- **app.py**: Main application script.
 **preprocess.py**: Script for preprocessing member and entry data, generating CSV files used for analysis.
- **requirements.txt**: Lists the dependencies required for the project.
- **.env**: Environment file for configuration


## Acknowledgements
- This project was created using the [Streamlit](https://streamlit.io/) library.
- Data processing was done using the [Pandas](https://pandas.pydata.org/) library.
- Visualization were generated using the [Matplotlib](https://matplotlib.org/) library.