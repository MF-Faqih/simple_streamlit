import streamlit as st
from streamlit_gsheets import GSheetsConnection

# ydata profiling
import pandas as pd
from ydata_profiling import ProfileReport

# report untuk streamlit
from streamlit_pandas_profiling import st_profile_report


# ---------------- CONFIGURATION ----------------
st.set_page_config(
    page_title="Data Profiler Dasboard",
    page_icon="🤴",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------- JUDUL DASHBOARD ----------------
st.markdown("<h1 style='text-align: center;'> Data Profiler App </h1>",
         unsafe_allow_html = True)
st.markdown("---")


# ---------------- SIDE BAR ----------------
with st.sidebar:
    st.subheader("Promotion Data") 
    st.markdown("---")

# ---------------- BUTTON ----------------
# ini adalah cara untuk memasukkan button kedalam sidebar
if st.sidebar.button("Start Profiling Data"): 
    
    ## Read data
    
    conn = st.connection("gsheet", type=GSheetsConnection)
    
    df = conn.read(
        spreadsheet = st.secrets.gsheet_promotion["spreadsheet"],
        worksheet = st.secrets.gsheet_promotion["worksheet"]
    )
    
    # Generate report dari ydata_profiling
    pr = ProfileReport(df)
    
    st_profile_report(pr)

# Condition when user not press the button yet
else:
    st.info("Click button in te left side bar to generate data reoprt")



