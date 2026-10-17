# Programa para verificar si un arreglo está en orden estrictamente creciente

# Leer tamaño del arreglo
N = int(input("Ingrese el tamaño del arreglo: "))

# Leer los elementos del arreglo
array = []
for i in range(N):
    valor = int(input(f"Ingrese el elemento {i+1}: "))
    array.append(valor)

# Verificar si está en orden creciente
aux = True
for i in range(N - 1):  # hasta N-2 para comparar con el siguiente
    if array[i] >= array[i + 1]:
        aux = False
        break

# Mostrar resultado
if aux:
    print("YES")
else:
    print("NO")
