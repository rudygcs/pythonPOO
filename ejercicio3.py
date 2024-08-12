# Función para calcular el factorial de un número
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

# Función para verificar si un número es perfecto
def es_perfecto(numero):
    suma_divisores = sum([i for i in range(1, numero) if numero % i == 0])
    return suma_divisores == numero

# Función para convertir un número a binario
def decimal_a_binario(numero):
    return bin(numero)[2:]

# Pedir al usuario un número
numero = int(input("Ingresa un número entero positivo: "))

# Calcular el factorial
factorial = calcular_factorial(numero)
print(f"Factorial de {numero}: {factorial}")

# Verificar si es primo
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

# Verificar si es perfecto
if es_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")

# Convertir a binario
binario = decimal_a_binario(numero)
print(f"{numero} en binario: {binario}")