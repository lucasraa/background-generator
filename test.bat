@echo off
echo Generate background...

python make-background.py

IF %ERRORLEVEL% NEQ 0 (
echo Error in Python script!
pause
exit /b
)

echo Open generated image...
start output.png