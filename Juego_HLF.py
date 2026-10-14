#%pip install numpy
import numpy as np
import funcionalidades_HLF as funcionalidad

tablero_usuario, flota_usuario=funcionalidad.crear_tablero()
print(f"TU TABLERO: \n {tablero_usuario} \n")
tablero_IA_real, flota_IA_real=funcionalidad.crear_tablero()
tablero_IA_muestra=np.full((10,10), '-')
print(f"EL TABLERO DE LA IA: \n {tablero_IA_muestra} \n")

while True:
    # Turno del usuario, le pedimos la casilla y la comprobamos
    while True:
        disparo_fila=input("ES TU TURNO: \nDime la fila de la casilla en la que quieres disparar:")
        disparo_fila=funcionalidad.comprobacion_numero(disparo_fila)
        disparo_columna=input("Genial! Ahora dime la columna de la casilla en la que quieres disparar:")
        disparo_columna=funcionalidad.comprobacion_numero(disparo_columna)
        casilla=(disparo_fila, disparo_columna)
        if tablero_IA_real[casilla[0], casilla[1]]=="X" or tablero_IA_real[casilla[0], casilla[1]]=="A":
            print("Ya disparaste aquí anteriormente, te daré otra oportunidad...")
        else:
            break

    # Aplicamos el disparo del usuario y comprobamos si ha ganado:
    funcionalidad.dispara_usuario(casilla, tablero_IA_real, tablero_IA_muestra, flota_IA_real)
    if np.sum(tablero_IA_real=="O")==0:
        print(f"Ganaste la partida, has hundido toda la flota de la IA: {tablero_IA_real}")
        break

    # Aplicamos el disparo de la IA y comprobamos si ha ganado:
    print("ES EL TURNO DE LA IA...")
    funcionalidad.dispara_IA(tablero_usuario, flota_usuario)
    if np.sum(tablero_usuario == "O")==0:
        print(f"La IA ha ganado la partida, ha hundido toda tu flota: {tablero_usuario}")
        break

    print("Pasamos a la siguiente ronda, mucha suerte!!")
    print("------------------------------------------------------------")