from math import sqrt, log10

def avg(numbers):
	len_numbers = len(numbers)
	if len_numbers == 0:
		raise ValueError('You have to provide at least one number in the list numbers')
	sum_total = 0
	for num in numbers:
		sum_total+=num
	return sum_total/float(len_numbers)

def variance(numbers):
	average=avg(numbers)
	squares=[]
	for num in numbers:
		squares.append((num - average) * (num - average))
	return avg(squares)

def standard_deviation(numbers):
	var=variance(numbers)
	return sqrt(var)

def coefficient_of_variability(numbers):
	average = avg(numbers)
	std_deviation = standard_deviation(numbers)
	return std_deviation/average

def median(numbers):
	numbers=sorted(numbers)
	n = len(numbers)
	if n%2 == 1:
		return numbers[n//2]
	else:
		i = n//2
		return (numbers[i-1] + numbers[i])/2

def cdf(numbers, gambiarra=False):
	numbers = sorted(numbers)
	last = numbers[0]
	total = len(numbers)
	cnt = 0
	x = []
	y = []
	axis_x_lim = None
	for num in numbers:
		if num != last:
			print(last, cnt/float(total))
			cnt += 1
			last = num
		else:
			cnt += 1
	print(last, cnt/float(total))

def pdf(numbers):
	numbers=sorted(numbers)
	if numbers.count(0) > 0:
		numbers = numbers[numbers.count(0):]
	last = numbers[0]
	total = len(numbers)
	cnt = 0
	for num in numbers:
		if num != last:
			print(log10(last), cnt/float(total))
			cnt = 1
			last = num
		else:
			cnt += 1
	print(log10(last), cnt/float(total))

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
	parser.add_argument("--cdf", action="store_true", help="calculate cdf")
	parser.add_argument("--pdf", action="store_true", help="calculate pdf")
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
			sys.exit()
		if args.variance:
			print('variancia')
			print(variance(values))
			sys.exit()
		if args.std_deviation:
			print('desvio padrao')
			print(standard_deviation(values))
			sys.exit()
		if args.coefficient_of_variability:
			print('coefficient-of-variability')
			print(coefficient_of_variability(values))
			sys.exit()
		if args.median:
			print('mediana')
			print(median(values))
			sys.exit()
		if args.quartiles:
			print('quartis')
			sys.exit()
		if args.cdf:
			cdf(values)
			sys.exit()
		if args.pdf:
			pdf(values)
			sys.exit()
	except Exception as e:
		print(e)
		print("Error: There's no file with the name '{}'".format(args.inputFile))