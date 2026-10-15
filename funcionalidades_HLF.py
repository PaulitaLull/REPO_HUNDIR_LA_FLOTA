import numpy as np

def crear_tablero():
 # Devuelve el tablero y la flota
 lista_longs_barcos=[2,2,2,3,3,4]
 tablero= np.full((10,10), '-')
 # Flota: lista de listas, donde cada una contiene todas las posiciones de un barco
 flota=[]
 # Bucle que crea el tablero con los barcos, devolviendo este mismo y la flota completa 
 for i in lista_longs_barcos:
       tablero, flota=crear_barcos(tablero, i, flota)
 return tablero, flota

def crear_barcos(tablero, longitud_barco, flota):
    # Esta funcion crea un barco de long x y hace el while,
    # hasta que consigue colocarlo y añadirlo a la lista de la flota.
    # 1º Mira que el barco no se salga del tablero, 
    # 2º que quepa en su boundary, y 3º lo coloca si procede.
    #Devuelve el tablero y la flota
    while True:
        barco=[]
        horizontal=np.random.rand()<0.5 #Devuelve true/false
        if horizontal==True:
            #Creamos una fila aleatoria hasta el 10 no incluido
            fila=np.random.randint(0,10)
            #Creamos una col aleatoria, forzando a que sea de 0 al 7 NO ICLUIDO 
            #para que el barco de 4 posiciones quepa
            col=np.random.randint(0,10-(longitud_barco-1))
            # Con esa posicion, creo el barco sumando posiciones en la fila
            for i in range(longitud_barco):
                barco.append([fila, col+i])
        else: #Booleano False (orientacion vertical)
            col=np.random.randint(0,10)
            fila=np.random.randint(0,10-(longitud_barco-1))
            for i in range(longitud_barco):
                barco.append([fila+i, col])

        # Reviso si barco cabe dentro de su boundary. 
        # Si no cabe, sale del for y vuelve a empezar el while de crear el barco 
        #para la longitud dada.

        # 1º defino filas y cols max y mins del barco
        fila_min = barco[0][0]
        fila_max = barco[-1][0]
        col_min = barco[0][1]
        col_max = barco[-1][1]

        # 2º ampliamos -1 y +2 para definir el boundary del barco
        # Si da la casualidad que esta en un borde, 
        # ahí el boundary es ese mismo borde (no nos salimos del tablero).
        fila_bound_inicio=fila_min-1
        if fila_bound_inicio < 0:
            fila_bound_inicio = 0

        fila_bound_fin = fila_max + 2  #para luego llegar hasta +1
        if fila_bound_fin > 10:
            fila_bound_fin = 10

        col_bound_inicio = col_min - 1
        if col_bound_inicio < 0:
            col_bound_inicio = 0

        col_bound_fin = col_max + 2
        if col_bound_fin > 10:
            col_bound_fin = 10

        # Comprobamos si en esa zona creada como boundary hay algun barco. 
        # Para ello creamos un sub tablero con la zona boundary y todo su interior:
        zona_bound = tablero[fila_bound_inicio:fila_bound_fin, col_bound_inicio:col_bound_fin]
        
        if "O" in zona_bound:
            libre = False
        else:
            libre = True

        # Si llega aquí es que el barco cabe en su zona boundary, 
        #y por tanto procede a colocarlo en el tablero y añadirlo a la flota.
        if libre:
           for fila, columna in barco:
               tablero[fila, columna] = "O"
           flota.append(barco)
           break
    return tablero, flota



def dispara_usuario(casilla, tablero_real, tablero_mostrar, flota):
   if tablero_real[casilla[0],casilla[1]]=="O": #tocado o hundido
      tablero_real[casilla[0],casilla[1]]="X"
      tablero_mostrar[casilla[0],casilla[1]]="X"
      #Si la función barco hundido devuelve true, barco hundido, sino tocado
      if barco_hundido(casilla[0], casilla[1], tablero_real, flota):
         print("¡HUNDIDO! Has hundido un barco de la IA")
      else:
         print("¡TOCADO! Tu disparo ha tocado a un barco")
   elif tablero_real[casilla[0],casilla[1]]=="-": #agua
      tablero_real[casilla[0],casilla[1]]="A"
      tablero_mostrar[casilla[0],casilla[1]]="A"
      print(f" Tu disparo ha dado al agua: ")
   else:
      print("Ya disparaste aquí, lo siento:(")

   print(tablero_mostrar)

def dispara_IA(tablero_usuario, flota):
   # Selecciona casilla aleatoria
   fila=np.random.randint(0,10)
   columna=np.random.randint(0,10)
   # Mientras la casilla ya halla sido seleccionada, repite la selección aleatoria
   while tablero_usuario[fila,columna]== "X" or tablero_usuario[fila,columna]== "A":
      fila=np.random.randint(0,10)
      columna=np.random.randint(0,10)

   if tablero_usuario[fila,columna]=="O": 
      tablero_usuario[fila, columna]="X"  #tocado o hundido
      #Si la función barco hundido devuelve true, barco hundido, sino tocado
      if barco_hundido(fila, columna, tablero_usuario, flota):
         print("¡La IA ha HUNDIDO uno de tus barcos!")
      else:
         print("La IA ha TOCADO uno de tus barcos")
   elif tablero_usuario[fila, columna]=="-": 
      tablero_usuario[fila, columna]="A"  #agua
      print(f"La IA ha dado al agua con su disparo: ")

   print(tablero_usuario)


def comprobacion_numero(numero):
   while True:
      try:
         # Convierto numeros enteros en ints,
         # si no puede, devuelve mensaje de: introdujiste palabra o float, dame otro input
         numero=int(numero) 
         try:
            # Si entero fuera de rango -> raise error y va al except: dame otro input
            # Si numero correcto, sale del while y devuelve el número
            if numero>9 or numero<0:
               raise ValueError
            break
         except ValueError:
            numero=input("Introdujiste un número fuera del rango, " \
            "debe ser uno entre del 0 al 9. Inténtalo de nuevo:")
      
      except ValueError: #si es una palabra o un float
            numero=input("Introdujiste una palabra o un número decimal " \
            "y ha de ser un numero entero del 0 al 9, vuelve a intentarlo:")
   return numero


def barco_hundido(fila, columna, tablero, flota):
    """Busca el barco al que pertenece la casilla en la lista de barcos flota 
    y devuelve True si todas sus casillas son X."""
    for barco in flota:
        #Si la casilla seleccionada pertenece a barco, revisamos casilla a casilla del barco
        if [fila, columna] in barco:
            for f, c in barco:
                # Si encuentra una no tocada, no está hundido y devuelve false
                if tablero[f, c] != "X":  
                    return False
            # Tras revisar cada casilla del barco, si todas están tocadas, devuelve True
            return True 
    #Si a casilla seleccionada no pertenece a ningún barco, también devuelve false
    return False  