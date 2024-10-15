'''
# 1. Crear una función que permita leer cada línea del archivo csv y convertir cada lectura en una matriz de
3X3.
# 2. Crear una función que reciba la matriz anterior y la muestre.
# 3. Crear una función que analice el contenido de la matriz y determine si gano la X, la O o si hubo empate.
# (Tienen que hacer varias funciones para analizar las líneas verticales, horizontales o diagonales).
# Repetir el punto 2 y 3 por cada línea del archivo.
# 4. Antes de finwalizar el programa mostrar las estadísticas:
# Cuántas veces ganó la X
# Cuántas veces ganó la O
# Cuántas veces hubo empate
'''
import re
def parser_csv_(path:str)-> list:
        matriz = []
        matrices =[]
        with open(path,"r",encoding="utf-8") as archivo :
            for  linea in archivo:
                registro = re.split(",|\n",linea.strip())
                matriz.append(registro)
                if len( matriz)== 3:
                    matrices.append(matriz)
                    matriz = []

        return matrices

matriz = parser_csv_("archivo.csv")
# print( matriz)
# print(matriz)}
def imprimir_matriz(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j],end=" ")
        print(" ")
imprimir_matriz(matriz[0])        
# for fila in range(len(matriz)):  # Recorre las filas
#     # print(matriz[fila])
#     for j in range(len(matriz[fila])):  # Recorre las columnas de la fila actual
#         for x in range(len(matriz[fila][j])):
#             print(matriz[fila][j][x],end=" ")
#         print("")
            

matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def determinar_vertical(matriz:list):
    lista = [""]* len(matriz[0])
    # lista =[]
    suma =0
    for i in range(len(matriz[0])):
        suma_vertical = ""
        for j in range(len(matriz)):
            suma =i+j

            # suma_vertical += matriz[j][i]
            lista[i]+= matriz[j][i]
        
        # lista.append(suma_vertical)
    # return lista    
        
# print(determinar_vertical(matriz))          

def determinar_diagonal1(matriz:list[list]):
    diagonal1 = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i ==j:
                diagonal1 += matriz[i][j]
    

    return diagonal1
def determinar_diagonal2(matriz:list):
    diagonal2 = " "
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i+j == len( matriz[0])-1:
                diagonal2 += matriz[i][j]
    return diagonal2
    
# print(determinar_diagonal2(matriz))
suma_horizontal= 0
lista = []
lista_2= []
diagonal1=0
diagonal2 = 0

for fila in range(len(matriz2)):  # Recorre las filas
    suma_horizontal = 0
    suma_vertical=0
    for j in range(len(matriz2[fila])):  # Recorre las columnas de la fila actual
        suma_horizontal+= matriz2[fila][j]
        suma_vertical+=matriz2[j][fila]
        if fila == j :
            diagonal1 +=  matriz2[fila][j]
        if fila + j == len(matriz2)-1:
                diagonal2 +=  matriz2[fila][j]
                # print(diagonal2)


    lista_2.append(suma_vertical)
    lista.append(suma_horizontal)
def imprimir_matriz(matriz:list[list]):
    for fila in matriz:
        
        for columna in fila:
            
            print(f"{columna}",end= " ")
        
        print("")
#imprimir_matriz(matriz)
def vertical(matriz:list):
    pass


def determinar_operacion(matriz:list):

   contador_x = 0
   contador_o = 0
   lista_resultado =[]

   for filas in matriz:
        for columnas in filas:
            
            if matriz[filas][columnas] == "x" :
                
                contador_x += 1
            elif matriz[filas][columnas] == "o":
                
                contador_o += 1
    
        lista_resultado = [contador_o, contador_x]
motrar_comptibilidad =34
def comprobacion( lista:list, elemento, elemento_2):
 
        contador = 0
        contador_2 = 0
        lista = []

        for i in lista:
     
         if i == elemento :
       
            contador  +=1 
         elif i == elemento_2:
      
            contador_2+=1
            lista = [ contador,contador_2]

        return lista

def lineas_verticales( matriz:list):
    
    
    lista_1 = []
    lista_2 = []
    lista_3 = []
    contador_o = 0
    contador_x = 0
    posicion = 0
    for  i in range(matriz):
        
        columnas_1 = matriz[i][0] 
        lista_1.append( columnas_1)
        columnas_2 = matriz[i][1]
        columnas_3 = matriz[i][2]
        lista_2.append( columnas_2)
        lista_3.append( columnas_3)
    
    comprobar_1 = comprobacion (lista_1,"x","o")
    comprobar_2 = comprobacion (lista_2,"x","o")
    comprobar_3 = comprobacion (lista_3,"x","o")
    contador_o = comprobar_1[0]+ comprobar_2[0] +comprobar_3[0]
    contador_X = comprobar_1[1]+ comprobar_2[1] +comprobar_3[1]

def diagonales( matriz:list):
    posicion = 0
    lista = []
    for i in range(len( matriz)):

      for j in range( len(i)):

          diagonal  = matriz [i][posicion]
          posicion += 1
          lista.append(diagonal)

    return lista
          

