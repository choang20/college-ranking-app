import unittest
from utils.api_fetch import fetch_college_data

class TestAPIFetch(unittest.TestCase):
    def test_fetch_college_data(self):
        df = fetch_college_data()
        self.assertFalse(df.empty, "Dataframe should not be empty")

if __name__ == "__main__":
    unittest.main()
