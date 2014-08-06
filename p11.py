import sys

def prod_horr(arr):
	themax = 0
	for line in arr:
		for i in range(0, len(line) - 4):
			prod = int(line[i]) * int(line[i + 1]) * int(line[i + 2]) * int(line[i + 3])
			if prod > themax:
				themax = prod
	print "Horizontal Max: " + str(themax)
	return themax

def prod_vertd(arr):
	themax = 0
	for i in range(len(arr) - 4):
		for n in range(len(arr[0])):
			prod = int(arr[i][n]) * int(arr[i + 1][n]) * int(arr[i + 2][n]) * int(arr[i + 3][n])
			if prod > themax:
				themax = prod
	print "Vertical Max: " + str(themax)
	return themax

def prod_diagr(arr):
	themax = 0
	for i in range(len(arr) - 4):
		for n in range(len(arr[0]) - 4):
			prod = int(arr[i + n][i + n]) * int(arr[i + n + 1][i + n + 1]) * int(arr[i + n + 2][i + n + 2]) * int(arr[i + n + 3][i + n + 3])
			if prod > themax:
				themax = prod
	print "Diagonal \ Max: " + str(themax)
	return themax	

def prod_diagl(arr):
	themax = 0
	for i in range(len(arr) - 4):
		for n in range(3, len(arr[0])):
			prod = int(arr[n - i][n - i]) * int(arr[n - i - 1][n - i - 1]) * int(arr[n - i - 2][n - i - 2]) * int(arr[n - i - 3][n - i -  3])
			if prod > themax:
				themax = prod
	print "Diagonal / Max: " + str(themax)
	return themax	

def main():
	f = open(sys.argv[1])
	arr = f.readlines()
	newarr = []
	for line in arr:
		newarr.append(line.strip().split(" "))
	print max(prod_horr(newarr), prod_vertd(newarr), prod_diagr(newarr), prod_diagl(newarr))
	return

main()