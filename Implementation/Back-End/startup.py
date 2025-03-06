import time
import subprocess
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Use absolute paths for all script calls
backend_path = os.path.join(script_dir, "backend.py")
api_path = os.path.join(script_dir, "api.py")
kiosk_keeper_path = os.path.join(script_dir, "kiosk_keeper.pyw")
# Define the path to Python 3.12 for the subprocess calls
python_command = ["py", "-3.12"]

try:
    subprocess.run(python_command + [backend_path])
except Exception as e:
    print(e)
    input("an error occurred in the backend, press enter to continue")

time.sleep(1)

try:
    subprocess.Popen(python_command + [api_path])
except Exception as e:
    print(e)
    input("an error occurred in the api, press enter to continue")

try:
    subprocess.run(["taskkill", "/f", "/im", "msedge.exe"])
except Exception as e:
    print(f"Note: Could not kill Edge: {e}")

# wait for all processes to close
time.sleep(0.3)

# check if edge is still running, if not, restart it
pid = subprocess.Popen(python_command + [kiosk_keeper_path]).pid
with open(os.path.join(script_dir, "PID"), "w") as f:
    f.write(str(pid))

# input("Press enter to close the startup script")
