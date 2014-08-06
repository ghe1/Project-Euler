def fib(start1, start2, max, cumsum):
	next = start1 + start2
	
	if next > max:
		print cumsum
		return
	elif next % 2 == 0:
		cumsum = cumsum + next

	fib(start2, next, max, cumsum)
	
fib(1, 2, 4000000, 2)