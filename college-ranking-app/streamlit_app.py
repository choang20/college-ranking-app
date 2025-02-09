import streamlit as st
import pandas as pd
from utils.api_fetch import fetch_college_data
from utils.scoring import normalize_and_score

st.title("🎓 Personalized College Ranking System")

# Sidebar - User-defined weights
st.sidebar.header("Adjust Criteria Weights")
weights = {
    "Admission Rate": st.sidebar.slider("Admission Rate", -1.0, 1.0, 0.2),
    "Tuition Cost (In-State)": st.sidebar.slider("Tuition Cost", -1.0, 1.0, -0.3),
    "Earnings After Graduation": st.sidebar.slider("Earnings After Graduation", -1.0, 1.0, 0.4)
}

# Fetch and process data
df = fetch_college_data()
df = normalize_and_score(df, weights)

# Display ranked results
st.subheader("🏆 Ranked Colleges")
st.dataframe(df[["school.name", "school.city", "school.state", "score"]])
