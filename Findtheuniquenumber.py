def encontrar_unico(arr):
    num_unico = [num for num in arr if arr.count(num) == 1][0]

    return num_unico
