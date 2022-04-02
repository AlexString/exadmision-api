import sys, json, pandas as pd
from pprint import pprint

# from api import ExadmisionApi

def main():
	system_arguments = sys.argv[1:]
	#exadmision_api = ExadmisionApi('./data/filename.csv')

	if len(system_arguments) == 0:
		print('No arguments provided')

	elif len(system_arguments) != 2:
		print('more than 1 argument sent')
		print(system_arguments)
	
main()