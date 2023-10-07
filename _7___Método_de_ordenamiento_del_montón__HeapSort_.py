def heapify(arr, n, i):
    largest = i  # Inicializamos el nodo raíz como el más grande
    left_child = 2 * i + 1  # Índice del hijo izquierdo
    right_child = 2 * i + 2  # Índice del hijo derecho

    # Comparamos el nodo raíz con el hijo izquierdo
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Comparamos el nodo raíz con el hijo derecho
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Si el nodo raíz no es el más grande, lo intercambiamos con el más grande
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Llamamos recursivamente a heapify en el subárbol afectado
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construimos un montón máximo (heap) a partir de la lista desordenada
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraemos elementos uno por uno del montón y los colocamos al final de la lista
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiamos el elemento más grande con el último
        heapify(arr, i, 0)  # Llamamos a heapify en el montón reducido

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de números desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenadacon heap:")
    print(unsorted_list)
    
    # Llamamos a la función de ordenamiento HeapSort
    heap_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("\nLista ordenada con heap:")
    print(unsorted_list)

