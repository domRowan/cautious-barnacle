def minimumSwaps(arr):
    sorted_input = sorted(arr)
    index_by_value = {}
    number_of_swaps = 0

    for i in range(len(arr)):
        index_by_value[arr[i]] = i

    for i in range(len(arr)):
        if arr[i] != sorted_input[i]:

            index_to_swap = index_by_value[sorted_input[i]]
            index_by_value[arr[i]] = index_by_value[sorted_input[i]]
            arr[i], arr[index_to_swap] = sorted_input[i], arr[i]

            number_of_swaps += 1
    return number_of_swaps


input = [4, 3, 1, 2]
print minimumSwaps(input)
