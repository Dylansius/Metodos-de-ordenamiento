def quick_sort(arr):
    # Caso base: Si la lista tiene 0 o 1 elemento, está ordenada por definición
    if len(arr) <= 1:
        return arr
    
    # Elegimos un elemento como pivote (en este caso, el último elemento)
    pivot = arr[-1]
    
    # Inicializamos listas para los elementos menores y mayores que el pivote
    lesser = []
    greater = []
    
    # Recorremos la lista, comparando cada elemento con el pivote
    for element in arr[:-1]:
        if element <= pivot:
            lesser.append(element)
        else:
            greater.append(element)
    
    # Llamamos recursivamente a quick_sort para las listas menores y mayores
    sorted_lesser = quick_sort(lesser)
    sorted_greater = quick_sort(greater)
    
    # Combinamos las listas menores, el pivote y las listas mayores para obtener la lista ordenada
    sorted_arr = sorted_lesser + [pivot] + sorted_greater
    
    return sorted_arr

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de números desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenada con quick:")
    print(unsorted_list)
    
    # Llamamos a la función de ordenamiento QuickSort
    sorted_list = quick_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("\nLista ordenada con quick:")
    print(sorted_list)

