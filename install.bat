@echo off
setlocal enabledelayedexpansion

echo ==============================
echo Background Generator Setup
echo ==============================
echo.

REM --- Check if Python is installed ---
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python not found in PATH.
    echo.
    echo Please install Python 3.6+ from: https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
) ELSE (
    echo [OK] Python is installed.
    python --version
)

echo.

REM --- Upgrade pip ---
echo [*] Upgrading pip...
python -m pip install --upgrade pip
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to upgrade pip.
    pause
    exit /b 1
)

echo [OK] pip upgraded successfully.
echo.

REM --- Install dependencies from requirements.txt ---
echo [*] Installing dependencies from requirements.txt...
IF NOT EXIST requirements.txt (
    echo [ERROR] requirements.txt not found!
    pause
    exit /b 1
)

pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)

echo [OK] All dependencies installed.
echo.
echo ==============================
echo Setup Complete!
echo ==============================
echo.
echo Next steps:
echo 1. Edit config.json with your preferences
echo 2. Add a background image (background.png) to this folder
echo 3. Run: set-background.bat
echo.

pause
