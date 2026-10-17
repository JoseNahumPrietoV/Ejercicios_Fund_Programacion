Algoritmo Triangulo
    Definir a, b, c Como Entero;
    
    Escribir "Ingrese el primer ángulo: ";
    Leer a;
    Escribir "Ingrese el segundo ángulo: ";
    Leer b;
    Escribir "Ingrese el tercer ángulo: ";
    Leer c;
    
    // Verificar que la suma de los ángulos sea 180
    Si (a + b + c <> 180) Entonces
        Escribir "Error";
    Sino
        Si (a = b Y b = c) Entonces
            Escribir "Equilátero";
        Sino
            Si ((a = b Y b <> c) O (b = c Y c <> a) O (a = c Y c <> b)) Entonces
                Escribir "Isósceles";
            Sino
                Escribir "Escaleno";
            FinSi
        FinSi
    FinSi
FinAlgoritmo