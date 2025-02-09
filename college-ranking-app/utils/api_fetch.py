import requests
import pandas as pd
from config import API_KEY, BASE_URL

def fetch_college_data():
    params = {
        "api_key": API_KEY,
        "fields": "school.name,school.city,school.state,"
                  "latest.admissions.admission_rate.overall,"
                  "latest.cost.tuition.in_state,"
                  "latest.earnings.10_yrs_after_entry.median",
        "per_page": 50
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return pd.DataFrame(data["results"])

if __name__ == "__main__":
    df = fetch_college_data()
    df.to_csv("data/preprocessed_college_data.csv", index=False)
