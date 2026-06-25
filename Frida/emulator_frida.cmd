adb connect 127.0.0.1:16384;adb root;adb shell
cd /data/local/tmp
./frida
# adb shell ps -A
# exit
adb forward tcp:27042 tcp:27042

frida-ps -U
frida -Uf jp.glee.girl -l hook.js #重启注入
frida -Un jp.glee.girl -l hook.js #附加注入