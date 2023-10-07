def bubble_sort(arr):
    n = len(arr)
    
    # Iterar a trav�s de todos los elementos de la lista
    for i in range(n):
        
        # �ltimos i elementos ya est�n en su lugar, por lo que no es necesario verificarlos
        for j in range(0, n-i-1):
            
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Lista desordenada
lista_desordenada = [64, 34, 25, 12, 22, 11, 90]

# Imprimir la lista desordenada
print("Lista desordenada:", lista_desordenada)

# Llamar a la funci�n de ordenamiento de burbuja
bubble_sort(lista_desordenada)

# Imprimir la lista ordenada
print("Lista ordenada:", lista_desordenada)



