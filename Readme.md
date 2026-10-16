# 🚢 Hundir la flota

Versión sencilla en Python del clásico juego de hundir la flota. Se juega por consola contra la IA, donde cada jugador tiene un tablero de 10x10 con una flota colocada al azar, y gana quien hunda primero todos los barcos del rival.

## Requisitos

- [NumPy](https://numpy.org/)

```
pip install numpy
```

## Estructura del proyecto

```
- Juego_HLF.py  (Bucle principal de la partida)
- Funcionalidades_HLF.py  (Funciones del juego)
- Readme.md
```

## Cómo jugar

1. Entra en el archivo principal **Juego_HLF.py** y ejecútalo:

2. En tu turno, el juego te pide la **fila** y la **columna** (un número entero del 0 al 9) de la casilla a la que quieres disparar.
3. Después dispara la IA a una casilla aleatoria de tu tablero.
4. Los turnos se alternan hasta que uno de los dos se queda sin barcos.

Si disparas a una casilla en la que ya habías disparado, el juego te deja volver a elegir sin perder el turno.

## Reglas

- El tablero es de **10x10**.
- Cada jugador tiene **6 barcos**: tres de longitud 2, dos de longitud 3 y uno de longitud 4.
- Los barcos se colocan de forma aleatoria, en horizontal o vertical, y **no pueden tocarse entre sí**.
- Al disparar, el juego avisa de si el resultado es **agua**, **tocado** o **hundido**.
- Gana quien hunda toda la flota del rival.

## Símbolos del tablero

| Símbolo | Significado                  |
|---------|------------------------------|
| `-`     | Casilla sin disparar         |
| `O`     | Parte de un barco            |
| `X`     | Barco tocado                 |
| `A`     | Disparo al agua              |

## Funciones principales

| Función | Descripción |
|---------|-------------|
| `crear_tablero()` | Crea un tablero con los 6 barcos colocados al azar y devuelve el ``tablero`` y la `flota` (lista de barcos, cada uno una lista de coordenadas). |
| `crear_barcos(tablero, longitud_barco, flota)` | Coloca un barco de la longitud indicada, repitiendo hasta que cabe dentro del tablero y sin tocar a otros barcos. |
| `dispara_usuario(casilla, tablero_real, tablero_mostrar, flota)` | Aplica el disparo del jugador y avisa de agua, tocado o hundido. |
| `dispara_IA(tablero_usuario, flota)` | Dispara la IA a una casilla aleatoria que no haya probado antes y avisa de agua, tocado o hundido. |
| `comprobacion_numero(numero)` | Valida que la entrada sea un entero entre 0 y 9, y vuelve a pedirla si no lo es. |
| `barco_hundido(fila, columna, tablero, flota)` | Comprueba si el barco al que pertenece la casilla introducida tiene todas sus posiciones tocadas. |

## Posibles mejoras

- IA más inteligente: que tras tocar un barco, dispare a las casillas de alrededor, o que tras hundir un barco descarte todas las casillas colindantes.
- Mostrar los dos tableros uno al lado del otro.
- Permitir al jugador colocar sus propios barcos.
- Modalidad para dos jugadores


