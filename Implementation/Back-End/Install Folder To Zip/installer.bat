@echo off
rem https://docs.python.org/3.12/using/windows.html#installing-without-ui

python-3.12.9-amd64.exe /passive

timeout 2

py -3.12 -m pip install --upgrade pip
py -3.12 -m pip install -r requirements.txt