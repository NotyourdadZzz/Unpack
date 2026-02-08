Process.enumerateModules().forEach(m => {
    if (m.name.indexOf("il2cpp") !== -1) {
        console.log(m.name, m.base);
    }
});