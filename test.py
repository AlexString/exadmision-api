import sys

def output(num):
	return f'Output from Python {num*2}'
	

def main():
	number = sys.argv[1]
	print(output(number))

main()