def find_occurance_of_key_in_sorted_array(input, key, FIRST, LAST):
    left_pointer = 0
    right_pointer = len(input) - 1
    result = -1

    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2
        if input[middle_pointer] > key:
            right_pointer = middle_pointer - 1
        elif input[middle_pointer] == key:
            result = middle_pointer
            if FIRST:
                right_pointer = middle_pointer - 1  # keep searching left
            if LAST:
                left_pointer = middle_pointer + 1  # Keep searching right
        else:  # input[middle_pointer] < key
            left_pointer = middle_pointer + 1

    return result


def find_enclosing_interval(input, key):
    first_occurance = -1
    last_occurance = -1

    first_occurance = find_occurance_of_key_in_sorted_array(
        input, key, True, False)
    last_occurance = find_occurance_of_key_in_sorted_array(
        input, key, False, True)

    return (first_occurance, last_occurance)


input = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13]
key = 11
print find_enclosing_interval(input, key)
