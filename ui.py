import streamlit as st
import requests
from scipy.stats import poisson
import numpy as np

API_TOKEN = "jJ4U44WVzIGCm7L5hkT1iWHFlfMoKjeHLSfMn3cv84kidEmeT3c7GFf6c5Bm"
BASE_URL = "https://api.sportmonks.com/v3/football"

def get_match_stats(match_id):
    url = f"{BASE_URL}/fixtures/{match_id}"
    params = {"api_token": API_TOKEN, "include": "stats,events"}
    res = requests.get(url, params=params)
    if res.status_code != 200:
        return None
    data = res.json()["data"]
    return {
        "home_team": data["home_team"]["name"],
        "away_team": data["away_team"]["name"],
        "home_goals": data["scores"]["home_score"],
        "away_goals": data["scores"]["away_score"],
        "home_yellow": sum(1 for e in data["events"] if e["type"] == "yellowcard" and e["team_id"] == data["home_team_id"]),
        "away_yellow": sum(1 for e in data["events"] if e["type"] == "yellowcard" and e["team_id"] == data["away_team_id"]),
    }

def predict_goals(avg_home, avg_away):
    return poisson(avg_home).mean(), poisson(avg_away).mean()

st.title("🔮 MS Klubů – Predikce se živými daty")

match_id = st.text_input("Match ID (ze Sportmonks)", "")

if st.button("Načíst a predikovat"):
    stats = get_match_stats(match_id)
    if not stats:
        st.error("❌ Nepodařilo se načíst data. Zkontroluj match ID nebo API token.")
    else:
        st.subheader("📊 Pravděpodobnost výsledku (simulovaná)")
        home_win = 0.55
        draw = 0.25
        away_win = 0.20
        st.json({
            f"Výhra {stats['home_team']}": home_win,
            "Remíza": draw,
            f"Výhra {stats['away_team']}": away_win
        })

        st.subheader("⚽ Skóre (aktuální)")
        st.write({
            stats["home_team"]: stats["home_goals"],
            stats["away_team"]: stats["away_goals"]
        })

        st.subheader("🟨 Žluté karty")
        st.write({
            stats["home_team"]: stats["home_yellow"],
            stats["away_team"]: stats["away_yellow"]
        })
