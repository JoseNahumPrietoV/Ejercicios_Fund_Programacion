# Suma gaussiana en Python

# Solicitar un número al usuario
n = int(input("Ingresa un número: "))

# Calcular la suma gaussiana
resultado = n * (n + 1) % 2   # uso // para división entera

# Mostrar el resultado
print("La suma gaussiana es:", resultado)
