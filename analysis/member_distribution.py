# analysis/member_distribution.py
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def plot_gender_distribution(gender_dist):
    colors = ['#4e79a6', '#f28e2c', '#e15659', '#76b7b1','#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
    plt.figure(figsize=(10, 6))
    ax = gender_dist.plot(kind='bar', color=colors)
    ax.set_title('Gender Distribution')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Number of Members')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    st.pyplot(plt)

def plot_age_distribution(age_dist):
    colors = ['#4e79a6', '#f28e2c', '#e15659', '#76b7b1','#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
    plt.figure(figsize=(10, 6))
    ax = age_dist.plot(kind='bar', color=colors)
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age Group')
    ax.set_ylabel('Number of Members')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    st.pyplot(plt)

def plot_campus_distribution(campus_dist):
    colors = ['#4e79a6', '#f28e2c', '#e15659', '#76b7b1','#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
    plt.figure(figsize=(10, 6))
    ax = campus_dist.plot(kind='bar', color=colors)
    ax.set_title('Campus Distribution')
    ax.set_xlabel('Campus')
    ax.set_ylabel('Number of Members')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    st.pyplot(plt)

def plot_registration_date_trends(reg_trends):
    reg_trends.index = pd.to_datetime(reg_trends.index.str.split('/').str[0], format='%Y-%m-%d')
    plt.figure(figsize=(10, 6))
    ax = reg_trends.plot(kind='line', color='blue', legend=False)

    plt.title('Registration Date Trends')
    plt.xlabel('Week')
    plt.ylabel('Number of Registrations')
    custom_labels = {
        '2023-08-28': 'Sep\n2023',
        '2023-09-25': 'Oct',
        '2023-10-30': 'Nov',
        '2023-11-27': 'Dec'
    }
    labels = [''] * len(reg_trends.index)
    for i, date in enumerate(reg_trends.index):
        if date.strftime('%Y-%m-%d') in custom_labels:
            labels[i] = custom_labels[date.strftime('%Y-%m-%d')]
    ax.set_xticks(reg_trends.index)
    ax.set_xticklabels(labels, rotation=45)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    st.pyplot(plt)