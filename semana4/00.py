# 1. Escriba una función en Python que sume todos los números en una lista. 
lista = ()

def Suma(lista):
    sum = 0
    for n in lista:
        sum = sum + n

    print(f"La suma de los elementos de la lista es: {sum}")

lista = (1,2,3,4,5)
Suma(lista)