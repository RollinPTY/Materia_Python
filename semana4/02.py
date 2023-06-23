# 3. Escriba una clase en Python que convierta un entero a un romano romano.

class aRomano:
    def __init__(self):
        self.nRomano = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}


    def toRoman(self, n):    
        
        resultado = ''

        for romano, entero in self.nRomano.items():
            while n >= romano:
                resultado += entero
                n -= romano
        
        return resultado

numero = 29
ejecuta = aRomano()
roman = ejecuta.toRoman(numero)
print(f"Entero: {numero}")
print(f"Romano: {roman}")



# class Convertir_a_Romano:
#     def diccionario():
#         nRomano = (('I', 1), ('IV', 4),('V', 5),('IX', 9),('X', 10),('XL', 40),('L', 50), ('XC', 90), ('C', 100),('CD', 400),('D', 500),('CM', 900), ('M', 1000) )

