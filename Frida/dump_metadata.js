// frida -Uf jp.glee.girl -l DumpMetadata.js // Android
// frida -f ".\*.exe" -l DumpMetadata.js // PC

// 这个还挺好用 jp.glee.girl 是包名 -U 是连接 USB 设备 -f 是启动应用 -n 是附加到正在运行的应用 -l 是加载脚本
// 如果成功导出, 数据会在 "/storage/emulated/0/Download/global-metadata.dat"
var save_path = "/storage/emulated/0/Download/global-metadata_dumped.dat"; // Android
// var save_path = "C:\\Users\\86182\\Downloads\\SKETCHY MASSAGE-2.0\\Photo\\Dump\\global-metadata_dumped.dat"; // PC
var metadata_header = "AF 1B B1 FA"; // global-metadata.dat header

var dumped = false;
function guess_metadata_size(base, rangeSize) {
    var sanity = Memory.readU32(base);
    var version = Memory.readU32(base.add(4));
    console.log("metadata sanity =", sanity.toString(16), "version =", version);

    var maxEnd = 0;
    var headerStart = base.add(8);

    for (var i = 0; i < 128; i++) { // scan first 0x400 bytes for offset/count pairs
        var offset = Memory.readU32(headerStart.add(i * 8));
        var count = Memory.readU32(headerStart.add(i * 8 + 4));

        if (offset === 0 || count === 0) {
            continue;
        }

        var end = offset + count;
        if (end > maxEnd && end < rangeSize) {
            maxEnd = end;
        }
    }

    return maxEnd;
}

function dump_metadata(pattern) {
    console.log("pattern:", pattern);

    ['r--', 'r-x', 'rw-'].forEach(function (perm) {
        Process.enumerateRangesSync(perm).forEach(function (range) {
            Memory.scan(range.base, range.size, pattern, {
                onMatch: function (address) {
                    if (dumped) return;

                    console.log("[+] found at", address);
                    var base = ptr(address);

                    var total = guess_metadata_size(base, range.size);

                    if (total < 0x100000) {
                        // fallback to older offsets
                        var off = base.add(0x108);
                        var cnt = base.add(0x10C);
                        total = Memory.readU32(off) + Memory.readU32(cnt);
                    }

                    if (total < 0x100000) {
                        // secondary fallback
                        var off2 = base.add(0x100);
                        var cnt2 = base.add(0x104);
                        total = Memory.readU32(off2) + Memory.readU32(cnt2);
                    }

                    console.log("metadata size =", total);
                    if (total < 0x100000) return;

                    var file = new File(save_path, "wb");
                    file.write(Memory.readByteArray(base, total));
                    file.close();

                    dumped = true;
                    console.log("dump done:", save_path);
                }
            });
        });
    });
    console.log("scan done");
}

setTimeout(function () {
     dump_metadata(metadata_header);
//    dump_metadata("5F E0 F9 F8");
}, 5000);

// ===== [ZaFrida Template Start: android_android_click_tracer] =====
// // Android Activity & Click Tracer (Android Activity与点击事件追踪器)
// // Logs Activity starts and View OnClick events to help locate UI logic. (记录Activity启动和View点击事件，帮助定位UI逻辑)
//
// function trace_activity_start() {
//     var Activity = Java.use("android.app.Activity");
//     Activity.startActivity.overload("android.content.Intent").implementation = function(intent) {
//         var component = intent.getComponent();
//         var target = component ? component.getClassName() : "Unknown";
//         console.log("[Activity] Starting: " + target);
//         console.log("  -> Intent: " + intent.toString());
//         return this.startActivity(intent);
//     }
// }
//
// function trace_view_clicks() {
//     var View = Java.use("android.view.View");
//     View.setOnClickListener.implementation = function(listener) {
//         if (listener != null) {
//             var listenerClassName = listener.getClass().getName();
//             console.log("[UI] setOnClickListener registered: " + listenerClassName);
//         }
//         return this.setOnClickListener(listener);
//     }
// }
//
// Java.perform(function() {
//     console.log("[.] UI Tracer Loaded");
//     trace_activity_start();
//     trace_view_clicks();
// });
// ===== [ZaFrida Template End: android_android_click_tracer] =====

// ===== [ZaFrida Template Start: android_android_hook_hashmap] =====
// // Android Hook HashMap (Android 钩子 HashMap)
// // 由于有些请求头会使用这个添加，可能通过okhttp直接增加(by 小佳)
// function hook_hashmap() {
//     var hashMap = Java.use("java.util.HashMap");
//     hashMap.put.implementation = function (a, b) {
//         console.log("hashMap.put: ", a, b);
//         return this.put(a, b);
//     }
// }
//
// function hook_concurrent_hashmap() {
//     var ConcurrentHashMap = Java.use("java.util.concurrent.ConcurrentHashMap");
//     ConcurrentHashMap.put.implementation = function (a, b) {
//         console.log("ConcurrentHashMap.put: ", a, b);
//         return this.put(a, b);
//     }
// }
//
// function hook_linked_hashmap() {
//     var LinkedHashMapClass = Java.use("java.util.LinkedHashMap");
//     LinkedHashMapClass.put.implementation = function (key, value) {
//         console.log("LinkedHashMap key:", key, "value:", value);
//         return this.put(key, value);
//     };
// }
//
// Java.perform(function() {
//     hook_hashmap();
//     hook_concurrent_hashmap();
//     hook_linked_hashmap();
// });
// ===== [ZaFrida Template End: android_android_hook_hashmap] =====
