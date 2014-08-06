# Triangle Numbers
# The ith triangle number is the sum of the first i natural numbers
# Find the first triangular number with over 500 divisors

import sys

# Generates N triangle numbers
def tri_gen(n):
	TRIANGLE = [0]
	for i in range(1, n):
		TRIANGLE.append(TRIANGLE[i - 1] + i)
	return TRIANGLE

# Find the number of divisors in a number
def n_divisors(num):
	maxrt = num ** 0.5
	cumsum = 0
	for i in range(2, int(maxrt) + 1):
		if num % i == 0:
			cumsum += 2
	return cumsum + 2 
	# Add in 1 and num

def max_div(tris):
	max = 0
	for i in range(len(tris)):
		n_div = n_divisors(tris[i])
		if n_div > max:
			max = n_div
		if max > 500:
			return tris[i]
	return 0

def main():
	TRI = tri_gen(int(sys.argv[1]))
	retval = max_div(TRI) 
	if retval == 0:
		print "FAIL. DREAM BIGGER"
		print "BIGGEST NUMBER: " + str(n_divisors(TRI[-1]))
	else:
		print "SUCCESS! " + str(retval)
	return

main()
