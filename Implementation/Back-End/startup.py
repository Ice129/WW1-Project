import time
import subprocess
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Use absolute paths for all script calls
backend_path = os.path.join(script_dir, "backend.py")
api_path = os.path.join(script_dir, "api.py")
kiosk_keeper_path = os.path.join(script_dir, "kiosk_keeper.pyw")

# Define the path to Python 3.12 executable
username = os.getenv("USERNAME")
possible_paths = [
    rf"C:\Users\{username}\AppData\Local\Programs\Python\Python312\python.exe",  # User installation
    r"C:\Program Files\Python312\python.exe",  # System-wide installation
]

# Try to find Python in the default locations
python_path = None
for path in possible_paths:
    if os.path.exists(path):
        python_path = path
        break

if python_path is None:
    raise FileNotFoundError("Python 3.12 not found in default locations")
else:
    python_command = [python_path]

try:
    # run and wait for the backend to finish
    subprocess.run(python_command + [backend_path])
except Exception as e:
    print(e)
    input("an error occurred in the backend, press enter to continue")

time.sleep(1)

try:
    # starts web server in new process
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
