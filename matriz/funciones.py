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

def ordenar_lista(lista:list[dict], valor:str, ascendente:bool):
    '''
    recibo la lista con los diccionarios un valor que sera el criterio a ordenar y el ascendente se recorrer la lista la cantidad de de elemntos de la lista recorre  con el primer for la cantidad de veces que lo hara el segundo  es para recorrer las posiciones lo siguinte es la parte que ordenadara mediante la psocion y la clave compara el elemento con el que esta despues de el si es ascendente intercambia los valores derecha  izq

    '''
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if ascendente :
                    if lista[j][valor] > lista[j+1][valor]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
                    if lista[j][valor] < lista[j+1][valor]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista
def suma_diagonales(matriz):
    suma_principal = 0
    suma_secundaria = 0
    # Tu código aquí
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0])):
            if i == j:
                suma_principal+= matriz [i][j]
    return suma_principal, suma_secundaria
def determinar_diagonal2(matriz:list):
    diagonal2 = " "# str
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i+j == len( matriz[0])-1:
                diagonal2 += matriz[i][j]
    return diagonal2
matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

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
 #inicio
#map
#map es recibi una funcion lambda que es el criterio, 2  la direcion de elementos que voy a iterar
lista_numeros = [33,2,2,2,2,1]
lista_modificada = []
for numero in lista_numeros:
    doble= numero*2
    lista_modificada.append(doble)
    
# lo mismo  de arriba pero con map
# ejemplo de map:
# le pasamos list osea la connvertimos a lista para que no nnos delvuelva el objecto map osea 0xxxx22

lista = list(map(lambda numero:numero*2,lista_numeros))
print(lista)





lista_numeros[1,2,3,4,56,7,8,9,10]
pares=[]
for numero in lista_numeros:
    if numero %2 ==0:
        pares.append(numero)

#filter filtra una lista recorre  cada elemento de la lista
#convierto a lista para delvolver una lista con 

pares=list(filter(lambda numero: numero %2==0,lista_numeros))
print(pares)
# ejemplo de filter, como funciona
def my_filter(criterio,lista):
    filtrada=[0]
    for elemento in lista:
        if criterio(elemento):# si delvolvio true
            filtrada.append(elemento)
    return filtrada
pares= my_filter(lambda numero : numero%2 == 0, lista_numeros)

 