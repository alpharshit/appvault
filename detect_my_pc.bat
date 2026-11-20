@echo off
title AppVault AI - Hardware Detection Utility
echo ===================================================================
echo             AppVault AI — Hardware Detection Utility
echo ===================================================================
echo Scanning your Windows PC hardware specifications...
echo.

if exist "%~dp0backend\app\native_detector.py" (
    py -X utf8 "%~dp0backend\app\native_detector.py"
) else if exist "%~dp0native_hardware_detector.py" (
    py -X utf8 "%~dp0native_hardware_detector.py"
) else (
    py -c "import urllib.request; exec(urllib.request.urlopen('http://127.0.0.1:8000/api/detection/native-utility/download').read().decode('utf-8'))"
)

if %ERRORLEVEL% NEQ 0 (
    if exist "%~dp0backend\app\native_detector.py" (
        python "%~dp0backend\app\native_detector.py"
    ) else if exist "%~dp0native_hardware_detector.py" (
        python "%~dp0native_hardware_detector.py"
    )
)

echo.
pause
