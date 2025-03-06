import os
import subprocess
import time

user_path = os.path.expanduser("~")

while True:
    time.sleep(0.3)
    if not "msedge.exe" in os.popen("tasklist").read():
        subprocess.Popen(
            [
                "start",
                "msedge",
                "--kiosk",
                f"{user_path}/Database Viewer Team 3/Front-End/index.html",
                "--edge-kiosk-type=fullscreen",
                "-no-first-run",
            ],
            shell=True,
        )
        continue
