import sys
import os

# Add the parent directory to sys.path so Python can find the utils module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.scoring import normalize_and_score
import pandas as pd

class TestScoring:
    def test_normalize_and_score(self):
        df = pd.DataFrame({
            "latest.admissions.admission_rate.overall": [0.5, 0.7, 0.9],
            "latest.cost.tuition.in_state": [20000, 30000, 40000],
            "latest.earnings.10_yrs_after_entry.median": [50000, 60000, 70000]
        })

        weights = {
            "Admission Rate": 0.2,
            "Tuition Cost (In-State)": -0.3,
            "Earnings After Graduation": 0.4
        }

        scored_df = normalize_and_score(df, weights)

        assert "score" in scored_df.columns, "❌ Score column missing!"
        print("✅ Test Passed! Scoring function is working.")

if __name__ == "__main__":
    test = TestScoring()
    test.test_normalize_and_score()
