import os
import shutil
# import requests
import zipfile
import subprocess
import winreg

user_path = os.path.expanduser("~")
new_folder = os.path.join(user_path, "Database Viewer Team 3")
os.makedirs(new_folder, exist_ok=True)
print(f"Created folder: {new_folder}") 

cwd = os.getcwd()

# unzip WW1-Project-Startup.zip
zip_file = os.path.join(cwd, "WW1-Project-Startup.zip")
with zipfile.ZipFile(zip_file, "r") as zip_ref:
    zip_ref.extractall(new_folder)
    # remove base folder
    base_folder = os.path.join(new_folder, "WW1-Project-Startup")
    shutil.move(base_folder, new_folder)

os.remove(zip_file)
files = os.listdir(new_folder)
for file in files:
    if file != "Implementation":
        shutil.rmtree(os.path.join(new_folder, file), ignore_errors=True)

print("Moved files to new folder")

shutil.move(os.path.join(new_folder, "Implementation"), new_folder)

shutil.move("startup.pyw", new_folder)

print("Moved startup.pyw to new folder")

with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders") as key:
    desktop_dir, _ = winreg.QueryValueEx(key, "Desktop")
    desktop_dir = os.path.expandvars(desktop_dir)

with open(os.path.join(desktop_dir, "Start Database Viewer.bat"), "w") as f:
    f.write(f'@echo off\nstart python "{os.path.join(new_folder, "startup.pyw")}"')
    
print("Created Start Database Viewer.bat on desktop")

# subprocess.Popen(["python", os.path.join(new_folder, "startup.py")])