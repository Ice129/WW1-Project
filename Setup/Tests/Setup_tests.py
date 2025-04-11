import pytest
import os
import sys
import time
import psutil
import subprocess
import shutil
import zipfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import setup


def test_create_new_folder():
    test_folder_name = "TestFolder"
    test_folder_path = setup.create_new_folder(test_folder_name)
    assert os.path.exists(
        test_folder_path
    ), f"Folder {test_folder_name} was not created successfully."
    assert os.path.isdir(test_folder_path), f"{test_folder_name} is not a directory."
    has_content = len(os.listdir(test_folder_path)) == 0
    assert has_content, "The folder should be empty after creation."
    shutil.rmtree(test_folder_path, ignore_errors=True)


def test_find_and_extract_zip():
    test_zip_name = "test.zip"
    test_zip_path = os.path.join(os.getcwd(), test_zip_name)
    with zipfile.ZipFile(test_zip_path, "w") as zipf:
        zipf.writestr("test.txt", "This is a test file.")
        zipf.writestr("test_folder/test.txt", "This is a test file in a folder.")
    # make a list comprehensiobn to prepend cwd to the files and folders
    unpacked_folders_and_files = [
        os.path.join(os.getcwd(), path)
        for path in ["test.txt", "test_folder", os.path.join("test_folder", "test.txt")]
    ]

    try:
        extracted_zip, extracted_folder = setup.find_and_extract_zip(
            os.getcwd(), "test"
        )
        assert (
            extracted_folder == os.path.splitext(os.path.basename(test_zip_name))[0]
        ), f"Expected {os.path.splitext(os.path.basename(test_zip_name))[0]}, got {extracted_folder}"
        assert (
            extracted_zip == test_zip_path
        ), f"Expected {test_zip_path}, got {extracted_zip}"
    except FileNotFoundError:
        pytest.fail("Zip file not found.")

    for item in unpacked_folders_and_files:
        if os.path.isdir(item):
            assert os.path.isdir(item), f"{item} is not a directory."
        elif os.path.isfile(item):
            assert os.path.isfile(item), f"{item} is not a file."
            # check if the file is empty
            assert os.path.getsize(item) > 0, f"{item} is empty."
        else:
            pytest.fail(f"{item} is neither a file nor a directory.")

    for item in unpacked_folders_and_files:
        if os.path.isdir(item):
            shutil.rmtree(item, ignore_errors=True)
        elif os.path.isfile(item):
            os.remove(item)
    os.remove(test_zip_path)

def delete_files_implementation(zip_path,target_folder):
    if os.path.exists(zip_path):
        os.remove(zip_path)
    if os.path.exists(target_folder):
        shutil.rmtree(target_folder, ignore_errors=True)
    if os.path.exists(os.path.join(os.getcwd(), "base")):
        shutil.rmtree(os.path.join(os.getcwd(), "base"), ignore_errors=True)
        

def test_copy_implementation_files():
    test_zip_name = "test.zip"
    test_zip_path = os.path.join(os.getcwd(), test_zip_name)
    target_folder = setup.create_new_folder("TestCopy")
    delete_files_implementation(test_zip_path,target_folder)
    files = [
        ["base\\imp6\\test1.txt", "this is a test file."],
        ["base\\imp6\\test_folder\\test2.txt", "this is a test file in a folder."],
        ["base\\unintended\\dont_copy3.txt", "this is a test file that should not be copied."],
    ]

    with zipfile.ZipFile(test_zip_path, "w") as zipf:
        for file in files:
            zipf.writestr(file[0], file[1])

    target_folder = setup.create_new_folder("TestCopy")
    unpacked_folders_and_files = [
        os.path.join(target_folder, os.path.join(*x[0].split(os.sep)[2:])) 
        for x in files if "imp6" in x[0]
    ]
    # unpack the zip file
    extracted_zip, extracted_folder = setup.find_and_extract_zip(os.getcwd(), "test")
    
    # copy the implementation files to a new folder
    setup.copy_implementation_files(os.getcwd(), "base", target_folder, "imp6")
    # check if the files were copied correctly
    for item in unpacked_folders_and_files:
        if "dont_copy3" in os.path.basename(item):
            assert not os.path.exists(item), f"{item} should not have been copied."
        else:
            assert os.path.exists(item), f"{item} was not copied successfully."
    delete_files_implementation(extracted_zip, target_folder)

def test_cleanup_files():
    test_zip_name = "test.zip"
    test_zip_file = os.path.join(os.getcwd(), test_zip_name)
    dir_name = "test_dir"
    os.makedirs(dir_name, exist_ok=True)
    with open(test_zip_file, "w") as f:
        f.write("This is a test file.")
    setup.cleanup_files(os.getcwd(), test_zip_file, dir_name)
    assert not os.path.exists(test_zip_file), f"{test_zip_file} was not deleted."
    assert not os.path.exists(dir_name), f"{dir_name} was not deleted."

def test_get_desktop_path():
    desktop_path = setup.get_desktop_path()
    assert os.path.exists(desktop_path), f"Desktop path {desktop_path} does not exist."
    assert os.path.isdir(desktop_path), f"{desktop_path} is not a directory."
    assert os.path.basename(desktop_path) == "Desktop", f"Expected 'Desktop' as last part of path, got {os.path.basename(desktop_path)}"
    
def test_find_python_executable():
    try:
        python_path = setup.find_python_executable()
    except FileNotFoundError:
        pytest.fail("Python executable not found.")
    assert os.path.exists(python_path), f"Python executable {python_path} does not exist."
    assert python_path.endswith("python.exe"), f"Expected the path to end with 'python.exe', got {python_path}"

def test_create_shortcut_batch_file():
    desktop_path = setup.get_desktop_path()
    target_folder = os.path.join(os.getcwd(), "TestFolder")
    python_path = setup.find_python_executable()
    setup.create_shortcut_batch_file(desktop_path, target_folder, python_path)
    batch_file_path = os.path.join(desktop_path, "Start Database Viewer.bat")
    assert os.path.exists(batch_file_path), f"Batch file {batch_file_path} was not created."
    with open(batch_file_path, "r") as f:
        batch_content = f.read()
    assert "TestFolder" in batch_content, f"Batch file content does not match expected content."
    assert python_path in batch_content, f"Batch file content does not match expected content."
    os.remove(batch_file_path)
    

test_create_new_folder()
test_find_and_extract_zip()
test_copy_implementation_files()
test_cleanup_files()
test_get_desktop_path()
test_find_python_executable()
test_create_shortcut_batch_file()
