import pytest
import os
import sys
import time
import psutil
import requests
import subprocess

# add the directory containing the currrent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import startup

# Fixtures for common resources
@pytest.fixture
def script_dir():
    return startup.get_script_dir()

@pytest.fixture
def python_command():
    return [startup.find_python_path()]

@pytest.fixture
def current_pid():
    return os.getpid()

# Helper functions to reduce code duplication
def cleanup_processes(current_pid):
    """Kill all python processes except the current one"""
    killed = False
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'python.exe' and proc.info['pid'] != current_pid:
            proc.kill()
            print(f"Killed process: {proc.info['pid']}")
            killed = True
    return killed

def verify_server_running():
    """Verify the API server is running by making a request"""
    try:
        response = requests.get("http://localhost:8000/")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the web server: {e}")
        return False

# Test the get_script_dir function
def test_get_script_dir(script_dir):
    assert os.path.isdir(script_dir), f"Expected {script_dir} to be a directory"
    assert os.path.basename(script_dir) == "Back-End", f"Expected the last part of the path to be 'Back-End', got {os.path.basename(script_dir)}"

def test_find_python_path(python_command):
    python_path = python_command[0]
    assert os.path.exists(python_path), f"Expected {python_path} to exist"
    assert python_path.endswith("python.exe"), f"Expected the path to end with 'python.exe', got {python_path}"

def test_run_backend(script_dir, python_command):
    backend_path = os.path.join(script_dir, "backend.pyw")

    # delete firstrun.flag if exists
    firstrun_flag_path = os.path.join(script_dir, "firstrun.flag")
    print(f"Deleting firstrun.flag at {firstrun_flag_path}")
    if os.path.exists(firstrun_flag_path):
        os.remove(firstrun_flag_path)

    try:
        assert startup.run_backend(python_command, backend_path) == True, "Backend did not run successfully"
        time.sleep(5)  # Wait for the backend to finish processing
        assert os.path.exists(firstrun_flag_path), "firstrun.flag was not created"
    finally:
        # Clean up the firstrun.flag file after the test
        if os.path.exists(firstrun_flag_path):
            os.remove(firstrun_flag_path)

def test_start_api_server(script_dir, python_command, current_pid):
    api_path = os.path.join(script_dir, "api.pyw")
    
    try:
        # Start the API server
        assert startup.start_api_server(python_command, api_path) == True, "API server did not start successfully"
        time.sleep(2)  # give the server time to start
        
        assert verify_server_running(), "Web server is not running"
    finally:
        # Cleanup
        killed = cleanup_processes(current_pid)
        assert killed, "No python processes were killed"

def test_kill_edge_browser():
    # Start Edge browser for testing
    subprocess.Popen(["start", "msedge"], shell=True)
    time.sleep(2)  # Give it some time to start
    
    success, output = startup.kill_edge_browser()
    assert success, "Failed to kill Edge browser"
    assert "SUCCESS: The process \"msedge.exe\" with PID" in output, f"Unexpected output: {output}"
    
    # Check if Edge is still running    
    edge_running = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'msedge.exe':
            edge_running = True
            break
    assert not edge_running, "Edge browser is still running after kill command"

def test_start_kiosk_keeper(script_dir, python_command):
    kiosk_keeper_path = os.path.join(script_dir, "kiosk_keeper.pyw")
    pid_file_path = os.path.join(script_dir, "PID_TEST")  # Use a test PID file to avoid conflicts
    
    try:
        # Start kiosk keeper
        pid = startup.start_kiosk_keeper(python_command, kiosk_keeper_path, pid_file_path)
        
        # Verify PID was returned
        assert pid is not None, "No PID returned when starting kiosk keeper"
        
        # Verify PID file was created with the correct PID
        assert os.path.exists(pid_file_path), "PID file was not created"
        with open(pid_file_path, "r") as f:
            saved_pid = int(f.read().strip())
        assert saved_pid == pid, f"Expected PID {pid}, got {saved_pid} in the PID file"
        
        # Verify the process is running
        process_running = False
        for proc in psutil.process_iter(['pid']):
            if proc.info['pid'] == pid:
                process_running = True
                proc.kill()  # Kill the process before exiting the test
                break
        assert process_running, "Kiosk keeper process is not running"
    finally:
        # Clean up the test PID file
        if os.path.exists(pid_file_path):
            os.remove(pid_file_path)

def test_main(script_dir, current_pid):
    pid_file_path = os.path.join(script_dir, "PID")
    
    try:
        # Run the main function
        result = startup.main()
        assert result == True, "Main function did not execute successfully"
        
        # Verify the PID file was created
        assert os.path.exists(pid_file_path), "PID file was not created by main function"
        
        # Verify the server is running
        time.sleep(2)  # Give the server time to start
        assert verify_server_running(), "Web server is not running after main function"
    except Exception as e:
        print(f"An error occurred: {e}")
        pytest.fail(f"Main function failed: {e}")
    cleanup_processes(current_pid)
    startup.kill_edge_browser()

# Manually call the tests with appropriate fixtures
def run_tests():
    script_dir = startup.get_script_dir()
    python_command = [startup.find_python_path()]
    current_pid = os.getpid()
    
    test_get_script_dir(script_dir)
    test_find_python_path(python_command)
    test_run_backend(script_dir, python_command)
    test_start_api_server(script_dir, python_command, current_pid)
    test_kill_edge_browser()
    test_start_kiosk_keeper(script_dir, python_command)
    test_main(script_dir, current_pid)

if __name__ == "__main__":
    run_tests()
