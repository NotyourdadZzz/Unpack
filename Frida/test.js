const moduleName = "GameAssembly.dll"; // Change if it's a different module
const imageBase = 0x180000000; // Standard IDA base

// Calculate offsets
const targetFuncOffset = 0x1801C1B80 - imageBase; 
const metadataPtrOffset = 0x181BDF3B8 - imageBase;
const dumpSize = 1024 * 1024 * 20;
const path = "C:\\Users\\86182\\Downloads\\TEMP\\dumped_metadata.dat";

function hookMetadata() {
    const baseAddr = Module.getBaseAddress(moduleName);
    console.log("[*] Module Base Address: " + baseAddr);

    if (!baseAddr) {
        console.error("[-] Could not find " + moduleName);
        return;
    }
    
    console.log("[+] Base Address: " + baseAddr);

    const targetFunc = baseAddr.add(targetFuncOffset);
    const metadataGlobalPtr = baseAddr.add(metadataPtrOffset);
    console.log("[+] Target Function Address: " + targetFunc);

    Interceptor.attach(targetFunc, {
        onEnter: function(args) {
            console.log("[*] Entered custom Metadata initialization function...");
        },
        onLeave: function(retval) {
            console.log("[+] Initialization complete. Extracting metadata...");

            // Read the global variable that holds the pointer to the decrypted metadata
            const metadataBase = metadataGlobalPtr.readPointer();
            console.log("[+] Decrypted Metadata Base Address: " + metadataBase);

            if (metadataBase.isNull()) {
                console.error("[-] Metadata pointer is null!");
                return;
            }

            // The metadata header usually contains its own size or we can dump a large chunk.
            // Standard Il2Cpp metadata starts with a magic number, then version, then size/offsets.
            // If the magic number is obfuscated, you might just want to dump a fixed size (e.g., 10MB)
            // or parse the header size dynamically.
            
            console.log("[*] Dumping " + dumpSize + " bytes of metadata...");
            
            try {
                const dumpedBytes = metadataBase.readByteArray(dumpSize);
                
                // Save to file (requires Frida to be running with file write permissions, 
                // or send back to Python/Node.js host via send())
                const file = new File(path, "wb");
                file.write(dumpedBytes);
                file.flush();
                file.close();
                
                console.log("[+] Successfully dumped to " + path);
            } catch (e) {
                console.error("[-] Failed to dump memory: " + e);
            }
        }
    });
}

rpc.exports = {
    init: function() {
        hookMetadata();
    }
};