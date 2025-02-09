from sklearn.preprocessing import MinMaxScaler

def normalize_and_score(df, weights):
    columns_to_normalize = [
        "latest.admissions.admission_rate.overall",
        "latest.cost.tuition.in_state",
        "latest.earnings.10_yrs_after_entry.median"
    ]

    df.fillna(0, inplace=True)
    scaler = MinMaxScaler()
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

    df["score"] = (
        df["latest.admissions.admission_rate.overall"] * weights["Admission Rate"] +
        df["latest.cost.tuition.in_state"] * weights["Tuition Cost (In-State)"] +
        df["latest.earnings.10_yrs_after_entry.median"] * weights["Earnings After Graduation"]
    )

    return df.sort_values(by="score", ascending=False)
