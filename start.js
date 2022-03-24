// Requiring express for routing and fetching data on routing
var express = require('express');
var app = express();

const { PythonShell } = require('python-shell');
  
// Creates server on port 3000 -> localhost:3000/route
app.listen(3000, () => {
    console.log('server running on port 3000');
} )
  
function callPythonScript(req, res, next) {
    // Options objecto for PythonShell
	let options = {
		mode: 'text',
		//pythonPath: './venv/bin/python' // Python venv path
		pythonOptions: ['-u'], // get print results in real-time
		//scriptPath: '',
		args: ['0'] //An argument which can be accessed in the script using sys.argv[1]
	};

	PythonShell.run('main.py', options, (err, result) => {
		if (err) throw err;

		// result is an array consisting of messages collected
		//during execution of script.
		//console.log('result: ', result.toString());
		res.send(result.toString())
	});
}

// E.g : http://localhost:3000/getsum?number=2
app.get('/', callPythonScript);