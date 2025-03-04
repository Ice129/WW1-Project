import os
import subprocess
import time

while True:
    time.sleep(0.5)
    if not "msedge.exe" in os.popen("tasklist").read():
        subprocess.Popen(["start", "", "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", 
                  "--kiosk", "http://localhost/", 
                  "--edge-kiosk-type=fullscreen", 
                  "-no-first-run"])
        continue
    break