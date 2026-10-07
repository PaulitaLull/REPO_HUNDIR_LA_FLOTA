#%pip install numpy
import numpy as np

def crear_tablero():
 lista_longs_barcos=[2,2,2,3,3,4]
 tablero= np.full((10,10), '-')
 for i in lista_longs_barcos:
       tablero, flota=crear_barcos(tablero, i)
 return tablero, flota

def crear_barcos(tablero, longitud_barco):
    # Esta funcion crea un barco de long x y hace el while hasta que consigue colocarlo
    # 1º que no se salga del tablero, 2º que lo coloque donde quepa
    while True:
        barco=[]
        #Flota será la lista de posiciones de todos los barcos
        flota=[]
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
         #Si llega aquí es que el barco cabe, y lo coloca
        if libre:
           for fila, columna in barco:
               tablero[fila, columna] = "O"
           flota=flota.append(barco)
           break
    return tablero, flota



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

def comprobacion_numero(numero):
   while True:
      try:
         numero=int(numero) #convierto "numeros enteros" en ints
         try:
            if numero>9 or numero<0:
               raise ValueError
            break
         except ValueError:
            numero=input("Introdujiste un número fuera del rango, debe ser uno entre del 0 al 9. Inténtalo de nuevo:")
      
      except ValueError: #si es una palabra o un float
            numero=input("Introdujiste una palabra o un número decimal y ha de ser un numero entero del 0 al 9, vuelve a intentarlo:")
   return numero

def todos_hundidos(tablero, flota):
    """Devuelve True si todas las casillas de todos los barcos están tocadas(X)."""
    for barco in flota:
        for fila, col in barco:
            if tablero[fila, col] != "X":
                return False
    return True