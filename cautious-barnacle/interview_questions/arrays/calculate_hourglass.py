def hourglassSum(arr):
    current_maximum = -9 * 7

    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[i])-2):
            current_maximum = max(
                calculate_hourglass((i, j), arr, current_maximum), current_maximum)

    return current_maximum


def calculate_hourglass(index, matrix, current_maximum):
    positions = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]
    hourglass_sum = 0

    for position in positions:
        y = index[0] + position[0]
        x = index[1] + position[1]

        hourglass_sum += matrix[y][x]

    return hourglass_sum


a = [1, 1, 0, 0, 0, ]
b = [1, 1, 1, 0, 0, 0]
c = [0, 0, 2, 4, 4, 0]
d = [0, 0, 0, 2, 0, 0]
e = [0, 0, 1, 2, 4, 0]
matrix = []
matrix.append(a)
matrix.append(b)
matrix.append(c)
matrix.append(d)
matrix.append(e)

print(hourglassSum(matrix))
