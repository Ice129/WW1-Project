@echo off
rem https://docs.python.org/3.12/using/windows.html#installing-without-ui

python-3.12.9-amd64.exe /passive

@REM timeout for 2 seconds to avoid system error
timeout 2

py -3.12 -m pip install --upgrade pip
py -3.12 -m pip install -r requirements.txt

py setup.py
pause