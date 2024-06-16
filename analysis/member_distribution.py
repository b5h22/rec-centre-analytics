# analysis/member_distribution.py
import matplotlib.pyplot as plt
import streamlit as st

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
    plt.figure(figsize=(10, 6))
    ax = reg_trends.plot(kind='line', color='blue')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.title('Registration Date Trends')
    plt.xlabel('Week')
    plt.ylabel('Number of Registrations')
    st.pyplot(plt)