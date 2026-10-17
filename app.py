import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Val CID Pulse",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Val CID Pulse")

st.markdown("""
### SDO Valenzuela CID Real-Time Monitoring Dashboard

Val CID Pulse provides real-time monitoring of Programs, Projects, and Activities (PPAs) of the Curriculum Implementation Division, supporting evidence-based planning, implementation, monitoring, and decision-making.
""")

# ===================================
# REPLACE THIS WITH YOUR ONEDRIVE LINK
# ===================================
EXCEL_URL = "https://depedph-my.sharepoint.com/:x:/g/personal/melvinwilly_roque_deped_gov_ph/IQCcUYJbOAteQKkFfISGLUyKASVSYUndL89Jz32_Qu7vsRM?e=9sLQAd"

@st.cache_data(ttl=60)
def load_data():
    return pd.read_excel(EXCEL_URL)

try:
    df = load_data()

    st.success("✅ Connected to Online Excel File")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total PPAs",
        len(df)
    )

    col2.metric(
        "Records",
        len(df.index)
    )

    col3.metric(
        "Last Refresh",
        datetime.now().strftime("%H:%M:%S")
    )

    st.divider()

    st.subheader("PPA Monitoring Data")

    st.dataframe(
        df,
        use_container_width=True
    )

except Exception as e:

    st.error("Unable to load data.")

    st.write(e)
