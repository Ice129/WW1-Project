import time
import os
import subprocess

print("Starting Database Viewer Team 3")

subprocess.run(["python", "backend.py"])
time.sleep(1)
subprocess.Popen(["pythonw", "api.py"])



### python:

#kill all running edge instances
subprocess.run(["taskkill", "/f", "/im", "msedge.exe"])

#wait for all processes to close
time.sleep(0.3)

# check if edge is still running, if not, restart it
pid = subprocess.Popen(["pythonw", "kiosk_keeper.pyw"]).pid
with open("PID", "w") as f:
    f.write(str(pid))