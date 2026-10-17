import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Val CID Pulse",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Val CID Pulse")

FILE_URL = "https://depedph-my.sharepoint.com/personal/melvinwilly_roque_deped_gov_ph/Documents/CID-PPAs%20DASHBOARD.xlsx"

try:
    df = pd.read_excel(FILE_URL)

    st.success("✅ Connected Successfully")

    st.write(df.head())

except Exception as e:
    st.error("Connection Failed")

    st.code(str(e))
