def merge_sort(input):
    input_length = len(input)

    if input_length > 1:
        middle_pointer = input_length // 2
        lhs = merge_sort(input[:middle_pointer])
        rhs = merge_sort(input[middle_pointer:])

        lhs_pointer = 0
        rhs_pointer = 0
        input_pointer = 0
        lhs_length = len(lhs)
        rhs_length = len(rhs)

        while lhs_pointer < lhs_length and rhs_pointer < rhs_length:
            if lhs[lhs_pointer] < rhs[rhs_pointer]:
                input[input_pointer] = lhs[lhs_pointer]
                lhs_pointer += 1
            else:
                input[input_pointer] = rhs[rhs_pointer]
                rhs_pointer += 1
            input_pointer += 1

        while lhs_pointer < lhs_length:
            input[input_pointer] = lhs[lhs_pointer]
            lhs_pointer += 1
            input_pointer += 1

        while rhs_pointer < rhs_length:
            input[input_pointer] = rhs[rhs_pointer]
            rhs_pointer += 1
            input_pointer += 1

    return input


input = [3, 56, 7, 3, 547, 12, 6, 78, 12, 4]
print merge_sort(input)
