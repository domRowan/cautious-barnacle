def find_prefix_in_strings(input, prefix):
    first_occurance = find_occurance_of_letter(input, prefix, True, False)
    last_occurance = find_occurance_of_letter(input, prefix, False, True)

    return (first_occurance, last_occurance)


def find_occurance_of_letter(input, prefix, FIRST, LAST):
    left_pointer = 0
    right_pointer = len(input) - 1
    result = -1

    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2

        prefix_at_middle_pointer = input[middle_pointer][:len(prefix)]
        if prefix_at_middle_pointer > prefix:
            right_pointer = middle_pointer - 1
        elif prefix_at_middle_pointer == prefix:
            result = middle_pointer
            if FIRST:
                # Continue searching left
                right_pointer = middle_pointer - 1
            if LAST:
                # Continue searching right
                left_pointer = middle_pointer + 1
        else:  # first prefix > prefix
            left_pointer = middle_pointer + 1

    return result


input = ["bar", "baz", "pre-foo", "pre-quux"]

prefix = "pre-"

print find_prefix_in_strings(input, prefix)
