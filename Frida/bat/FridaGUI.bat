@echo off
chcp 65001 >nul
echo 正在启动 FridaUiTools...
start "" "D:\Tools\ReverseTools\FridaGUI\fridaUiTools_2.0.3_windows\fridaUiTools.exe"

echo 等待 3 秒确保程序加载...
timeout /t 3 /nobreak >nul

echo 正在连接 ADB...
adb connect 127.0.0.1:16384
adb root
adb shell "cd /data/local/tmp && ./frida"
