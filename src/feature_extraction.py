import pandas as pd
import numpy as np

df = pd.read_csv("data/raw_keystrokes.csv")

SESSION_SIZE = 50
PAUSE_THRESHOLD = 0.5

features = []

for i in range(0, len(df), SESSION_SIZE):
    session = df.iloc[i:i + SESSION_SIZE]

    if len(session) < SESSION_SIZE:
        continue

    hold_times = session["hold_time"]
    delays = session["inter_key_delay"].dropna()

    pauses = delays[delays > PAUSE_THRESHOLD]

    features.append({
        "mean_hold_time": hold_times.mean(),
        "std_hold_time": hold_times.std(),
        "mean_inter_key_delay": delays.mean(),
        "std_inter_key_delay": delays.std(),
        "pause_count": len(pauses),
        "avg_pause_duration": pauses.mean() if len(pauses) > 0 else 0,
        "typing_speed": SESSION_SIZE / (session["release_time"].iloc[-1] - session["press_time"].iloc[0])
    })

features_df = pd.DataFrame(features)
features_df.to_csv("data/session_features.csv", index=False)

print("Session-level feature dataset created.")
