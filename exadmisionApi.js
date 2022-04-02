import { PythonShell } from 'python-shell';

export default class ExadmisionApi {
	constructor() {
		this.pythonScriptName = 'test.py';
		this.args = [];

		this.options = {
			mode: 'json',
			pythonPath: './venv/bin/python', // python venv path
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
				console.log(result.pop());
				//res.send(result.toString());
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
