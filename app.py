import streamlit as st
import pandas as pd

# Titul
st.title("📈 Forex Dashboard")

# Forex páry
forex_pairs = [
    "EUR/USD", "USD/JPY", "GBP/USD", "USD/CHF", "AUD/USD", "USD/CAD",
    "NZD/USD", "EUR/GBP", "EUR/JPY", "GBP/JPY", "AUD/JPY", "CHF/JPY",
    "EUR/AUD", "EUR/CAD", "AUD/CAD", "NZD/JPY", "GBP/CHF", "CAD/JPY",
    "AUD/NZD", "USD/SGD", "EUR/NZD", "EUR/CHF", "GBP/AUD", "GBP/CAD",
    "USD/NOK", "USD/SEK", "USD/MXN", "USD/TRY", "USD/ZAR", "EUR/SEK"
]

pair = st.selectbox("Vyber Forex pár:", forex_pairs)

# Ukážkové dáta
st.subheader("📰 Ekonomické správy (demo)")
st.write("• NFP: 250k vs 200k očakávania — pozitívne pre USD")
st.write("• CPI: 3.2% vs 3.1% očakávania — neutrálne")
st.write("• PMI: 49.5 vs 51.0 očakávania — negatívne pre USD")

st.subheader("📊 COT Report (demo)")
st.bar_chart(pd.DataFrame({"Net Position": [30, -10, 20]}, index=["Large Traders", "Retail", "Commercials"]))

st.subheader("💵 DXY Index (demo)")
st.metric(label="DXY Index", value="104.30", delta="+0.20")

st.subheader("📅 Sezonalita (demo)")
st.line_chart(pd.DataFrame({
    "January": [1.0], "February": [1.2], "March": [1.1],
    "April": [1.3], "May": [1.0]
}).T)
