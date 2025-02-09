import unittest
import pandas as pd
from utils.scoring import normalize_and_score

class TestScoring(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "latest.admissions.admission_rate.overall": [0.5, 0.7, 0.9],
            "latest.cost.tuition.in_state": [20000, 30000, 40000],
            "latest.earnings.10_yrs_after_entry.median": [50000, 60000, 70000]
        })
        self.weights = {
            "Admission Rate": 0.2,
            "Tuition Cost (In-State)": -0.3,
            "Earnings After Graduation": 0.4
        }

    def test_normalize_and_score(self):
        scored_df = normalize_and_score(self.df, self.weights)
        self.assertIn("score", scored_df.columns, "Score column should be present")

if __name__ == "__main__":
    unittest.main()
