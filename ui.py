import streamlit as st

st.title("MS Klubů – Predikce zápasů")

home = st.text_input("Domácí tým", "Juventus")
away = st.text_input("Hostující tým", "Manchester City")

if st.button("Predikovat"):
    # Simulovaná predikce (můžeš později nahradit modelem)
    st.subheader("📊 Pravděpodobnost výsledku")
    st.json({
        "Výhra domácích": 0.55,
        "Remíza": 0.25,
        "Výhra hostů": 0.20
    })

    st.subheader("⚽ Očekávané góly")
    st.json({
        home: 1.8,
        away: 1.2
    })

    st.subheader("🟨 Očekávané žluté karty")
    st.json({
        home: 1.5,
        away: 1.1
    })
