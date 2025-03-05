import os
import subprocess
import time

while True:
    time.sleep(0.5)
    if not "msedge.exe" in os.popen("tasklist").read():
        # Option 1: Using a raw string path with direct execution
        subprocess.Popen(["start"
            r"msedge",
                  "--kiosk", "http://localhost/", 
                  "--edge-kiosk-type=fullscreen", 
                  "-no-first-run"])
        continue
    # TODO: if needed, update the url to the correct one used by api.py