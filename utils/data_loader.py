#utils/data_loader.py
import pandas as pd
from datetime import datetime, time

def load_members_data(filepath):
  try:
    members_df = pd.read_excel(filepath, sheet_name='Members')
    members_df['registration_date'] = pd.to_datetime(members_df['registration_date'])

    # Create age group column
    age_bins = [0, 20, 30, 40, 50, float('inf')]
    age_labels = ['Under 20', '20-29', '30-39', '40-49', '50+']
    members_df['age_group'] = pd.cut(members_df['age'], bins=age_bins, labels=age_labels)

    return members_df
  except Exception as e:
    raise RuntimeError(f"Failed to load members data: {e}")

def load_entries_data(filepath, members_df, log_unmatched=True):
  try:
    xls = pd.ExcelFile(filepath)
    entries_df = pd.concat([pd.read_excel(xls, sheet_name=sheet) for sheet in xls.sheet_names])
    entries_df['date'] = pd.to_datetime(entries_df['date'])

    def parse_time(x):
      if isinstance(x, str):
        return datetime.strptime(x, '%H:%M:%S').time()
      elif isinstance(x, datetime):
        return x.time()
      elif isinstance(x, time):
        return x
      else:
        raise ValueError(f"Unexpected time format: {x}")
    entries_df['time'] = entries_df['time'].apply(parse_time)
    entries_df['entry_time'] = entries_df.apply(lambda row: pd.Timestamp.combine(row['date'], row['time']), axis=1)
    entries_df['day_of_week'] = entries_df['entry_time'].dt.day_name()
    entries_df['hour_of_day'] = entries_df['entry_time'].dt.hour

    # Filter out unmatched entries
    matched_entries_df = entries_df[entries_df['member_id'].isin(members_df['member_id'])]
    unmatched_entries_df = entries_df[~entries_df['member_id'].isin(members_df['member_id'])]

    # Merge with members_df to get 'gender' and other member info
    merged_df = pd.merge(matched_entries_df, members_df, on='member_id', how='left')

    return merged_df
  except Exception as e:
    raise RuntimeError(f"Failed to load entries data: {e}")
