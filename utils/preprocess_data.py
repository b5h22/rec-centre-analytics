# utils/preprocess_data.py
import os
from dotenv import load_dotenv
import pandas as pd
from utils.data_loader import load_members_data, load_entries_data

# Load environment variables from .env file
load_dotenv()

# Load data using environment variables
members_data_path = os.getenv('MEMBERS_DATA_PATH')
entries_data_path = os.getenv('ENTRIES_DATA_PATH')

members_df = load_members_data(members_data_path)
entries_df = load_entries_data(entries_data_path, members_df)

# Perform analysis and save results
def save_analysis_results():
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)  # Create data directory if it doesn't exist
    
    gender_dist = members_df['gender'].value_counts()
    gender_dist.to_csv(os.path.join(data_dir, 'gender_distribution.csv'))
    
    age_dist = members_df['age_group'].value_counts().sort_index()
    age_dist.to_csv(os.path.join(data_dir, 'age_distribution.csv'))
    
    campus_dist = members_df['campus'].value_counts()
    campus_dist.to_csv(os.path.join(data_dir, 'campus_distribution.csv'))
    
    reg_trends = members_df['registration_date'].dt.to_period('W').value_counts().sort_index()
    reg_trends.to_csv(os.path.join(data_dir, 'registration_date_trends.csv'))
    
    entry_trends_day = entries_df['day_of_week'].value_counts().reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    entry_trends_day.to_csv(os.path.join(data_dir, 'entry_trends_day.csv'))
    
    entry_trends_time = entries_df['hour_of_day'].value_counts().sort_index()
    entry_trends_time.to_csv(os.path.join(data_dir, 'entry_trends_time.csv'))
    
    facility_usage = entries_df['facility'].value_counts()
    facility_usage.to_csv(os.path.join(data_dir, 'facility_usage.csv'))
    
    peak_times_df = entries_df.groupby(['hour_of_day', 'facility']).size().unstack()
    peak_times_df.to_csv(os.path.join(data_dir, 'peak_times.csv'))
    
    facility_dist = entries_df.groupby(['day_of_week', 'facility']).size().unstack()
    facility_dist.to_csv(os.path.join(data_dir, 'facility_distribution.csv'))
    
    facility_gender = entries_df.groupby(['gender', 'facility']).size().unstack().fillna(0)
    facility_gender.to_csv(os.path.join(data_dir, 'facility_gender.csv'))
    
    facility_age = entries_df.groupby(['age_group', 'facility']).size().unstack().fillna(0)
    facility_age.to_csv(os.path.join(data_dir, 'facility_age.csv'))

save_analysis_results()
