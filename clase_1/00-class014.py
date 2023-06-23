number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el segundo número: "))


larger_number = number1

if number2 > larger_number:
    larger_number = number2

if number3 > larger_number:
    larger_number = number2

print("El número más grande es:", larger_number)