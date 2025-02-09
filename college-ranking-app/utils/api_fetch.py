import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load API key
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

    # Check if request was successful
    if response.status_code != 200:
        print("❌ API Call Failed! Status:", response.status_code)
        print("Response:", response.text)
        return pd.DataFrame()  # Return empty DataFrame to prevent crash

    data = response.json()

    # Debugging: Print API response to check structure
    print("🔍 API Response:", data)

    # Ensure 'results' key exists before accessing it
    if "results" not in data:
        print("❌ Error: 'results' key not found in API response!")
        return pd.DataFrame()

    return pd.DataFrame(data["results"])
