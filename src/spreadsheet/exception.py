class SpreadsheetError(Exception):
	def __init__(self,message):
		super().__init__(message)

class SpreadsheetNotFoundError():
	def __init__(self):
		raise SpreadsheetError('Spreadsheet file not found or file extension does not match .xlsx or .csv')

class SpreadsheetNotSetError():
	def __init__(self):
		raise SpreadsheetError('Spreadsheet is not set, cannot generate dataset')