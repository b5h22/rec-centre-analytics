# app.py
import os
import pandas as pd
import streamlit as st
from analysis.member_distribution import plot_gender_distribution, plot_age_distribution, plot_campus_distribution, plot_registration_date_trends
from analysis.member_activity import plot_entry_trends_day, plot_entry_trends_time
from analysis.facility_usage import plot_facility_usage, plot_peak_times, plot_facility_distribution
from analysis.member_segmentation import plot_preferred_facilities_by_gender, plot_preferred_facilities_by_age

# Load preprocessed result files
def load_preprocessed_data():
    data_dir = 'data'
    
    gender_dist = pd.read_csv(os.path.join(data_dir, 'gender_distribution.csv'), index_col=0)
    age_dist = pd.read_csv(os.path.join(data_dir, 'age_distribution.csv'), index_col=0)
    campus_dist = pd.read_csv(os.path.join(data_dir, 'campus_distribution.csv'), index_col=0)
    reg_trends = pd.read_csv(os.path.join(data_dir, 'registration_date_trends.csv'), index_col=0)
    entry_trends_day = pd.read_csv(os.path.join(data_dir, 'entry_trends_day.csv'), index_col=0)
    entry_trends_time = pd.read_csv(os.path.join(data_dir, 'entry_trends_time.csv'), index_col=0)
    facility_usage = pd.read_csv(os.path.join(data_dir, 'facility_usage.csv'), index_col=0)
    peak_times_df = pd.read_csv(os.path.join(data_dir, 'peak_times.csv'), index_col=0)
    facility_dist = pd.read_csv(os.path.join(data_dir, 'facility_distribution.csv'), index_col=0)
    facility_gender = pd.read_csv(os.path.join(data_dir, 'facility_gender.csv'), index_col=0)
    facility_age = pd.read_csv(os.path.join(data_dir, 'facility_age.csv'), index_col=0)
    
    return {
        "gender_dist": gender_dist.squeeze(),
        "age_dist": age_dist.squeeze(),
        "campus_dist": campus_dist.squeeze(),
        "reg_trends": reg_trends.squeeze(),
        "entry_trends_day": entry_trends_day.squeeze(),
        "entry_trends_time": entry_trends_time.squeeze(),
        "facility_usage": facility_usage.squeeze(),
        "peak_times_df": peak_times_df,
        "facility_dist": facility_dist,
        "facility_gender": facility_gender,
        "facility_age": facility_age
    }

data = load_preprocessed_data()

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
        plot_campus_distribution(data["campus_dist"])
    elif plot_option == "Gender Distribution":
        plot_gender_distribution(data["gender_dist"])
    elif plot_option == "Age Distribution":
        plot_age_distribution(data["age_dist"])
    elif plot_option == "Registration Trends":
        plot_registration_date_trends(data["reg_trends"])

elif menu_selection == "Member Activity Trends":
    plot_option = st.radio("Select View", ("Entry Trends by Day", "Entry Trends by Time"))
    if plot_option == "Entry Trends by Day":
        plot_entry_trends_day(data["entry_trends_day"])
    elif plot_option == "Entry Trends by Time":
        plot_entry_trends_time(data["entry_trends_time"])

elif menu_selection == "Facility Usage Patterns":
    plot_option = st.radio("Select View", ("Overall Usage Trends", "Peak Usage Times", "Usage Distribution by Day"))
    if plot_option == "Overall Usage Trends":
        plot_facility_usage(data["facility_usage"])
    elif plot_option == "Peak Usage Times":
        plot_peak_times(data["peak_times_df"])
    elif plot_option == "Usage Distribution by Day":
        plot_facility_distribution(data["facility_dist"])

elif menu_selection == "Member Preferences":
    plot_option = st.radio("Select View", ("Preferred Facilities by Gender", "Preferred Facilities by Age Group"))
    if plot_option == "Preferred Facilities by Gender":
        plot_preferred_facilities_by_gender(data["facility_gender"])
    elif plot_option == "Preferred Facilities by Age Group":
        plot_preferred_facilities_by_age(data["facility_age"])
