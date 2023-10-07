def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3  # Factor de reducción del espacio

    swapped = True  # Bandera para controlar si se realizó algún intercambio

    while gap > 1 or swapped:
        # Calculamos el espacio (gap) y nos aseguramos de que sea al menos 1
        gap = max(1, int(gap / shrink_factor))
        swapped = False  # Reiniciamos la bandera de intercambio

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]  # Intercambiamos los elementos
                swapped = True  # Se realizó un intercambio

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de números desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenada con comb:")
    print(unsorted_list)
    
    # Llamamos a la función de ordenamiento Comb Sort
    comb_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("\nLista ordenada con comb:")
    print(unsorted_list)

