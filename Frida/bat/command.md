adb forward tcp:27042 tcp:27042 # 端口转发, 安装frida用的
adb forward tcp:23946 tcp:23946 # 端口转发, IDA
magisk resetprop ro.debuggable 1 # 设置系统属性为可调试
## 模拟器
adb connect 127.0.0.1:16384;adb root;adb shell
adb shell ps -A # 查看模拟器进程
cd /data/local/tmp # 进入 frida 目录
./frida # 启动模拟器 frida 服务

# 模拟器启动 frida 服务之后
frida-ps -U # 查看进程号
frida -Uf jp.glee.girl -l hook.js #重启注入指定包名app
frida -Un jp.glee.girl -l hook.js #附加注入

exit # 退出 frida

# PC
frida -f "/.../*.exe" -l hook.js

