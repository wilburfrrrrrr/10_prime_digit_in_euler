from sympy import isprime
import numpy as np
import decimal

def is_ten_digit(n):
	return len(str(n)) == 10

def fft_multiplication(a, b):
	n = len(a) + len(b) - 1
	a = np.fft.fft(a, n)
	b = np.fft.fft(b, n)
	c = np.fft.ifft(a * b)
	return np.rint(c).astype(int)[:n]

def factorial(n):
	if n == 0 or n == 1:
		return [1]
	else:
		fact = np.arange(1, n+1)
		for i in range(2, n):
			fact = fft_multiplication(fact, np.array([i]))
		return fact
	
def compute_e(n):
	decimal.getcontext().prec = n + 1
	e = 0
	fact = factorial(n)
	for i in range(n):
		e += 1 / fact[i]
	return e
	
def tenth_prime_digit_in_e(e_number):
	e = str(e_number)[2:]
	for i in range(len(e)):
		number = int(e[i:i+10])
		if isprime(number):
			return number
	return None

if __name__ == "__main__":
	n = 200
	e = compute_e(n)
	print(e)
	print(tenth_prime_digit_in_e(e))