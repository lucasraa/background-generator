@echo off
echo Generate background ...
python make-background.py
IF %ERRORLEVEL% NEQ 0 (
  echo Error in Python script!
  pause
  exit /b
)

echo Set background...
@echo off

set IMAGE=%cd%\output.png

echo Set background to: %IMAGE%

powershell -Command ^
"Add-Type -TypeDefinition 'using System; using System.Runtime.InteropServices; public class Wallpaper { [DllImport(\"user32.dll\", CharSet=CharSet.Auto)] public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni); }'; ^
[Wallpaper]::SystemParametersInfo(20, 0, '%IMAGE%', 3)"

echo Done!
exit