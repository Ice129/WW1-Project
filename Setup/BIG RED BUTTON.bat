cmd /c Taskkill /PID "pyw.exe" /F
cmd /c Taskkill /PID "py.exe" /F
cmd /c Taskkill /PID "python.exe" /F
cmd /c Taskkill /PID "pythonw.exe" /F
echo msgbox "All Python Code Has Been Killed" > %tmp%\tmp.vbs
cscript /nologo %tmp%\tmp.vbs
del %tmp%\tmp.vbs