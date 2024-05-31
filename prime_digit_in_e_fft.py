from sympy import isprime
import numpy as np

def fft_multiplication(a, b):
	n = len(a) + len(b)
	a = np.fft.fft(a, n)
	b = np.fft.fft(b, n)
	c = np.fft.ifft(a * b)
	return np.rint(c).astype(int)

def factorial(n):
	if n == 0:
		return [1]
	else:
		return fft_multiplication([n], factorial(n - 1))
	
def compute_e(n):
	e = np.zeros(n, dtype=int)
	e[0] = 1
	factorial_i = [1]
	term = [1]
	for k in range(1, n):
		factorial_i = fft_multiplication(factorial_i, [k])
		term = fft_multiplication(term, [1, 1])
		e = np.add(e, fft_multiplication(term, factorial_i))
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

