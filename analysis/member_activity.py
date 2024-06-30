# analysis/member_activity.py
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import streamlit as st

def plot_entry_trends_day(entry_trends_day):
    cmap = mcolors.LinearSegmentedColormap.from_list("gradient", ["#E1F5FE", "#01579B"])
    norm = mcolors.Normalize(vmin=0, vmax=entry_trends_day.max())
    plt.figure(figsize=(10, 6))
    ax = entry_trends_day.plot(kind='bar', color=[cmap(norm(value)) for value in entry_trends_day])
    ax.set_title('All Facilities Entry Trends by Day of the Week')
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Number of Entries')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    st.pyplot(plt)

def plot_entry_trends_time(entry_trends_time):
    cmap = mcolors.LinearSegmentedColormap.from_list("gradient", ["#E1F5FE", "#01579B"])
    norm = mcolors.Normalize(vmin=0, vmax=entry_trends_time.max())
    plt.figure(figsize=(10, 6))
    ax = entry_trends_time.plot(kind='bar', color=[cmap(norm(value)) for value in entry_trends_time])
    ax.set_title('All Facilities Entry Trends by Time of Day')
    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Number of Entries')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    st.pyplot(plt)
