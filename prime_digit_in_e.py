from sympy import isprime

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
	

def compute_e(n):
	e = 0
	for i in range(n):
		e += 1 / factorial(i)
	return e

def tenth_prime_digit_in_e():
	#generate digits until we find the 10th prime digit
	n = 0
	i = 0
	while n < 10:
		e = compute_e(i)
		for digit in str(e):
			if digit != '.':
				if isprime(int(digit)):
					n += 1
					if n == 10:
						break
		i += 1
	return i
