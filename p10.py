import sys

def sieve(n):
	SIEVE = [False, False] + ([True] * (n - 1))
	maxrt = n ** 0.5
	for i in range(2, int(maxrt) + 1):
		if SIEVE[i] is True:
			for t in range(2, n/i + 1):
				SIEVE[i*t] = False
	return SIEVE


def main():
	SIEVE = sieve(int(sys.argv[1]))
	runtot = 0
	for i in range(0, len(SIEVE)):
		if SIEVE[i] is True:
			runtot += i
	print runtot
	return

main()

