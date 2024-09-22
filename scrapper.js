const fs = require("fs");
const { exec } = require("child_process");
fs.readFile("../Webscapper/data.json", "utf-8", (err, data) => {
  if (err) throw err;
  const jsonData = JSON.parse(data);
  console.log(jsonData);
});

//function to run python script

function runPythonScript() {
  exec("python ../Webscapper/webscraper.py", (err, stdout, stderr) => {
    if (err) {
      console.error(`Error executing Python script: ${err}`);
      return;
    }
    console.log(`Python script output: ${stdout}`);
  });
}

runPythonScript();
