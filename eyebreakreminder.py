'''
10/12/26
pip install winotify
'''

import time
from pathlib import Path

from winotify import Notification, audio

APP_ID = "Eye Break Reminder"
TITLE = "Lookey Lookey Away"
MESSAGE = "Do something else you baka!"
INTERVAL_MINUTES = 20
INTERVAL_SECONDS = INTERVAL_MINUTES * 60
IMAGE_PATH = Path(__file__).resolve().parent / "goat.png"


def send_reminder() -> None:
    image = str(IMAGE_PATH) if IMAGE_PATH.is_file() else None

    toast = Notification(
        app_id=APP_ID,
        title=TITLE,
        msg=MESSAGE,
        duration="short",
        icon=image or "",
    )

    toast.set_audio(audio.Default, loop=False)
    toast.show()


def main() -> None:
    print(f"Running every {INTERVAL_MINUTES} minutes!!!")
    print("Oi...")
    print("Ctrl + C to stop...")

    try:
        while True:
            time.sleep(INTERVAL_SECONDS)
            send_reminder()
    except KeyboardInterrupt:
        print("\nCome back baka...\n")


if __name__ == "__main__":
    main()
