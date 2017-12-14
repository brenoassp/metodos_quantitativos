from matplotlib import pyplot as plt

if __name__ == "__main__":
	import sys
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('inputFile', help="Text file that contains the numbers that will be used to calculate the pdf (one pair per line, e.g, 1 0.1)", type=str)
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
		if axis_x_lim is None:
			plt.plot(axis_x,axis_y)
			plt.title('Pdf of file sizes')
			plt.xscale('log')
			plt.xlim(1, 10)
			#plt.xticks([0.01, 0.1, 1, 10])
			plt.show()
	except Exception as e:
		print(e)
		print("Error: There's no file with the name '{}'".format(args.inputFile))