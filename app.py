import streamlit as st
import os
from PIL import Image


st.title("Ashwin Chavan PortFolio :sunglasses:")
st.caption("Data Scientist")
st.snow()
image = Image.open('2.jpg')

st.image(image, caption='Proud to Be Data Scientist')

st.header("About Me")
st.text('Aspiring to Become Data Scientist with a good knowledge. Eager to Learn New Things and Try My Knowledge to Help to Grow The Technology Field.')
st.text('Moving towards my Goals and to go on top')
st.text('Having good Qualities to Lead a Team.')
st.text("Skilled in Python, Data Analysis and Web Development.")

st.subheader("Let's Connect:-")
st.text("LinkedIn:- ")
if st.button(' Click Here to Connect with me'):
    st.write('https://www.linkedin.com/in/ashwin-chavan-30175a213/')
    st.balloons()

st.text("GitHub:- ")
if st.button(' Click Here to Connect'):
    st.write('https://github.com/Ash7540')
    st.balloons()

st.text("Instagram:- ")
if st.button(' Click Here to Connect on Instagram'):
    st.image('3.png')
    st.balloons()
