import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Val CID Pulse",
    layout="wide"
)

st.title("📊 Val CID Pulse")

st.markdown("""
**Val CID Pulse** is a real-time monitoring dashboard for the Curriculum Implementation Division (CID) of SDO Valenzuela, providing up-to-date insights on the implementation status, accomplishments, timelines, and budget utilization of PPAs.
""")

# CHANGE THIS LATER TO YOUR ONEDRIVE LINK
EXCEL_URL = "YOUR_ONEDRIVE_LINK_HERE"

@st.cache_data(ttl=60)
def load_data():
    return pd.read_excel(EXCEL_URL)

try:
    df = load_data()

    total_ppa = len(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total PPAs", total_ppa)
    col2.metric("Last Refresh", datetime.now().strftime("%H:%M"))
    col3.metric("Records", len(df))

    st.divider()

    st.subheader("PPA Data")

    st.dataframe(
        df,
        use_container_width=True
    )

except Exception as e:

    st.error(
        "Unable to load Excel file."
    )

    st.write(e)
