def bubble_sort(input):
    have_performed_swap = True

    while have_performed_swap:
        have_performed_swap = False

        for i in range(0, len(input)):
            next_index = i + 1
            if next_index < len(input) and input[i] > input[next_index]:
                temp_value = input[i]
                input[i] = input[next_index]
                input[next_index] = temp_value
                have_performed_swap = True

    return input


input = [3, 56, 7, 3, 547, 12, 6, 78, 12, 4]
print bubble_sort(input)
