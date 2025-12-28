import time
import joblib
import numpy as np
from pynput import keyboard
import pandas as pd


# Load trained model and encoder
model = joblib.load("model/cognitive_load_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

press_times = {}
records = []
last_release_time = None

SESSION_DURATION = 30  # seconds
PAUSE_THRESHOLD = 0.5


def on_press(key):
    global last_release_time
    press_time = time.time()

    if last_release_time is not None:
        inter_key_delay = press_time - last_release_time
    else:
        inter_key_delay = None

    press_times[key] = (press_time, inter_key_delay)


def on_release(key):
    global last_release_time
    release_time = time.time()

    if key in press_times:
        press_time, inter_key_delay = press_times[key]
        hold_time = release_time - press_time

        records.append((hold_time, inter_key_delay))

    last_release_time = release_time


def extract_features(records):
    holds = [r[0] for r in records]
    delays = [r[1] for r in records if r[1] is not None]

    pauses = [d for d in delays if d > PAUSE_THRESHOLD]

    features = [
        np.mean(holds),
        np.std(holds),
        np.mean(delays),
        np.std(delays),
        len(pauses),
        np.mean(pauses) if pauses else 0,
        len(records) / SESSION_DURATION
    ]

    feature_names = [
        "mean_hold_time",
        "std_hold_time",
        "mean_inter_key_delay",
        "std_inter_key_delay",
        "pause_count",
        "avg_pause_duration",
        "typing_speed"
    ]

    return pd.DataFrame([features], columns=feature_names)



if __name__ == "__main__":
    print("Start typing... (30 seconds)")

    start_time = time.time()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while time.time() - start_time < SESSION_DURATION:
            time.sleep(0.1)
        listener.stop()

    X = extract_features(records)

    prediction = model.predict(X)[0]
    probs = model.predict_proba(X)[0]

    label = label_encoder.inverse_transform([prediction])[0]
    confidence = max(probs)

    print("\nReal-time Prediction:")
    print(f"Cognitive Load: {label.upper()}")
    print(f"Confidence: {confidence:.2f}")
