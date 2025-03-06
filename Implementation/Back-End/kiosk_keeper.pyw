import os
import subprocess
import time

while True:
    time.sleep(0.3)
    if not "msedge.exe" in os.popen("tasklist").read():
        # Option 1: Using a raw string path with direct execution
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
    # TODO: if needed, update the url to the correct one used by api.py
