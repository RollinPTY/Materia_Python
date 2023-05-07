#se utiliza para elegir un movimiento aleatoria de la máquina
import random

# el tablero de manera inicial
tablero = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

# dibuja el tablero
def DisplayBoard(tablero):
    #ejecuta el tablero fila por fila y así completa el cuadro 3x3
    print("+-------+-------+-------+")
    for fila in range(3): # 0,1,2
        print("|       |       |       |")
        print(f"|   {tablero[fila][0]}   |   {tablero[fila][1]}   |   {tablero[fila][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Ingresar el movimiento del usuario
def EnterMove(tablero):
    # preguntar el siguiente movimiento
    while True:
        move = (input("Ingresa tu próximo movimiento: "))
        if move.isnumeric: #Confirma de que sea numérico
            move = int(move) # lo convierte a enterio
            if move >=1 and move<=9: # pregunta si el movimiento está entre los movimientso válidos
                columna = (move - 1) % 3 # en la columna = move -1 por se empieza por 0,1,2
                if move >=1 and move<=3: # se asigna la fila
                    fila = 0
                elif move == 4 or move == 6:
                    fila = 1
                elif move >=7 and  move <=9:
                    fila = 2
            # verifica que el moviento del usuario, no esté ocupado
            if tablero[fila][columna] != "X" and tablero[fila][columna] != "0":
                tablero[fila][columna] = "0"
                return
        print(f"Movimiento incorrecto, {move} ya está ocuapado.")

# hace una lista de los espacios vacios
def MakeListOfFreeFields(tablero):
    cuadroVacio = [] # se crea una lista vacia
    for i in range(3):
        for j in range(3):
            if tablero[i][j] != "X" and tablero[i][j] != "0": # si no está ocupada por X o 0
                cuadroVacio.append((i,j)) # almacena los espacios vacios en la lista 
    print("Los espacios vacíos son: " , cuadroVacio)
    return cuadroVacio

#verifica si alguien ganó
def VictoryFor(tablero):
    # son las formas posibles de ganar
    Victory = (
    #Horizontal
    [(0, 0), (0, 1), (0, 2)], 
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    #Vertical
    [(0, 0), (1, 0), (2, 0)], 
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    #diagonal
    [(0, 0), (1, 1), (2, 2)], 
    [(0, 2), (1, 1), (2, 0)],
    )
    # verifica las posiciones de las X y 0, para saber si ha ganado
    for indexes in Victory:
        row = [tablero[r][c] for r, c in indexes]
        if all(x == "X" for x in row):
            return "X"
        if all(x == "0" for x in row):
            return "0"
        
# movimiento de la máquina
def DrawMove(tablero):
    movMaq = MakeListOfFreeFields(tablero) #almacena las posiciones libres
    if len(movMaq)>=1: # verifica que hayan movimientos disponibles
        movimiento = random.choice(movMaq) # elige un elemento aleatorio (n,m)
        fila = movimiento[0] #asigna n a fila
        columna = movimiento[1] # asigna m a columna
        tablero[fila][columna] = "X" # asigna X a la posicion n,m
    

# funcion Main, donde se ejecuta todo el programa, en el orden solicitado
def Main():
    nombre = input("Ingresa tu nombre: ")
    #imprime el tablero
    DisplayBoard(tablero)
    while True:
        EnterMove(tablero) # ingresa el movimiento el usuario
        DisplayBoard(tablero) # imprime el tablero con los cambios
        MakeListOfFreeFields(tablero) # crea la lista de los espacios vacios

        if VictoryFor(tablero): # verifica si Usuario ganó
            print(f"¡ {nombre} Has Ganado!")
            break
        
        DrawMove(tablero)# sino, hace el movimiento la maquina
        DisplayBoard(tablero) # imprime el tablero con los cambios

        if VictoryFor(tablero): # verifica si la maquina gano
            print("La máquina ha ganado")
            DisplayBoard(tablero) # imprime el tablero con los cambios
            break
        
        # verifica si hay empate
        if len(MakeListOfFreeFields(tablero)) == 0:
            print("Es empate, no hay más movimientos disponibles")
            break
        

Main()