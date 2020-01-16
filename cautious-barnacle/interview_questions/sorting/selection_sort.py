def not_a_selection_sort(input):
    last_index = len(input) - 1
    did_a_shuffle = False

    for pivot_index in range(last_index, -1, -1):
        print "________ Pivot index", pivot_index
        if did_a_shuffle:
            pivot_index = last_index
            did_a_shuffle = False
            print "Did a shuffle, updating the pivot index", pivot_index

        for i in range(0, pivot_index):
            if input[i] > input[pivot_index]:
                # do the shuffle
                value_to_shuffle = input[i]
                input.remove(value_to_shuffle)
                input.append(value_to_shuffle)
                pivot_index -= 1
                did_a_shuffle = True
                print "Doing a shuffle ", input[pivot_index], value_to_shuffle, pivot_index
                print input

    return input


def selection_sort(input):
    last_index = len(input) - 1

    for current_max in range(last_index, -1, -1):
        position_of_max = 0
        for i in range(0, current_max+1):
            if input[i] > input[position_of_max]:
                position_of_max = i
        temp = input[current_max]
        input[current_max] = input[position_of_max]
        input[position_of_max] = temp
    return input


input = [3, 56, 7, 3, 547, 12, 6, 78, 12, 4, 0]
print selection_sort(input)
