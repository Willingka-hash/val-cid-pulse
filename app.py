import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Val CID Pulse",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Val CID Pulse")

st.markdown("""
### SDO Valenzuela CID Real-Time Monitoring Dashboard
""")

df = pd.read_excel("CID-PPAs DASHBOARD.xlsx")

st.success("✅ Data Connected")

st.write(df)
