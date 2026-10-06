#%pip install numpy
import numpy as np
import funcionalidad

tablero_usuario=funcionalidad.crear_tablero()
print(f"TU TABLERO SECRETO: \n {tablero_usuario} \n")
tablero_IA_real=funcionalidad.crear_tablero()
tablero_IA_muestra=np.full((10,10), '-')
print(f"EL TABLERO DE LA IA: \n {tablero_IA_muestra} \n")

while True:
    # Turno del usuario, le pedimos la casilla
    disparo_fila=int(input("ES TU TURNO: \nDime la fila de la casilla en la que quieres disparar:"))
    while disparo_fila> 9 or disparo_fila<0:
        disparo_fila=int(input("Introdujiste una fila incorrecta, debe ser un entero del 0 al 9. Inténtalo de nuevo:"))

    disparo_columna=int(input("Genial! Ahora dime la columna de la casilla en la que quieres disparar:"))
    while disparo_columna> 9 or disparo_columna<0:
        disparo_columna=int(input("Introdujiste una columna incorrecta, debe ser un entero del 0 al 9. Inténtalo de nuevo:"))
    
    casilla=(disparo_fila, disparo_columna)

    # Aplicamos el disparo del usuario y comprobamos si ha ganado:
    funcionalidad.dispara_usuario(casilla, tablero_IA_real, tablero_IA_muestra)
    if tablero_IA_real.sum("O")==16:
        print(f"Ganaste la partida, has hundido toda la flota de la IA: {tablero_IA_real}")
        break

    # Aplicamos el disparo de la IA y comprobamos si ha ganado:
    print("Es el turno de la IA:")
    funcionalidad.dispara_IA(tablero_usuario)
    if tablero_usuario.sum("O")==16:
        print(f"La IA ha ganado la partida, ha hundido toda tu flota: {tablero_usuario}")
        break

    print("Pasamos a la siguiente ronda, mucha suerte!!")
    print("------------------------------------------------------------")