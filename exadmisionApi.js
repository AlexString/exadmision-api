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

	callPythonScript = () => {
		return new Promise((resolve, reject) => {
			PythonShell.run(this.pythonScriptName, this.options, (err, result) => {
				if (err) reject(err);

				resolve(result);
			});
		});
	};

	getQuestions = async () => {
		let result = await this.callPythonScript();
		return result;
	};

	getQuestionsById = async ids => {
		this.args.push(...ids);
		let result = await this.callPythonScript();
		this.args.length = 0;
		return result;
	};
}
