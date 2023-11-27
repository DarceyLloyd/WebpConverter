const aftc = require("aftc-node-tools")
const log = aftc.log;
const fs = require('fs');
const fsExtra = require('fs-extra')
const path = require('path');
var spawn = require('child_process').spawn;
let { getFiles} = require("./libs");

console.clear();

let exe = path.resolve("./cwebp.exe");
let quality = 76; // 0 = bad, 100 = best, best values are between 70 to 80

start();
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -










async function start() {

    let inputDir = path.resolve("./input");


    await fsExtra.remove("./output");
    await fsExtra.mkdir("./output");

    let outputDir = path.resolve("./output");

    await getFiles(inputDir)
        .then(async (files) => {

            log("WEBP Converter v1.1.0".green);
            log("WARNING: This can take a long time".cyan);
            // log(("inputDir = "+inputDir).cyan);
            // log(("outputDir = "+outputDir).cyan);
            log(("No of files to convert " + files.length).cyan);


            for await (const inputFile of files) {

                let fileName = path.basename(inputFile);
                let ext = path.extname(inputFile);
                // fileName = fileName.replace(/[^a-zA-Z0-9.]/g, "");
                fileName = fileName.replace(/[\r\n]/g, "");
                fileName = fileName.replace(ext, ".webp");

                let outputFile = path.resolve((outputDir + "/" + fileName))

                // log("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #".yellow)
                // log("inputFile = " + inputFile);
                // log("outputFile = " + outputFile);

                await convertFile(inputFile, outputFile)
                .then((response) => {
                    // log(response);
                    // log(("Processed file: " + c + "/" + noOfFilesToProcess + " - " + params.correctedSourcePath + " [" + params.bitDepth + "Bit]").green);
                })
                .catch((response) => {
                    // log("ERROR: " + response);
                    // errorCount++;
                    // log(("ERROR: " + params.correctedSourcePath + " [" + params.bitDepth + "Bit]").red);
                })

            }; // end files.forEach

            // log("COMPLETE!".green);

        })


}
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


async function convertFile(source, target) {

    let args = [
        "-q",
        quality,
        source,
        "-o",
        target
    ]


    return new Promise((resolve, reject) => {
        var proc = spawn(exe, args);

        proc.stdout.on('data', function (data) {
            // console.log(data);
            // resolve(true);
        });

        proc.stderr.setEncoding("utf8")
        proc.stderr.on('data', function (data) {
            console.log(data);
            reject(false);
        });

        proc.on('close', function () {
            resolve(true);
        });
    })

}
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -