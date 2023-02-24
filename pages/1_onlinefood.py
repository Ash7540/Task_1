import streamlit as st
from matplotlib import image
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "food1.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "onlinefoods.csv")

st.title("Visualization Dashboard")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)

st.subheader("Data Records")
st.dataframe(df)

st.subheader("Data Visualization by Histogram And BoxPlot")
st.caption('Data Histogram plot against feedback')
species = st.selectbox("Select the Feedback Type:", df['Feedback'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Feedback'] == species], x="Family size")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['Feedback'] == species], x="Monthly Income")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3= px.histogram(df[df['Feedback'] == species], x="Age")
col1.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.histogram(df[df['Feedback'] == species], x="Gender")
col2.plotly_chart(fig_4, use_container_width=True)

fig_5 = px.histogram(df[df['Feedback'] == species], x="Occupation")
col1.plotly_chart(fig_5, use_container_width=True)

fig_6 = px.histogram(df[df['Feedback'] == species], x="Marital Status")
col2.plotly_chart(fig_6, use_container_width=True)


st.subheader("Online Food Order Visualization Through Region")
st.map(df)
