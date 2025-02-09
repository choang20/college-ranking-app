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

# Fetch data
df = fetch_college_data()

# 🔍 Debug: Print available columns before normalization
print("🔍 Available Columns in Streamlit:", df.columns.tolist())

# Check if expected columns exist
expected_columns = [
    "latest.admissions.admission_rate.overall",
    "latest.cost.tuition.in_state",
    "latest.earnings.10_yrs_after_entry.median"
]
missing_columns = [col for col in expected_columns if col not in df.columns]

if missing_columns:
    print(f"❌ Missing columns in Streamlit DataFrame: {missing_columns}")
    st.error(f"Error: Missing columns {missing_columns} in API response.")

# Proceed only if all columns exist
if all(col in df.columns for col in expected_columns):
    df = normalize_and_score(df, weights)
    st.dataframe(df[["school.name", "school.city", "school.state", "score"]])
