# Escribir un programa que solicite al usuario su peso (en libras) y estatura (en metros), calcule el índice de masa corporal 
# y almacénelo en una variable, e imprima por pantalla la frase "Su índice de masa corporal es <imc>" donde <imc> es el índice
# de masa corporal calculado redondeado con un decimal. 

# ¿Cuál es su peso en libras? 200
# ¿Cuál es su estatura en metros? 1.75

# Su peso equivale a 91 kilogramos
# Su estatura es 1.75 metros

# Su índice de masa corporal es 29.7

print("Bienvenido \n")


peso = float(input("¿Cuál es su peso en libras? "))
estatura = float(input("¿Cuál es su estatura en metros? "))

#round(number, digits)

peso = peso/2.2
round(peso, 2)

imc = peso/(estatura**2)


print(f'\nSu peso equivale a {round(peso)} kilogramos')
print(f'Su estatura es {round(estatura,2)} metros')
print(f'Su índice de masa corporal es {round(imc,1)} ')