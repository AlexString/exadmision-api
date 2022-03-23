import json
from pprint import pprint

from src.Question.question import Question

def test_question():
	myQuestion = Question(1,1,'Descripcion','12-24',2)
	myQuestion.set_answers(23.1,[23,20,19])

	pprint(json.dumps(myQuestion.__dict__,ensure_ascii=False))

	print('\n')

	myQuestion.transform_jsonable()
	pprint(json.dumps(myQuestion.__dict__,ensure_ascii=False))

test_question()