def find_first_occurance_of_element_greater_than_key(input, key):
    left_pointer = 0
    right_pointer = len(input) - 1
    result = -1

    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2

        if input[middle_pointer] < key:
            left_pointer = middle_pointer + 1
        elif input[middle_pointer] == key:
            right_pointer = middle_pointer - 1
            result = middle_pointer + 1
        else:  # input[middle_pointer] > key
            right_pointer = middle_pointer - 1
    return result


input = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
key = 108

print find_first_occurance_of_element_greater_than_key(input, key)
