import os
import subprocess
import time

while True:
    time.sleep(0.3)
    user_directory = os.path.expanduser("")
    user_directory = user_directory + "/Data Viewer Team 3"
    if not "msedge.exe" in os.popen("tasklist").read():
        subprocess.Popen(
            [
                "start",
                "msedge",
                "--kiosk",
                f"{user_directory}/Front-End/index.html",
                "--edge-kiosk-type=fullscreen",
                "-no-first-run",
            ],
            shell=True,
        )
        continue
