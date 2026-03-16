//frida -Uf jp.glee.girl -l DumpMetadata.js
// 这个还挺好用 jp.glee.girl 是包名 -U 是连接 USB 设备 -f 是启动应用 -n 是附加到正在运行的应用 -l 是加载脚本
// 如果成功导出, 数据会在 "/storage/emulated/0/Download/global-metadata.dat"
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

                    var path = "/storage/emulated/0/Download/global-metadata.dat";
                    var file = new File(path, "wb");
                    file.write(Memory.readByteArray(base, total));
                    file.close();

                    dumped = true;
                    console.log("dump done:", path);
                }
            });
        });
    });
}

setTimeout(function () {
    dump_metadata("AF 1B B1 FA");
}, 5000);
