from decimal import Decimal, getcontext

def calculate_e_terms(n):
    getcontext().prec = n + 50  # Set precision higher than needed to handle intermediate steps
    result = Decimal(2)  # Start with 2 (1 + 1)
    factorial_value = Decimal(1)
    
    for i in range(2, n + 1):
        factorial_value *= i
        result += Decimal(1) / factorial_value
    
    return result

def format_result(e_value, decimal_places):
    e_str = str(e_value)
    integer_part, decimal_part = e_str.split('.')
    formatted_e = integer_part + '.' + decimal_part[:decimal_places]
    return formatted_e

def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_first_prime_in_e(precision, length):
    """Find the first prime number of a given length in the decimals of e."""
    getcontext().prec = precision + 10  # Extra precision to ensure accuracy
    e_value = calculate_e_terms(precision)
    e_str = format_result(e_value, precision)
    e_decimals = e_str.replace('.', '')  # Get the decimal part of e without the dot
    
    for i in range(len(e_decimals) - length + 1):
        candidate = int(e_decimals[i:i + length])
        if is_prime(candidate):
            return candidate
    return None

# Parameters
decimal_places = 200  # Calculate 100,000 decimal places of e
length = 10  # Length of the prime number to find

# Find the first prime number of the given length in the decimals of e
prime_number = find_first_prime_in_e(decimal_places, length)

if prime_number:
    print(f"The first prime number of {length} digits in the decimals of e is: {prime_number}")
else:
    print(f"No prime number of {length} digits found in the first {decimal_places} decimal places of e.")
