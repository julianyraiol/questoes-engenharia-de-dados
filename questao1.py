def median(matriz):
    size = len(matriz)

    if size%2 == 1:
        middle = size//2
        return matriz[middle]
    else:
        middle = size // 2
        return (matriz[middle-1] + matriz[middle])/2


matriz = [1,2,3,4,5,6]
print(median(matriz))
