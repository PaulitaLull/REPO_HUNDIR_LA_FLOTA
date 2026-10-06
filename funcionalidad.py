#%pip install numpy
import numpy as np

def crear_tablero():
 lista_longs_barcos=[2,2,2,3,3,4]
 tablero= np.full((10,10), '-')
 for i in lista_longs_barcos:
       tablero=crear_barcos(tablero, i)
 return tablero

def crear_barcos(tablero, longitud_barco):
    # Esta funcion crea un barco de long x y hace el while hasta que consigue colocarlo
    while True:
        barco=[]
        horizontal=np.random.rand()<0.5
        if horizontal==True:
            fila=np.random.randint(0,10)
            #Creamos una col aleatoria, forzando a que sea de 0 al 7 NO ICLUIDO para que el barco de 4 posiciones quepa
            col=np.random.randint(0,10-(longitud_barco-1))
            for i in range(longitud_barco):
                barco.append([fila, col+i])
        else: #Booleano False (orientacion vertical)
            # Creamos una FILA aleatoria forzando a que sea de 0 a 7 NO ICLUIDO para que el barco de 4 posiciones quepa
            col=np.random.randint(0,10)
            fila=np.random.randint(0,10-(longitud_barco-1))
            for i in range(longitud_barco):
                barco.append([fila+i, col])

        # Reviso si barco cabe. Si no cabe, sale del for y vuelve a empezar el while de crear el barco para la long dada
        libre=True
        for j,k in barco:
            if tablero[j,k]=="O" or tablero[j,k]=="X":
               libre=False
               break
        if libre:
           for fila, columna in barco:
               tablero[fila, columna] = "O"
           break
    return tablero



def dispara_usuario(casilla, tablero_real, tablero_mostrar):
   if tablero_real[casilla[0],casilla[1]]=="O": #tocado
      tablero_real[casilla[0],casilla[1]]="X"
      tablero_mostrar[casilla[0],casilla[1]]="X"
      print(f" Tu disparo ha dado a un barco, ENHORABUENA!: ")
   elif tablero_real[casilla[0],casilla[1]]=="-": #agua
      tablero_real[casilla[0],casilla[1]]="A"
      tablero_mostrar[casilla[0],casilla[1]]="A"
      print(f" Tu disparo ha dado al agua: ")
   else:
      print("Ya disparaste aquí, lo siento:(")

   print(tablero_mostrar)

def dispara_IA(tablero_usuario):
   fila=np.random.randint(0,10)
   columna=np.random.randint(0,10)
   while tablero_usuario[fila,columna]== "X" or tablero_usuario[fila,columna]== "A":
      fila=np.random.randint(0,10)
      columna=np.random.randint(0,10)
   if tablero_usuario[fila,columna]=="O": 
      tablero_usuario[fila, columna]="X"   #tocado
      print(f"La IA ha tocado a tu barco con su disparo: ")
   elif tablero_usuario[fila, columna]=="-": 
      tablero_usuario[fila, columna]="A"  #agua
      print(f"La IA ha dado al agua con su disparo: ")

   print(tablero_usuario)