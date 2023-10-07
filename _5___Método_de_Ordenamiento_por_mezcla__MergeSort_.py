def merge_sort(arr):
    if len(arr) > 1:
        # Dividir la lista en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamada recursiva para ordenar ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializar índices para recorrer las dos mitades y el índice principal
        i = j = k = 0

        # Fusionar las dos mitades en una lista ordenada
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Comprobar si quedan elementos sin fusionar en ambas mitades
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de números desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenada con merge:")
    print(unsorted_list)
    
    # Llamamos a la función de ordenamiento por mezcla
    merge_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("\nLista ordenada con merge:")
    print(unsorted_list)

