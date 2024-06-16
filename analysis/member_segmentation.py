#analysis/member_segmentation.py
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_preferred_facilities_by_gender(facility_gender):
    colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#f7b7a3']
    wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
    
    for gender in facility_gender.index:
        data = facility_gender.loc[gender]
        data = data[data > 0]
        plt.figure(figsize=(8, 8))
        plt.pie(data, labels=data.index, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors[:len(data)], wedgeprops=wedgeprops)
        plt.title(f'Preferred Facilities by Gender: {gender}')
        st.pyplot(plt)

def plot_preferred_facilities_by_age(facility_age):
    colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#f7b7a3']
    wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
    
    for age in facility_age.index:
        data = facility_age.loc[age]
        data = data[data > 0]
        plt.figure(figsize=(8, 8))
        plt.pie(data, labels=data.index, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors[:len(data)], wedgeprops=wedgeprops)
        plt.title(f'Preferred Facilities by Age: {age}')
        st.pyplot(plt)