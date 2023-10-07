def cocktail_sort(arr):
    n = len(arr)
    swapped = True

    # Inicializamos las variables de l�mites superior e inferior
    start = 0
    end = n - 1

    while (swapped == True):
        # Reseteamos la bandera de intercambio en cada pasada
        swapped = False

        # Bucle de izquierda a derecha (similar al ordenamiento de burbuja)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Si no se realiz� ning�n intercambio, la lista est� ordenada
        if swapped == False:
            break

        # Actualizamos el l�mite superior, ya que el elemento m�s grande est� en su lugar
        end = end - 1

        # Bucle de derecha a izquierda
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Actualizamos el l�mite inferior, ya que el elemento m�s peque�o est� en su lugar
        start = start + 1

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de n�meros desordenados
    unsorted_list = [64, 25, 12, 22, 11]
    
    # Imprimimos la lista desordenada
    print("Lista desordenada con cocktail:")
    print(unsorted_list)
    
    # Llamamos a la funci�n de ordenamiento Cocktail Sort
    cocktail_sort(unsorted_list)
    
    # Imprimimos la lista ordenada
    print("\nLista ordenada con cocktail:")
    print(unsorted_list)

