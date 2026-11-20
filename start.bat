@echo off
setlocal
echo ====================================================
echo Starting AppVault AI Application Server...
echo Open your browser at http://localhost:8000
echo ====================================================

set PYTHON_EXE=C:\Users\harshit\AppData\Local\Programs\Python\Python314\python.exe

if exist "%PYTHON_EXE%" (
    echo Using Python 3.14 at %PYTHON_EXE%
    "%PYTHON_EXE%" run.py
    goto end
)

if exist "%LOCALAPPDATA%\Programs\Python\Python314\python.exe" (
    echo Using Python 3.14 at %LOCALAPPDATA%\Programs\Python\Python314\python.exe
    "%LOCALAPPDATA%\Programs\Python\Python314\python.exe" run.py
    goto end
)

echo Attempting py launcher...
py -X utf8 run.py
if %ERRORLEVEL% EQU 0 goto end

echo Attempting python from PATH...
python run.py

:end
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Server exited with an error.
    pause
)
