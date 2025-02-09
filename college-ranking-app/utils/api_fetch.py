import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.data.gov/ed/collegescorecard/v1/schools"

def fetch_college_data():
    params = {
        "api_key": API_KEY,
        "fields": "school.name,school.city,school.state,"
                  "latest.admissions.admission_rate.overall,"
                  "latest.cost.tuition.in_state,"
                  "latest.earnings.10_yrs_after_entry.median",
        "per_page": 5
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("❌ API Call Failed! Status:", response.status_code)
        print("Response:", response.text)
        return pd.DataFrame()

    data = response.json()

    # Print API response keys to check structure
    print("🔍 API Response Keys:", data.keys())

    if "results" not in data:
        print("❌ 'results' key missing in API response!")
        return pd.DataFrame()

    df = pd.DataFrame(data["results"])

    # Print first row to confirm structure
    print("✅ First Row in Streamlit Cloud:", df.iloc[0].to_dict())

    return df
