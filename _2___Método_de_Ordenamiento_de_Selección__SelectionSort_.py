def selection_sort(arr):
    # Iteramos a trav�s de toda la lista
    for i in range(len(arr)):
        # Suponemos que el elemento actual es el m�nimo
        min_index = i
        
        # Buscamos el m�nimo elemento restante en la lista
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambiamos el elemento actual con el m�nimo encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de n�meros desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenada:")
    print(unsorted_list)
    
    # Llamamos a la funci�n de ordenamiento de selecci�n
    selection_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("Lista ordenada:")
    print(unsorted_list)


