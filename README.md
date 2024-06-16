# Newnham Recreation Centre Dashboard
This project is a data analysis and visualization application for the Newnham Recreation Centre. It is built using Streamlit and leverages various Python libraries such as pandas and matplotlib for data processing and visualization.


## Table of Contents
- [Overview](#overview)
- [Features](#features)
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
│   ├── facility_usage.py
│   ├── member_activity.py
│   ├── member_distribution.py
│   ├── member_segmentation.py
├── utils
│   ├── data_loader.py
├── app.py
├── requirements.txt
├── .env
└── README.md
```
- **analysis**: Contains modules for generating various plots and visualizations.
- **utils**: Contains the data loading utility.
- **app.py**: Main application script.
- **requirements.txt**: Lists the dependencies required for the project.
- **.env**: Environment file for configuration


## Acknowledgements
- This project was created using the [Streamlit](https://streamlit.io/) library.
- Data processing was done using the [Pandas](https://pandas.pydata.org/) library.
- Visualization were generated using the [Matplotlib](https://matplotlib.org/) library.