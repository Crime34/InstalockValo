Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "venv\Scripts\pythonw.exe" & chr(34) & " " & chr(34) & "main.py" & chr(34), 0
Set WshShell = Nothing 
