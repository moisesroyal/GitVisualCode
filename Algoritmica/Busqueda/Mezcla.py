def merge_sort(lista):
    if len(lista) > 1:
        # Divide la lista en 2 sublistas
        izquierda = lista[:len(lista)//2]
        derecha = lista[len(lista)//2:]
        print(izquierda, '*' * 5, derecha)

        # Ordeno cada sublista con recursión
        merge_sort(izquierda)
        merge_sort(derecha)

        # Define los iteradores que van a atravesar la lista izquierda, la derecha y la resultante
        i = 0
        d = 0
        r = 0

        # Compara el primer elemento de cada una de las listas hasta haber atravesado todos los elementos de alguna lista
        while i < len(izquierda) and d < len(derecha):
            if izquierda[i] < derecha[d]:
                lista[r] = izquierda[i]
                i += 1
            else:
                lista[r] = derecha[d]
                d += 1
            r += 1

        # Agrega los elementos restantes de la sublista izquierda (si los hay)
        while i < len(izquierda):
            lista[r] = izquierda[i]
            i += 1
            r += 1

        # Agrega los elementos restantes de la sublista derecha (si los hay)
        while d < len(derecha):
            lista[r] = derecha[d]
            d += 1
            r += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista
