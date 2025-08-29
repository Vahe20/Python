import re
import time
import threading
from plyer import notification

class Timer:
    def __init__(self, name, seconds, message=None):
        self.name = name
        self.seconds = seconds
        self.message = message if message else f"Таймер '{name}' завершен!"

    def start(self):
        thread = threading.Thread(target=self.run_timer)
        thread.start()

    def run_timer(self):
        remaining = self.seconds
        while remaining > 0:
            mins, secs = divmod(remaining, 60)
            print(f"[{self.name}] {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            remaining -= 1
        print(f"\n{self.message}")
        notification.notify(
            title = "Jarvis",
            message = self.message,
            app_name = "Jarvis",
            timeout = 10
        )