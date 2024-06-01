import time
import decimal
from math import factorial
from sympy import isprime

# Función para calcular e utilizando la serie de Taylor
def calculate_e(num_terms):
    decimal.getcontext().prec = num_terms + 1
    e_sum = decimal.Decimal(0)
    for n in range(num_terms):
        e_sum += decimal.Decimal(1) / decimal.Decimal(factorial(n))
    return e_sum

def find_prime_in_e(e_value):
    e_str = str(e_value)[2:]  # Convertir e a string y eliminar "2."
    for i in range(len(e_str) - 9):  # Recorrer los decimales de e
        candidate = int(e_str[i:i+10])  # Tomar un bloque de 10 dígitos
        if isprime(candidate):
            return candidate
    return None

# Función para medir el tiempo de ejecución
def measure_time(num_terms):
    start_time = time.time()
    e = calculate_e(num_terms)
    end_time = time.time()
    elapsed_time1 = end_time - start_time
    start_time = time.time()
    prime10 = find_prime_in_e(e)
    end_time = time.time()
    elapsed_time2 = end_time - start_time
    return elapsed_time1, elapsed_time2,  elapsed_time2+elapsed_time1, prime10



# Calcular e y medir el tiempo
elapsed_time1, elapsed_time2, elapsed_time3, prime10 = measure_time(200)
print(f"Tiempo de ejecución: {elapsed_time1} segundos de los digitos de e")
print(f"Tiempo de ejecución: {elapsed_time2} segundos encontrando el numero primo de 10 digitos")
print(f"Tiempo de ejecución: {elapsed_time3} total")
if prime10:
    print(f"El primer número primo de 10 dígitos en los decimales de e es: {prime10}")
else:
    print("No se encontró un número primo de 10 dígitos en los decimales de e con los términos calculados.")