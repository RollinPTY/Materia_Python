# Escriba un programa en el que se solicite una frase y una letra. El programa debe mostrar por pantalla el número de veces que aparece la letra en la frase.


letra = ''
count = 0
letra = str(input("Ingresa una letra: "))
letra = letra.lower()
frase = str(input("Ingresa una frase: "))
frase = frase.lower()
for i in frase:
    if letra == i :
        count += 1

print(f"La letra se repite: {count} veces en la frase ")