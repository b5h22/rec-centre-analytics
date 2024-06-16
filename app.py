# app.py
import os
from dotenv import load_dotenv
import streamlit as st
from utils.data_loader import load_members_data, load_entries_data
from analysis.member_distribution import plot_gender_distribution, plot_age_distribution, plot_campus_distribution, plot_registration_date_trends
from analysis.member_activity import plot_entry_trends_day, plot_entry_trends_time
from analysis.facility_usage import plot_facility_usage, plot_peak_times, plot_facility_distribution
from analysis.member_segmentation import plot_preferred_facilities_by_gender, plot_preferred_facilities_by_age

# Load environment variables from .env file
load_dotenv()

# Load data using environment variables
members_data_path = os.getenv('MEMBERS_DATA_PATH')
entries_data_path = os.getenv('ENTRIES_DATA_PATH')

if not members_data_path or not entries_data_path:
    st.error("Please define MEMBERS_DATA_PATH and ENTRIES_DATA_PATH in .env file.")
    st.stop()

members_df = load_members_data(members_data_path)
entries_df = load_entries_data(entries_data_path, members_df)

# Streamlit app layout
st.title('Newnham Recreation Centre Dashboard')

# Menu bar
menu_options = [
    "Member Demographics",
    "Member Activity Trends",
    "Facility Usage Patterns",
    "Member Preferences"
]
menu_selection = st.selectbox("Select Analysis Category", menu_options)

if menu_selection == "Member Demographics":
    plot_option = st.radio("Select View", ("Campus Distribution", "Gender Distribution", "Age Distribution", "Registration Trends"))
    if plot_option == "Campus Distribution":
        plot_campus_distribution(members_df)
    elif plot_option == "Gender Distribution":
        plot_gender_distribution(members_df)
    elif plot_option == "Age Distribution":
        plot_age_distribution(members_df)
    elif plot_option == "Registration Trends":
        plot_registration_date_trends(members_df)

elif menu_selection == "Member Activity Trends":
    plot_option = st.radio("Select View", ("Entry Trends by Day", "Entry Trends by Time"))
    if plot_option == "Entry Trends by Day":
        plot_entry_trends_day(entries_df)
    elif plot_option == "Entry Trends by Time":
        plot_entry_trends_time(entries_df)

elif menu_selection == "Facility Usage Patterns":
    plot_option = st.radio("Select View", ("Overall Usage Trends", "Peak Usage Times", "Usage Distribution by Day"))
    if plot_option == "Overall Usage Trends":
        plot_facility_usage(entries_df)
    elif plot_option == "Peak Usage Times":
        plot_peak_times(entries_df)
    elif plot_option == "Usage Distribution by Day":
        plot_facility_distribution(entries_df)

elif menu_selection == "Member Preferences":
    plot_option = st.radio("Select View", ("Preferred Facilities by Gender", "Preferred Facilities by Age Group"))
    if plot_option == "Preferred Facilities by Gender":
        plot_preferred_facilities_by_gender(entries_df)
    elif plot_option == "Preferred Facilities by Age Group":
        plot_preferred_facilities_by_age(entries_df)
