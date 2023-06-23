# Escriba un programa que solicite al usuario un número entero y muestre por pantalla si es par o impar.

n = 0

n = int(input("Ingrese un número entero: "))

if n % 2 == 0:
    print(f"El un número  {n}  par")
else:
    print(f"Es un número  {n} impar")