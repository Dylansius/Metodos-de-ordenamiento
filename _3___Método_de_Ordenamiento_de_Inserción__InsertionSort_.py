def insertion_sort(arr):
    # Iteramos a trav�s de toda la lista, comenzando desde el segundo elemento (�ndice 1)
    for i in range(1, len(arr)):
        # Guardamos el valor actual para su posterior inserci�n
        current_value = arr[i]
        position = i
        
        # Comparamos el valor actual con los elementos anteriores
        # y desplazamos los elementos mayores hacia la derecha
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        
        # Insertamos el valor actual en la posici�n correcta
        arr[position] = current_value

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de n�meros desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la parte desordenada de la lista antes de ordenarla
    print("Parte desordenada con inserccion de la lista:")
    print(unsorted_list[:])  # Imprimimos toda la lista
    
    # Llamamos a la funci�n de ordenamiento de inserci�n
    insertion_sort(unsorted_list)
    
    # Imprimimos la parte ordenada de la lista despu�s de ordenarla
    print("\nParte ordenada con inserccion de la lista:")
    print(unsorted_list)



