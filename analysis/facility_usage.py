# analysis/facility_usage.py
import matplotlib.pyplot as plt
import streamlit as st

def plot_facility_usage(facility_usage):
    colors = ['#4e79a6', '#f28e2c', '#e15659', '#76b7b1','#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
    plt.figure(figsize=(10, 6))
    ax = facility_usage.plot(kind='bar', color=colors[:len(facility_usage)])
    ax.set_title('Facility Usage Trends')
    ax.set_xlabel('Facility')
    ax.set_ylabel('Number of Entries')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    st.pyplot(plt)

def plot_peak_times(peak_times_df):
    plt.figure(figsize=(10, 6))
    for facility in peak_times_df.columns:
        plt.plot(peak_times_df.index, peak_times_df[facility], label=facility)
    plt.title('Peak Times for Facility Usage')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Entries')
    plt.legend()
    st.pyplot(plt)

def plot_facility_distribution(facility_dist):
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    facility_dist = facility_dist.reindex(day_order)
    plt.figure(figsize=(10, 6))
    for facility in facility_dist.columns:
        plt.plot(facility_dist.index, facility_dist[facility], label=facility)
    plt.title('Facility Usage Distribution by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Entries')
    plt.legend()
    st.pyplot(plt)
