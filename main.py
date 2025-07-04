import streamlit as st
import pandas as pd
import sqlite3

from db import init_db, get_all_residents, add_resident, delete_resident
from camera_utils import process_camera

import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call this at the top of your main.py, adjust the filename accordingly:
add_bg_from_local("background.jpeg")


# Set page settings
st.set_page_config(page_title="Smart Gate OCR", page_icon="🚘", layout="wide")

# Initialize database
init_db()

# ============================ SIDEBAR ============================

st.sidebar.markdown("## 🏠 Resident Vehicle Manager")
st.sidebar.markdown("Manage resident vehicles in your society below.")

# Show current residents
residents = get_all_residents()
if residents:
    st.sidebar.markdown("### 📋 Current Residents")
    for r in residents:
        st.sidebar.markdown(f"• **{r[0]}** — {r[1]} (Flat {r[2]})")
else:
    st.sidebar.info("No residents added yet.")

# Add new resident
with st.sidebar.expander("➕ Add New Vehicle", expanded=False):
    with st.form("add_resident"):
        number = st.text_input("Vehicle Number").upper()
        name = st.text_input("Owner Name")
        flat = st.text_input("Flat Number")
        add_button = st.form_submit_button("✅ Add Vehicle")
        if add_button and number:
            add_resident(number, name, flat)
            st.success(f"✅ Vehicle {number} Added")

# Delete resident
with st.sidebar.expander("🗑️ Remove Vehicle", expanded=False):
    if residents:
        numbers = [r[0] for r in residents]
        to_delete = st.selectbox("Select Vehicle to Remove", numbers)
        if st.button("❌ Delete Vehicle"):
            delete_resident(to_delete)
            st.success(f"❌ Vehicle {to_delete} Deleted")
    else:
        st.info("No residents to delete.")

# ============================ MAIN PAGE ============================

st.markdown("# 🚘 Smart Gate OCR Monitoring System")
st.markdown("AI-powered number plate recognition and visitor logging system for gated communities.")

st.divider()

col1, col2 = st.columns([2, 1])

# LEFT: Camera + Log Button
with col1:
    st.subheader("📷 Live Vehicle Detection")
    st.markdown("Press the button below to start/stop the camera. Outsiders will be logged automatically.")
    if st.button("🚦 Start / Stop Camera – View Outsider Log After Stop"):
        st.info("🔴 Camera started... Press ESC in the live feed window to stop.")
        process_camera()

# RIGHT: Resident Summary
with col2:
    st.subheader("👥 Total Registered Residents")
    st.metric(label="Registered Vehicles", value=len(residents))

st.divider()

# Outsider Logs
st.subheader("🕵️ Outsider Visitor Log")
conn = sqlite3.connect('database.db')
df = pd.read_sql_query("SELECT * FROM outsiders", conn)
conn.close()

if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.warning("No outsider vehicle data logged yet.")

st.markdown("---")
st.markdown("🔒 Developed with ❤️ by **Jaiveer Singh**")
