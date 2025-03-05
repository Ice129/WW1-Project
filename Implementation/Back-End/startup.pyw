import time
import subprocess
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Use absolute paths for all script calls
backend_path = os.path.join(script_dir, "backend.py")
api_path = os.path.join(script_dir, "api.py")
kiosk_keeper_path = os.path.join(script_dir, "kiosk_keeper.pyw")

try:
    subprocess.run(["python", backend_path])
except Exception as e:
    print(e)
    input("an error occurred in the backend, press enter to continue")
time.sleep(1)
subprocess.Popen(["pythonw", api_path])

#kill all running edge instances
subprocess.run(["taskkill", "/f", "/im", "msedge.exe"])

#wait for all processes to close
time.sleep(0.3)

# check if edge is still running, if not, restart it
pid = subprocess.Popen(["pythonw", kiosk_keeper_path]).pid
with open(os.path.join(script_dir, "PID"), "w") as f:
    f.write(str(pid))