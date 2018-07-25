var html = require('pa11y-reporter-html');
var pa11y = require('pa11y');
var fs = require("fs");
//var y = require('events').EventEmitter.prototype._maxListeners = 100;


async function runPa11y(url) {
    try {
        let results = await pa11y(url);
        let htmlResults = html.results(results);
        return htmlResults
    } catch (err) {
        console.log("Error: " + err)
    }
}


function listScript() {
    const args = process.argv;
    const os = require('os');
    const siteName = args[2];

    pathToSiteDir = os.homedir() + "/" + siteName
    try {
        fd = fs.openSync(pathToSiteDir + '/audits/results-pally.html', 'w');
    } catch (err) {
        console.log("Could not open results.html" + err)
    } finally {
        if (fd !== undefined)
            fs.closeSync(fd);
    }

    var array = fs.readFileSync(pathToSiteDir + "/crawled.txt").toString().split("\n");
    array = array.filter(function(entry) { return entry.trim() != ''; }); //removes empty element at the end of array

    (function theLoop (i) {
        setTimeout(function () {
            console.log("url: " + array[i])
            let reply = runPa11y(array[i])
            reply.then(function(result) {
                try {
                    fd = fs.openSync(pathToSiteDir + '/audits/results-pally.html', 'a');
                    fs.appendFileSync(fd, result + "<br>", 'utf8');
                } catch (err) {
                    console.log("Could not open results.html" + err)
                } finally {
                if (fd !== undefined)
                    fs.closeSync(fd);
                }
            });

            --i
            if (i >= 0) {          // If i > 0, keep going
                theLoop(i);       // Call the loop again, and pass it the current value of i
                console.log("Links left to audit: " + i)
            }
        }, 1000);
    })(array.length -1);
}

listScript()
