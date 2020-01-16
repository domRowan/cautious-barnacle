def arrayManipulation(n, queries):
    output = [0] * n
    current_max = 0

    for query in queries:
        start_pointer = query[0] - 1
        end_pointer = query[1]
        value = query[2]

        for i in range(start_pointer, end_pointer):
            output[i] += value
            if output[i] > current_max:
                current_max = output[i]

    return current_max
