from sets import Set


def find_pair_with_sum(input, target_sum):
    values = Set()
    result = None

    for i in range(0, len(input)):
        value = target_sum - input[i]
        for j in values:
            if (j + value) == target_sum:
                result = (value, j)
        if value not in values:
            values.add(value)

    return result


input = [1, 2, 4, 9]
# input = [1, 2, 4, 4]

sum = 8

print find_pair_with_sum(input, sum)
