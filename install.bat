@echo off
:: Sprawdzenie Pythona
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python nie jest zainstalowany. Pobierz i zainstaluj Python 3.x!
    pause
    exit /b
)

:: Instalacja wymaganych bibliotek
echo Instalacja wymaganych bibliotek...
pip install --upgrade pip
pip install pyautogui keyboard colorama

:: Uruchomienie skryptu
echo Uruchamianie autoklikera...
cls 

call start.bat