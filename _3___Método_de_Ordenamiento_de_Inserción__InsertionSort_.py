def insertion_sort(arr):
    # Iteramos a través de toda la lista, comenzando desde el segundo elemento (índice 1)
    for i in range(1, len(arr)):
        # Guardamos el valor actual para su posterior inserción
        current_value = arr[i]
        position = i
        
        # Comparamos el valor actual con los elementos anteriores
        # y desplazamos los elementos mayores hacia la derecha
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        
        # Insertamos el valor actual en la posición correcta
        arr[position] = current_value

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de números desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la parte desordenada de la lista antes de ordenarla
    print("Parte desordenada con inserccion de la lista:")
    print(unsorted_list[:])  # Imprimimos toda la lista
    
    # Llamamos a la función de ordenamiento de inserción
    insertion_sort(unsorted_list)
    
    # Imprimimos la parte ordenada de la lista después de ordenarla
    print("\nParte ordenada con inserccion de la lista:")
    print(unsorted_list)



