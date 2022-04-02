import pandas as pd

class QuestionSpreadsheet:
	def __init__(self, df: pd.DataFrame):
		self._spreadsheet = df
		self._priority = None

 
	def set_priority(self, ids):
		self._priority = ids

	def generate(self):
		pass