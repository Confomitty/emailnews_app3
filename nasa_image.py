import time
import requests
import streamlit as st
import os

api_key2 = os.getenv("API_KEY2")

url = ("https://api.nasa.gov/planetary/apod?"
       "api_key=api_key2")

response = requests.get(url)
info = response.json()
print(info)

st.header("Astronomy Image of The Day" , text_alignment="center")
st.text(time.strftime("%d %B %Y") , text_alignment="center")
st.subheader(info["title"])
st.image(info["hdurl"])
st.text(info["explanation"])
st.subheader("by " + info["copyright"])




