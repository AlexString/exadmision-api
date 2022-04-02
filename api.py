from src.Spreadsheet.reader import SpreadsheetReader
from src.Spreadsheet.question_spreadsheet import QuestionSpreadsheet

from src.Resolver.resolver import Resolver
from src.Encoder.encoder import Encoder

from src.Question.builder import QuestionBuilder

class ExadmisionApi:
	def __init__(self, file_path):
		self.reader = SpreadsheetReader()
		self._resolver = Resolver()
		self._builder = QuestionBuilder()
		self._encoder = Encoder()

		self._questions_spreadsheet = QuestionSpreadsheet(self.reader.read_file(file_path))
	
	def give_priorization_on_ids(self, ids: list):
		self._questions_spreadsheet.set_priority(ids)
	
	def process_questions(self):
		new_questions_spreadsheet = self._questions_spreadsheet.generate()
		new_questions_spreadsheet = self._resolver.resolve(self._questions_spreadsheet)

		questions = self._builder.execute(new_questions_spreadsheet)	
		json_questions = self._encoder.encode_to_json(questions)

		return json_questions

	def get_questions(self):
		json_questions = self.process_questions()
		return json_questions