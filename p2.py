# Even Fibonacci number sum function without using recursion
def fib_norecurs(nmax):
	s, n, cumsum = 0, 1, 0
	while s < nmax:
		s, n = n, s + n
		if n % 2 == 0:
			cumsum += n
	return cumsum

# Even Fibonacci number sum function using recursion
# Would hit recursion limit for higher max
def fib_recurs(start1, start2, max, cumsum):
	next = start1 + start2
	
	if next > max:
		return cumsum
	elif next % 2 == 0:
		cumsum = cumsum + next

	return fib(start2, next, max, cumsum)
	
# print fib_recurs(0, 1, 4000000, 0)
print fib_norecurs(4000000)
