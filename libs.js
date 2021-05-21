function log(arg) { console.log(arg); }
const { promisify } = require('util');
const path = require('path');
const fsExtra = require('fs-extra')
const fs = require('fs');
const readdir = promisify(fs.readdir);
const stat = promisify(fs.stat);
const utf8 = require('utf8');
var spawn = require('child_process').spawn;
const { resolve } = require('path');
// - - - - - - - - - - - - - - - - - - - - - - - - - - - -


let exe = "./cwebp.exe";




async function getFiles(dir) {
    const subdirs = await readdir(dir);
    const files = await Promise.all(subdirs.map(async (subdir) => {
        const res = resolve(dir, subdir);
        return (await stat(res)).isDirectory() ? getFiles(res) : res;
    }));
    return files.reduce((a, f) => a.concat(f), []);
}
// - - - - - - - - - - - - - - - - - - - - - - - - - - - -












module.exports = {
    getFiles
}