import ExadmisionApi from './exadmisionApi.js';

function main() {
	let api = new ExadmisionApi('main.py', 'text', './venv/bin/python');
	api.getQuestions();

	const questions = ['mult', 'sum', 'factor'];
	api.getQuestionsByIds(questions);
}

main();
