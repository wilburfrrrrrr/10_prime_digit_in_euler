from sympy import isprime
import numpy as np

def fft_multiplication(a, b):
	n = len(a) + len(b) - 1
	n_transform = 2 ** int(np.ceil(np.log2(n)))
	a = np.fft.fft(a, n_transform)
	b = np.fft.fft(b, n_transform)
	c = np.fft.ifft(a * b)
	return np.rint(c).astype(int)[:n]

def factorial(n):
	if n == 0 or n == 1:
		return [1]
	else:
		fact = [1]
		for i in range(2, n):
			fact = fft_multiplication(fact, np.array([i]))
		print(f"{fact}")
		return fact
	
def compute_e(n):
	digits = [2]
	factorials = [1]
	for i in range(1, n):
		factorials.append(factorial(i))
	for k in range(1, n):
		term = [1]
		factorial_k = factorials[k]
		
		for i in range(len(term)):
			if i < len(factorial_k) and factorial_k[i] != 0:
				term[i] //= factorial_k[i]
			else:
				term[i] = 0
		
		if len(term) > len(digits):
			digits.extend([0] * (len(term) - len(digits)))
		for i in range(len(term)):
			digits[i] += term[i]

	return digits if len(digits) <= n else digits[:n]
	
def tenth_prime_digit_in_e(e_number):
	e = ''.join(map(str, e_number))
	for i in range(len(e) - 9):
		number = int(e[i:i+10])
		if isprime(number):
			return number
	return None

if __name__ == "__main__":
	n = 20
	e = compute_e(n)
	print(e)
	print(tenth_prime_digit_in_e(e))