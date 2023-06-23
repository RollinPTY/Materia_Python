#Calculo de áreasa geométricas
# Libreria
from math import pi

print("CÁLCULO DE ÁREAS GEOMÉTRICAS")
print("1. Área de un cuadrado")
lado = int(input("Escribe el valor del lado del cuadrado:"))
area = lado**2
print('Áreas del cuadrado : %6d'% area)

print("2. Área de un rectángulo")
base = int(input("Escribe el valor de la base: "))
altura = int(input("Escribe el valor de la altura: "))
area = base * altura
print('Área del rectángulo: %6d'% area)

print("3.  Área de un triángulo")
base = int(input("Escribe el valor de la base: "))
altura = int(input("Escribe el valor de la altura: "))
area = (base * altura)/2
print('Área del triángulo: %6.2f'% area)


print("4. Área de un rombo")
dmayor = int(input("Diagonal Mayor: "))
dmenor = int(input("Diagonal Menor: "))
area = (dmayor * dmenor)/2
print('Área del rombo: %6.2f'% area)

print("5. Área de un circulo")
r= float(input("Escriba el radio: "))
area = pi*r**2
print('Área del círculo: %6.2f'% area)