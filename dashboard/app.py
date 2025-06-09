
import streamlit as st
import pandas as pd
import os
from utils.config import LOG_CSV, SNAPSHOT_DIR

st.title("📊 Smart Surveillance Dashboard")

if os.path.exists(LOG_CSV):
    df = pd.read_csv(LOG_CSV)
    st.write("### Motion Event Log", df)

    for _, row in df.tail(5).iterrows():
        path = os.path.join(SNAPSHOT_DIR, row['filename'])
        st.image(path, caption=f"Detected at {row['timestamp']}", width=300)
else:
    st.info("No motion data available yet.")
