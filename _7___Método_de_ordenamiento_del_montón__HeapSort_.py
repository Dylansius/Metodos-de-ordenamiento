def heapify(arr, n, i):
    largest = i  # Inicializamos el nodo ra�z como el m�s grande
    left_child = 2 * i + 1  # �ndice del hijo izquierdo
    right_child = 2 * i + 2  # �ndice del hijo derecho

    # Comparamos el nodo ra�z con el hijo izquierdo
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Comparamos el nodo ra�z con el hijo derecho
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Si el nodo ra�z no es el m�s grande, lo intercambiamos con el m�s grande
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Llamamos recursivamente a heapify en el sub�rbol afectado
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construimos un mont�n m�ximo (heap) a partir de la lista desordenada
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraemos elementos uno por uno del mont�n y los colocamos al final de la lista
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiamos el elemento m�s grande con el �ltimo
        heapify(arr, i, 0)  # Llamamos a heapify en el mont�n reducido

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de n�meros desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenadacon heap:")
    print(unsorted_list)
    
    # Llamamos a la funci�n de ordenamiento HeapSort
    heap_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("\nLista ordenada con heap:")
    print(unsorted_list)

