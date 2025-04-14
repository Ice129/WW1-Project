import os
import shutil
import zipfile
import winreg


def create_new_folder(folder_name):
    """Create a new folder in user's home directory for project files."""
    user_path = os.path.expanduser("~")
    new_folder = os.path.join(user_path, folder_name)
    shutil.rmtree(new_folder, ignore_errors=True)
    os.makedirs(new_folder, exist_ok=True)
    return new_folder

def find_and_extract_zip(current_dir, zip_prefix):
    """Find and extract zip file with specified prefix."""
    zip_file = None
    for file in os.listdir(current_dir):
        if file.startswith(zip_prefix) and file.endswith(".zip"):
            zip_file = os.path.join(current_dir, file)
            zip_name = file[:-4]
            break
    
    if zip_file is None:
        raise FileNotFoundError(f"Could not find {zip_prefix}*.zip in {current_dir}")

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(current_dir)
    
    print(f"Extracted {zip_file} to {current_dir}")
    print(f"Extracted to {os.path.join(current_dir, zip_name)}")
    print(f"Extracted to {os.path.join(current_dir, zip_name, 'Implementation')}")
    
    return zip_file, zip_name


def copy_implementation_files(current_dir, zip_name, target_folder, wanted_folder="Implementation"):
    """Copy implementation files to the target folder."""
    implementation_dir = os.path.join(current_dir, zip_name, wanted_folder)
    if not os.path.exists(implementation_dir):
        implementation_dir = os.path.join(current_dir, "Implementation")
    if os.path.exists(implementation_dir):
        print(f"Copying files from {implementation_dir} to {target_folder}")
        for item in os.listdir(implementation_dir):
            src = os.path.join(implementation_dir, item)
            dst = os.path.join(target_folder, item)
            print(f"Copying {src} to {dst}")
            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)
    else:
        raise FileNotFoundError(f"Could not find {wanted_folder} in {os.path.join(current_dir, zip_name)}")
    return implementation_dir


def cleanup_files(current_dir, zip_file, zip_name):
    """Clean up extracted files."""
    os.remove(zip_file)
    shutil.rmtree(os.path.join(current_dir, zip_name), ignore_errors=True)
    print(f"Removed {zip_file} and {os.path.join(current_dir, zip_name)}")


def get_desktop_path():
    """Get the user's desktop path."""
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
    ) as key:
        desktop_dir, _ = winreg.QueryValueEx(key, "Desktop")
        desktop_dir = os.path.expandvars(desktop_dir)
    return desktop_dir


def find_python_executable():
    """Find the Python executable path."""
    username = os.getenv("USERNAME")
    possible_paths = [
        r"C:\Program Files\Python312\python.exe",  # System-wide installation
        rf"C:\Users\{username}\AppData\Local\Programs\Python\Python312\python.exe",  # User installation
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    raise FileNotFoundError("Python 3.12 not found in default locations")

def create_shortcut_batch_file(desktop_dir, target_folder, python_path):
    """Create a batch file shortcut on the desktop."""
    with open(os.path.join(desktop_dir, "Start Database Viewer.bat"), "w") as f:
        batch_content = rf"""@echo off
cd /d "{os.path.join(target_folder, "Back-End")}"
start "" "{python_path}" startup.pyw
"""
        f.write(batch_content)



def main():
    folder_name = "Database Viewer Team 3"
    zip_prefix = "WW1-Project"
    current_dir = os.getcwd()
    
    # Create folder and extract zip
    target_folder = create_new_folder(folder_name)
    zip_file, zip_name = find_and_extract_zip(current_dir, zip_prefix)
    
    # Copy files and clean up
    implementation_dir = copy_implementation_files(current_dir, zip_name, target_folder)
    cleanup_files(current_dir, zip_file, implementation_dir)
    
    # Create desktop shortcut
    desktop_dir = get_desktop_path()
    python_path = find_python_executable()
    create_shortcut_batch_file(desktop_dir, target_folder, python_path)

main()