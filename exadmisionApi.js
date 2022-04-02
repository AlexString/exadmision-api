import { PythonShell } from 'python-shell';

export default class ExadmisionApi {
	constructor(scriptName, mode, pythonBin) {
		this.pythonScriptName = scriptName;
		this.mode = mode;
		this.pythonBin = pythonBin;
		this.args = [];

		this.options = {
			mode: this.mode,
			pythonPath: this.pythonBin, // python venv path
			pythonOptions: ['-u'], // get print results in real-time
			scriptPath: './',
			args: this.args,
		};
	}
	_callPythonScript = () => {
		const callPythonScript = (req, res) => {
			PythonShell.run(this.pythonScriptName, this.options, (err, result) => {
				if (err) throw err;

				console.log('Output:');
				result.forEach(message => {
					console.log(message);
				});
			});
		};
		console.log('Calling python script');
		callPythonScript();
	};

	getQuestions = () => {
		this._callPythonScript();
	};

	getQuestionsByIds = ids => {
		this.args.push(...ids);
		this._callPythonScript();
		this.args.length = 0;
	};
}
