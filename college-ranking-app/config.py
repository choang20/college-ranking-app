import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key securely
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.data.gov/ed/collegescorecard/v1/schools"
