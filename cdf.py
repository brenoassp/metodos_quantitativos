from matplotlib import pyplot as plt

if __name__ == "__main__":
	import sys
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('inputFile', help="Text file that contains the numbers that will be used to calculate the cdf (one pair per line, e.g, 1 0.1)", type=str)
	parser.add_argument("--limit-axis", action="store", help="plot cdf with chosen y axis", type=float)
	parser.add_argument("--title", action="store", help="chart title", type=str)
	args = parser.parse_args()
	try:
		file = open(args.inputFile, 'r')
		axis_x = []
		axis_y = []
		axis_x_lim = None
		for line in file.readlines():
			splited_line = line.split()
			current_x = float(splited_line[0])
			current_y = float(splited_line[1])
			axis_x.append(current_x)
			axis_y.append(current_y)
			if args.limit_axis:
				if axis_x_lim is None and current_y > args.limit_axis:
					axis_x_lim = current_x
		if axis_x_lim is None:
			plt.plot(axis_x,axis_y)
			if not args.title:
				plt.title('Cdf of file sizes')
			else:
				plt.title(args.title)
			plt.savefig('cdf.png')
			plt.show()
		else:
			plt.plot(axis_x,axis_y)
			plt.axis([0, axis_x_lim, 0, 1])
			if not args.title:
				plt.title('Cdf of file sizes')
			else:
				plt.title(args.title)
			plt.savefig('cdf.png')
			plt.show()
	except Exception as e:
		print(e)
		print("Error: There's no file with the name '{}'".format(args.inputFile))