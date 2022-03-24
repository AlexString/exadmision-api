from api import ExadmisionApi

import sys
import re

import json
import pandas as pd

from pprint import pprint

from src.Question.question import Question

def test_question():
	myQuestion = Question(1,1,'Descripcion','12-24',2)
	myQuestion.set_answers(23.1,[23,20,19])

	pprint(json.dumps(myQuestion.__dict__,ensure_ascii=False))

	print('\n')

	myQuestion.transform_jsonable()
	pprint(json.dumps(myQuestion.__dict__,ensure_ascii=False))

def test_commands():
	def test_pandas_venv():
		df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
                   'monkey', 'parrot', 'shark', 'whale', 'zebra']})
		print(df.head())

	test_pandas_venv()


#test_question()
#test_commands()

def main():
	exadmision_api = ExadmisionApi('file/path')
	url_parameter = sys.argv[1]

	if url_parameter == 'questions':
		return exadmision_api.get_questions()

	if re.search("questions?", url_parameter) != None:
		url_parameter = url_parameter.replace('questions?','')
		formula_ids = url_parameter.split(',')

		exadmision_api.give_priorization_on_ids(formula_ids)
		return exadmision_api.get_questions()