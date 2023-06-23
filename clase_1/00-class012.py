km_recorridos = float(input("Inroduzca Km. recorridos: "))
litros_usados = float(input("Introduzca litros de gasolina"))
costo_gasolina = float(input("Costo total del combustible"))
costo_mant = float(input("Costo total de mantenimiento"))



kp1 = km_recorridos / litros_usados

costo_total = costo_gasolina * costo_mant

costo_km = costo_total/km_recorridos

print("Km. recorridos por litro de combustible: ", kp1, "km")
print("Costo total uso vehículo: ", costo_total, "Dólares")
print("Costo por kilómetro: ", costo_km, "Dólares")