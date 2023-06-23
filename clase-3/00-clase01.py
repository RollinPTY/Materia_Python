materias = ["Español", "Inglés", "Matemáticas", "Física", "Química", "Historia"]
m_repetir = []
for n in materias:
    nota = int(input(f"Que nota has sacado en {n}: "))
    if nota < 71:
        m_repetir.append(n)
        

print(f"Tienes que repetir {m_repetir}")