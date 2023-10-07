def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3  # Factor de reducci�n del espacio

    swapped = True  # Bandera para controlar si se realiz� alg�n intercambio

    while gap > 1 or swapped:
        # Calculamos el espacio (gap) y nos aseguramos de que sea al menos 1
        gap = max(1, int(gap / shrink_factor))
        swapped = False  # Reiniciamos la bandera de intercambio

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]  # Intercambiamos los elementos
                swapped = True  # Se realiz� un intercambio

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de n�meros desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenada con comb:")
    print(unsorted_list)
    
    # Llamamos a la funci�n de ordenamiento Comb Sort
    comb_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("\nLista ordenada con comb:")
    print(unsorted_list)

