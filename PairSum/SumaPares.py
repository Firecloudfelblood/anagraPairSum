def suma_pares(arr, k):
    cardinalidad = 0
    container = []
    for num in arr:
        for i in range(arr.index(num) + 1, len(arr), 1):
            if num + arr[i] == k and not [num, arr[i]] in container:
                cardinalidad += 1
                container.append([num, arr[i]])
    return cardinalidad
