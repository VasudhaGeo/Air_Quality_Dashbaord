import streamlit as st
import requests
import pandas as pd


st.set_page_config(
page_title = "Air quality",
layout = "wide"
)

st.title ("Air Quality Dashboard")

API_KEY = st.secrets["API_KEY"]

city = st.text_input("Enter city", "Delhi")

url = f"https://api.waqi.info/feed{city}/?token={API_KEY}"

response = requests.get(url).json()

if response ["status"] == "ok":
    data = response["data"]
    st.subheader(f"Air Quality in {city}")
    st.metric("AQI", data["aqi"])
    iaqi = data["iaqi"]

    pollutant = {}
    for x in iaqi :
        pollutant[x] = iaqi[x]["v"]

    df = pd.DataFrame(list(pollutant.items())),
    columns = ["Pollutants", "Value"]

    st.bar_chart(df.set_index("Pollutants"))
else:
    st.error("City not found")
