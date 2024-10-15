def suma_diagonales(matriz):
    suma_principal = 0
    suma_secundaria = 0
    # Tu código aquí
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0])):
            if i == j:
             suma_principal+= matriz [i][j]
    return suma_principal, suma_secundaria

def guardar_lista_en_archvo_txt(lista_numeros:list,path):
    cadena =""
    for nombre in lista_numeros:
        cadena+= f"{nombre}\n"
    with open(path,"w") as archivo:
        archivo.write(cadena)
def guardar_matriz_en_archvo_txt(lista_numeros:list,path):
    cadena =""
    for nombre in lista_numeros:
        for j  in nombre:
            cadena+= f"{j}\n"
    with open(path,"w") as archivo:
        archivo.write(cadena)
# Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
# Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
# Menú:
# Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
# Mostrar la recaudación de todos los coches y líneas.
# Calcular y mostrar recaudación por línea.
# Calcular y mostrar recaudación por coche.
# Calcular y mostrar la recaudación total.
# Salir
# Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.

lineas = [
    [101, 102, 103, 104, 105],  # Coches de la línea 1
    [201, 202, 203, 204, 205],  # Coches de la línea 2
    [301, 302, 303, 304, 305]   # Coches de la línea 3
]
guardar_matriz_en_archvo_txt(lineas,"elsds")
legajos = [
    [1234, 5678, 9012, 3456, 7890],
    [2345, 6789, 1235, 5679, 9013],
    [3457, 7891, 2346, 6790, 1236]
]

recaudaciones = [
    [1000, 2000, 2000, 2000, 1000],  # Recaudación de los coches de la línea 1
    [2000, 1900, 1700, 2400, 2300],  # Recaudación de los coches de la línea 2
    [1000, 2200, 2000, 2100, 1950]   # Recaudación de los coches de la línea 3
]
def recaudacion_por_linea(matriz:list):
 if type (matriz)== list:
    m=len(matriz)
    n=len(matriz[0])
    suma_por_linea=[0]*m
    for i in range(m):
        for j in range(n):
         suma_por_linea[i]+= matriz [i][j]
    for i in range(len(suma_por_linea)):
        retorno=print(suma_por_linea[i])
 else:
    retorno=None
    print("error, ingrese una matriz")
 return retorno
print( recaudacion_por_linea(recaudaciones))