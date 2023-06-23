# Escriba un programa que almacene la cadena de caracteres Pa$$w0rd en una variable, y le pregunte al usuario por esta contraseña hasta que introduzca la contraseña correcta.

password = "Pa$$w0rd"
string = ''

while string != password:
    string = str(input("Ingrese la contraseña requerida: "))
    if string == password:
        print("\nContraseña correcta.")
    else:
        print("\nContraseña incorrecta, vuelva a intentar.")
        
        

