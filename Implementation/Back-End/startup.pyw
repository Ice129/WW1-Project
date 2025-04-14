import time
import subprocess
import os

def get_script_dir():
    """Get the directory where this script is located"""
    return os.path.dirname(os.path.abspath(__file__))

def find_python_path():
    """Find the Python 3.12 executable path"""
    username = os.getenv("USERNAME")
    possible_paths = [
        rf"C:\Users\{username}\AppData\Local\Programs\Python\Python312\python.exe",  # User installation
        r"C:\Program Files\Python312\python.exe",  # System-wide installation
    ]

    # Try to find Python in the default locations
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    raise FileNotFoundError("Python 3.12 not found in default locations")

def run_backend(python_command, backend_path):
    """Run the backend and wait for it to finish"""
    try:
        # Save current directory
        original_dir = os.getcwd()
        # Change to the directory where the script is located
        script_dir = get_script_dir()
        os.chdir(script_dir)
        
        # Run the backend
        subprocess.run(python_command + [backend_path])
        
        # Restore original directory
        os.chdir(original_dir)
        return True
    except Exception as e:
        print(e)
        input("an error occurred in the backend, press enter to continue")
        return False

def start_api_server(python_command, api_path):
    """Start the API server as a separate process"""

    original_dir = os.getcwd()
    script_dir = get_script_dir()
    os.chdir(script_dir)
    try:
        subprocess.Popen(python_command + [api_path])
        os.chdir(original_dir)
        return True
    except Exception as e:
        print(e)
        print("an error occurred in the api")
        os.chdir(original_dir)
        return False

def kill_edge_browser():
    """Kill any running Microsoft Edge processes"""
    try:
        process = subprocess.run(["taskkill", "/f", "/im", "msedge.exe"], capture_output=True, text=True)
        return True, process.stdout
    except Exception as e:
        print(f"Note: Could not kill Edge: {e}")
        return False, None

def start_kiosk_keeper(python_command, kiosk_keeper_path, pid_file_path):
    """Start the kiosk keeper and save its PID"""
    original_dir = os.getcwd()
    script_dir = get_script_dir()
    os.chdir(script_dir)
    try:
        pid = subprocess.Popen(python_command + [kiosk_keeper_path]).pid
        with open(pid_file_path, "w") as f:
            f.write(str(pid))
        os.chdir(original_dir)
        return pid
    except Exception as e:
        print(f"Error starting kiosk keeper: {e}")
        os.chdir(original_dir)
        return None

def main():
    """Main function to orchestrate the startup process"""
    # Get the directory where this script is located
    script_dir = get_script_dir()
    
    # Use absolute paths for all script calls
    backend_path = os.path.join(script_dir, "backend.pyw")
    api_path = os.path.join(script_dir, "api.pyw")
    kiosk_keeper_path = os.path.join(script_dir, "kiosk_keeper.pyw")
    pid_file_path = os.path.join(script_dir, "PID")
    
    try:
        python_path = find_python_path()
        python_command = [python_path]
        run_backend(python_command, backend_path)
        # Give backend time to finish file processing
        time.sleep(1)

        start_api_server(python_command, api_path)
        kill_edge_browser()
        # Wait for all processes to close
        time.sleep(0.3)
        start_kiosk_keeper(python_command, kiosk_keeper_path, pid_file_path)
        
        return True
    except Exception as e:
        print(f"Startup failed: {e}")
        return False

if __name__ == "__main__":
    main()
