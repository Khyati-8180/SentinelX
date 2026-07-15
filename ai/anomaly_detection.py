from sklearn.ensemble import IsolationForest


def detect_anomalies(df):

    features = df[
        [
            "Failed_Logins",
            "Files_Accessed",
            "USB_Events",
            "Login_Hour"
        ]
    ]

    model = IsolationForest(
        contamination=0.25,
        random_state=42
    )

    prediction = model.fit_predict(features)

    df["Prediction"] = prediction

    df["Risk"] = prediction

    df["Risk"] = df["Risk"].replace({
        -1: "High",
        1: "Low"
    })

    return df