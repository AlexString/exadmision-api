class Question:
	def __init__(self, id: int, formula_id: int, description: str, values_range: str, values_count: int):
		self.id = id
		self.formula_id = formula_id
		self.description = description
		self.answers = None

		self._values_range = values_range
		self._values_count = values_count
	
	def _is_answers(self):
		return True if self.answers != None else False 

	def set_description_values(self, values: list):
		if self._values_count != len(values):
			return		

		index = 0
		for i in range(1,self._values_count+1):
			self.description.replace(f'\${i}', values[index])
			index += 1

	def set_answers(self, correct: float, wrong: list):
		if len(wrong) is not 3:
			return

		self.answers = {
			"correct": correct,
			"wrong": wrong
		}
	
	def _drop_unnecesary_values(self):
		del self._values_range
		del self._values_count
	
	def transform_jsonable(self):
		if not self._is_answers():
			return

		self._drop_unnecesary_values()