import os
import shutil
import requests

user_path = os.path.expanduser("~")
new_folder = os.path.join(user_path, "Database Viewer Team 3")
os.makedirs(new_folder, exist_ok=True)

cwd = os.getcwd()

requests.get()