import sys
import json

def main():
	dictionary = {
		'message': 'Hello World',
		'source': 'python script test.py'
	}
	return json.dumps(dictionary)

print(main())