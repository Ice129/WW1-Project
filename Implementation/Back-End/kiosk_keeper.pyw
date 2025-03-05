import os
import subprocess
import time

while True:
    time.sleep(0.5)
    if not "msedge.exe" in os.popen("tasklist").read():
        # Option 1: Using a raw string path with direct execution
        subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                  "--kiosk", "http://localhost/", 
                  "--edge-kiosk-type=fullscreen", 
                  "-no-first-run"])
        continue
    # TODO: if needed, update the url to the correct one used by api.py