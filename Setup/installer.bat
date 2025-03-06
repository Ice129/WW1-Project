@echo off
rem https://docs.python.org/3.12/using/windows.html#installing-without-ui

python-3.12.9-amd64.exe /passive

@REM timeout for 2 seconds to avoid system error
timeout 2

REM Check for Python 3.12 installation in common locations
set PYTHON_SYS_PATH=C:\Program Files\Python312\python.exe
set PYTHON_USER_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe

REM Initialize python_path variable
set "python_path="

REM Check if Python exists in user installation
IF EXIST "%PYTHON_USER_PATH%" (
    set "python_path=%PYTHON_USER_PATH%"
    goto :FOUND_PYTHON
)

REM Check if Python exists in system-wide installation
IF EXIST "%PYTHON_SYS_PATH%" (
    set "python_path=%PYTHON_SYS_PATH%"
    goto :FOUND_PYTHON
)

REM Python not found in default locations
echo Python 3.12 not found in default locations
echo Checked paths:
echo - %PYTHON_SYS_PATH%
echo - %PYTHON_USER_PATH%
exit /b 1 rem Error code 1 for Python not found

:FOUND_PYTHON
echo Found Python at: %python_path%

REM Use the found Python path instead of py command
"%python_path%" -m pip install --upgrade pip
"%python_path%" -m pip install -r requirements.txt

"%python_path%" setup.py

rem clear screen then say instilation is done
cls
echo Installation is done
echo you can close this screen and run the program from the shortcut on your desktop
pause