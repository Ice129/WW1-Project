import os
import shutil
import zipfile
import winreg

# create new folder in user's home directory for project files
user_path = os.path.expanduser("~")
new_folder = os.path.join(user_path, "Database Viewer Team 3")
shutil.rmtree(new_folder, ignore_errors=True)
os.makedirs(new_folder, exist_ok=True)

# Unzip WW1-Project-Startup.zip to current directory
cwd = os.getcwd()
zip_file = None
for file in os.listdir(cwd):
    if file.startswith("WW1-Project") and file.endswith(".zip"):
        zip_file = os.path.join(cwd, file)
        zip_name = file[:-4]
        break
if zip_file is None:
    raise FileNotFoundError(f"Could not find WW1-Project*.zip in {cwd}")

with zipfile.ZipFile(zip_file, "r") as zip_ref:
    zip_ref.extractall(cwd)

# Move contents of the Implementation folder to the new folder in user's home directory
implementation_dir = os.path.join(cwd, zip_name, "Implementation")
if os.path.exists(implementation_dir):
    for item in os.listdir(implementation_dir):
        src = os.path.join(implementation_dir, item)
        dst = os.path.join(new_folder, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)


# Clean up zip file and extracted folder
os.remove(zip_file)
shutil.rmtree(os.path.join(cwd, zip_name), ignore_errors=True)

# Create Start Database Viewer.bat on desktop
with winreg.OpenKey(
    winreg.HKEY_CURRENT_USER,
    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
) as key:
    desktop_dir, _ = winreg.QueryValueEx(key, "Desktop")
    desktop_dir = os.path.expandvars(desktop_dir)

username = os.getenv("USERNAME")
possible_paths = [
    r"C:\Program Files\Python312\python.exe",  # System-wide installation
    rf"C:\Users\{username}\AppData\Local\Programs\Python\Python312\python.exe",  # User installation
]

# Try to find Python in the default locations
python_path = None
for path in possible_paths:
    if os.path.exists(path):
        python_path = path
        break

if python_path is None:
    raise FileNotFoundError("Python 3.12 not found in default locations")

with open(os.path.join(desktop_dir, "Start Database Viewer.bat"), "w") as f:
    batch_content = rf"""@echo off
cd /d "{os.path.join(new_folder, "Back-End")}"
start "" "{python_path}" startup.py
"""
    f.write(batch_content)
    # TODO: update file extentions to pyw
