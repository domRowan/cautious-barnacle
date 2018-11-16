def minimumBribes(q):
    too_chaotic = check_if_too_chaotic(q)

    if too_chaotic:
        print("Too chaotic")
    else:
        print(get_number_of_swaps(q))


def check_if_too_chaotic(input):
    too_chaotic = False
    for i in range(0, len(input)):
        expected_value_at_index = i+1
        if input[i] > expected_value_at_index + 2:
            too_chaotic = True

    return too_chaotic


def get_number_of_swaps(input):
    have_performed_swap = True
    number_of_swaps = 0

    while have_performed_swap:
        have_performed_swap = False

        for i in range(0, len(input)):
            next_index = i + 1
            if next_index < len(input) and input[i] > input[next_index]:
                temp_value = input[i]
                input[i] = input[next_index]
                input[next_index] = temp_value
                have_performed_swap = True
                number_of_swaps += 1

    return number_of_swaps


input = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(input)

# [1, 2, 5, 3, 7, 8, 6, 4] evai = 1, v = 1, d = na, nos = 0
# [1, 2, 5, 3, 7, 8, 6, 4] evai = 2, v = 2, d = na, nos = 0
# [1, 2, 5, 3, 7, 8, 6, 4] evai = 3, v = 5, d = 2, nos = 2
# [1, 2, 5, 3, 7, 8, 6, 4] evai = 4, v = 3, d = na, nos = 2
# [1, 2, 5, 3, 7, 8, 6, 4] evai = 5, v = 7, d = 2, nos = 4
# [1, 2, 5, 3, 7, 8, 6, 4] evai = 6, v = 8, d = 2, nos = 6
# [1, 2, 5, 3, 7, 8, 6, 4] evai = 7, v = 6, d = na, nos = 6
# [1, 2, 5, 3, 7, 8, 6, 4] evai = 8, v = 4, d = na, nos = 6
