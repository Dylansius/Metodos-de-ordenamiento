def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializamos el espacio (gap) en la mitad de la longitud de la lista
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Realizamos la inserci�n de forma similar al algoritmo de inserci�n
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reducimos a la mitad el espacio en cada iteraci�n

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de n�meros desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenada con shell:")
    print(unsorted_list)
    
    # Llamamos a la funci�n de ordenamiento Shell
    shell_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("\nLista ordenada con shell:")
    print(unsorted_list)