def avg(numbers):
	len_numbers = len(numbers)
	if len_numbers == 0:
		raise ValueError('You have to provide at least one number in the list numbers')
	sum_total = 0
	for num in numbers:
		sum_total+=num
	return sum_total/float(len_numbers)

def variance(numbers):
	return 1

if __name__ == "__main__":
	import sys
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('inputFile', help="Text file that contains the numbers that will be used to calculate the metrics (one number per line)", type=str)
	parser.add_argument("--all", action="store_true", help="calculate all metrics")
	parser.add_argument("--avg", action="store_true", help="calculate average")
	parser.add_argument("--variance", action="store_true", help="calculate variance")
	parser.add_argument("--std-deviation", action="store_true", help="calculate standard deviation")
	parser.add_argument("--coefficient-of-variability", action="store_true", help="calculate coefficient of variability")
	parser.add_argument("--median", action="store_true", help="calculate median")
	parser.add_argument("--quartiles", action="store_true", help="calculate quartiles")
	args = parser.parse_args()
	try:
		file = open(args.inputFile, 'r')
		values=[]
		for line in file.readlines():
			values.append(int(line))
		if args.all:
			print('todos os valores')
			sys.exit()
		if args.avg:
			print(avg(values))
		if args.variance:
			print('variancia')
		if args.std_deviation:
			print('desvio padrao')
		if args.coefficient_of_variability:
			print('coefficient-of-variability')
		if args.median:
			print('mediana')
		if args.quartiles:
			print('quartis')
	except Exception:
		print("Error: There's no file with the name '{}'".format(args.inputFile))