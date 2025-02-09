import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key securely
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.data.gov/ed/collegescorecard/v1/schools"

# Define test parameters
params = {
    "api_key": API_KEY,
    "fields": "school.name,school.city,school.state,"
              "latest.admissions.admission_rate.overall,"
              "latest.cost.tuition.in_state,"
              "latest.earnings.10_yrs_after_entry.median",
    "per_page": 5  # Fetch a few results for testing
}

# Make API request
response = requests.get(BASE_URL, params=params)

# Print results
if response.status_code == 200:
    data = response.json()
    print("✅ API Call Successful!")
    print("First College:", data["results"][0])  # Print first result
else:
    print("❌ API Call Failed!")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
