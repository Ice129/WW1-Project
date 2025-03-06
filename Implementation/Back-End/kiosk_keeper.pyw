import os
import subprocess
import time

while True:
    time.sleep(0.3)
    if not "msedge.exe" in os.popen("tasklist").read():
        subprocess.Popen(
            [
                "start",
                "msedge",
                "--kiosk",
                "http://localhost:8000",
                "--edge-kiosk-type=fullscreen",
                "-no-first-run",
            ],
            shell=True,
        )
        continue
