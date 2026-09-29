# Programa: Clasificación de triángulos según sus ángulos

# Leer los tres ángulos
a = int(input("Ingrese el primer ángulo: ")) 
b = int(input("Ingrese el segundo ángulo: "))
c = int(input("Ingrese el tercer ángulo: "))

# Verificar que la suma sea igual a 180
if a + b + c != 180:
    print("Error no es ningun tipo de Triangulo")
else:
    if a == b and b == c:
        print("Equilátero")
    elif (a == b and b != c) or (b == c and c != a) or (a == c and c != b):
        print("Isósceles")
    else:
        print("Escaleno")
