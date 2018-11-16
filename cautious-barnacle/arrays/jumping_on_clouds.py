def jumpingOnClouds(c):
    number_of_clouds = len(c)-1
    current_index = 0
    number_of_jumps = 0

    while current_index < number_of_clouds:
        if can_jump_two(c, number_of_clouds, current_index):
            current_index = current_index + 2
            number_of_jumps += 1
        else:
            current_index = current_index + 1
            number_of_jumps += 1

    return number_of_jumps


def can_jump_two(clouds, number_of_clouds, current_index):
    jump = current_index + 2
    if jump <= number_of_clouds and clouds[jump] == 0:
        return True

    return False


array_of_clouds = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(array_of_clouds))
