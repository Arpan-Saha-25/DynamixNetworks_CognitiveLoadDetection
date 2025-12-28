import time
import csv
from pynput import keyboard

# Dictionary to store key press times
press_times = {}

# List to store processed keystroke records
records = []

last_release_time = None


def on_press(key):
    global last_release_time

    current_press_time = time.time()

    if last_release_time is not None:
        inter_key_delay = current_press_time - last_release_time
    else:
        inter_key_delay = None

    # Store press time safely
    press_times[key] = (current_press_time, inter_key_delay)


def on_release(key):
    global last_release_time

    release_time = time.time()

    if key in press_times:
        press_time, inter_key_delay = press_times[key]
        hold_time = release_time - press_time

        records.append([
            press_time,
            release_time,
            hold_time,
            inter_key_delay
        ])

    last_release_time = release_time

    # Stop logging on ESC
    if key == keyboard.Key.esc:
        return False


def save_to_csv():
    with open("data/raw_keystrokes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "press_time",
            "release_time",
            "hold_time",
            "inter_key_delay"
        ])
        writer.writerows(records)


if __name__ == "__main__":
    print("Typing started... Press ESC to stop.")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    save_to_csv()
    print("Keystroke data saved successfully.")
