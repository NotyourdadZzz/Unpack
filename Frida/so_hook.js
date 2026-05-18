// frida -Uf jp.glee.girl -l so_hook.js
var FALLBACK_OFFSET = 0x8EC128;

var finded = false
var addr;
var notFirstTime = true
var s_GlobalMetadataHeader;
var completed = false;
var metadataLoaderFunc = null;
var searchAttempted = false;

function get_self_process_name() {
    var openPtr = Module.getExportByName('libc.so', 'open');
    var open = new NativeFunction(openPtr, 'int', ['pointer', 'int']);

    var readPtr = Module.getExportByName("libc.so", "read");
    var read = new NativeFunction(readPtr, "int", ["int", "pointer", "int"]);

    var closePtr = Module.getExportByName('libc.so', 'close');
    var close = new NativeFunction(closePtr, 'int', ['int']);

    var path = Memory.allocUtf8String("/proc/self/cmdline");
    var fd = open(path, 0);
    if (fd != -1) {
        var buffer = Memory.alloc(0x1000);

        var result = read(fd, buffer, 0x1000);
        close(fd);
        result = ptr(buffer).readCString();
        return result;
    }

    return "-1";
}

var intervalId = setInterval(() => {
    if (completed) {
        clearInterval(intervalId);
        return;
    }

    if (finded) {
        if (addr != null && metadataLoaderFunc == null && !searchAttempted) {

            if (metadataLoaderFunc == null) {
                metadataLoaderFunc = addr.base.add(FALLBACK_OFFSET);
            }
        }

        if (metadataLoaderFunc != null) {
            if (notFirstTime) {
                notFirstTime = false;
                try {
                    Interceptor.attach(metadataLoaderFunc, {
                        onEnter: function (args) {
                            console.log("MetadataLoader::LoadMetadataFile 被调用");
                        },
                        onLeave: function (retval) {
                            console.log("s_GlobalMetadataHeader：" + retval.toString(16));
                            s_GlobalMetadataHeader = retval;
                            save(get_size());
                            completed = true;
                        }
                    });
                } catch (e) {
                    completed = true;
                }
            }
        }
    } else {
        try {
            addr = Process.findModuleByName("libil2cpp.so");
            if (addr != null) {
                console.log("找到libil2cpp.so模块，基址: " + addr.base.toString(16));
                finded = true;
            }
        } catch (e) {
        }
    }
}, 100);

function get_size() {
    const metadataHeader = s_GlobalMetadataHeader;
    let fileOffset = 0x10C;
    let lastCount = 0;
    let lastOffset = 0;
    while (true) {
        lastCount = Memory.readInt(ptr(metadataHeader).add(fileOffset));
        if (lastCount !== 0) {
            lastOffset = Memory.readInt(ptr(metadataHeader).add(fileOffset - 4));
            break;
        }
        fileOffset -= 8;
        if (fileOffset <= 0) {
            console.log("获取到的大小错误!");
            break;
        }
    }
    return lastOffset + lastCount;
}

function save(size) {
    var file = new File("/data/data/" + get_self_process_name() + "/global-metadata.dat", "wb");
    var contentBuffer = Memory.readByteArray(s_GlobalMetadataHeader, size);
    file.write(contentBuffer);
    file.flush();
    file.close();
    console.log("global-metadata已导出到/data/data/" + get_self_process_name() + "/global-metadata.dat")
}