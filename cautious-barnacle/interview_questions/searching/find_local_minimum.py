# A[0] >= A[1]
# A[n-2] <= A[n-1]
# local minimum ((A[i] <= A[i+1]) and (A[i] <= A[-1]))


def is_local_minimum(input, left_pointer, middle_pointer, right_pointer):
    result = False
    if input[middle_pointer] <= input[left_pointer] and input[middle_pointer] <= input[right_pointer]:
        result = True
    return result


def is_valid_index(input, index):
    result = False
    if index <= len(input) or index >= 0:
        result = True

    return result


def find_local_minimum(input):
    left_pointer = 0
    middle_pointer = left_pointer + 1
    right_pointer = middle_pointer + 1
    result = -1  # return the index of the local minimum

    while is_valid_index(input, left_pointer) and is_valid_index(input, middle_pointer) and is_valid_index(input, right_pointer):
        if is_local_minimum(input, left_pointer, middle_pointer, right_pointer):
            result = middle_pointer
            break
        else:
            left_pointer += 1
            middle_pointer += 1
            right_pointer += 1

    return result


input = [2, 4, 43, 45, 45, 203]
print find_local_minimum(input)
