import ExadmisionApi from './exadmisionApi.js';

function main() {
	const getResults = async () => {
		let result = await api.getQuestions();
		console.log('Python script without arguments output:');
		console.log(result);

		const questions = ['mult', 'sum', 'factor'];
		result = await api.getQuestionsById(questions);
		console.log('Python script with arguments output:');
		result.forEach(message => {
			console.log(message);
		});
	};

	let api = new ExadmisionApi('main.py', 'text', './venv/bin/python');

	getResults();
}

main();
