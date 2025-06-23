import streamlit as st
import requests

st.title("MS Klubů – Predikce zápasů")

home = st.text_input("Domácí tým", "Juventus")
away = st.text_input("Hostující tým", "Manchester City")

if st.button("Predikovat"):
    res = requests.post("https://wc.onrender.com/predict", json={"home_team": home, "away_team": away})
    st.json(res.json())
