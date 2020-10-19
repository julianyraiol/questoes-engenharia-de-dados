def median(array):
    size = len(array)
    if size % 2 == 1:
        middle = size // 2
        return array[middle]
    else:
        middle = size // 2
        return (array[middle - 1] + array[middle]) / 2


def read_file():

    try:
        numbers = []
        with open('in.txt', 'r') as file_in:
            contents = file_in.read()
            numbers += [int(x) for x in contents.split()]
        return numbers
    except:
        raise Exception('Não foi possível processar mediana')


if __name__ == "__main__":
    array = read_file()
    array.sort()
    print("A mediana desse conjunto de dados é: ", median(array))
