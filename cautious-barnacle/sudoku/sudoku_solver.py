from sudoku_checker import sudoku_checker


# Many MANY assumptions on 9x9
def sudoku_solver(sudoku_board):

    print("Input board")
    print_board(sudoku_board)

    # create list of empty points
    empty_points = find_empty_points(sudoku_board)

    previous_pass_valid = True

    index = 0

    while (index >= 0) and (index < len(empty_points)):
        current_point = empty_points[index]
        current_value = sudoku_board[current_point[0]][current_point[1]]
        new_value = current_value + 1
        if (value_is_out_of_range(new_value)):
            # reset the value at the current point
            # go back to the previous point and add one
            sudoku_board[current_point[0]][current_point[1]] = 0
            index -= 1
            continue
        
        sudoku_board[current_point[0]][current_point[1]] = new_value

        current_row = get_current_row(sudoku_board, current_point)
        current_column = get_current_column(sudoku_board, current_point)
        current_square = get_current_square(sudoku_board, current_point)

        current_row_valid = is_row_column_square_valid(current_row)
        current_column_valid = is_row_column_square_valid(current_column)
        current_square_valid = is_row_column_square_valid(current_square)

        if not current_row_valid or not current_column_valid or not current_square_valid:
            continue

        index += 1
    
    print("Complete board")
    print_board(sudoku_board)

    return sudoku_checker(sudoku_board)

def print_board(sudoku_board):
    for row in sudoku_board:
        print(row)

def get_current_square(sudoku_board, current_point):
    current_square_centre_point = get_current_square_centre_point(sudoku_board, current_point)
    return create_square_around_point(sudoku_board, current_square_centre_point)

def create_square_around_point(sudoku_board, point):
    square = []
    square_directions = get_square_directions()

    for direction in square_directions:
        point_in_direction = ((point[0] + direction[0]), (point[1], direction[1]))
        square.append(sudoku_board[point_in_direction[0]][point_in_direction[1]])
    
    return square

def get_square_directions():
    return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

def get_current_square_centre_point(sudoku_board, current_point):
    centre_points = get_centre_points()

    for centre_point in centre_points:
        # +2 because range is exclusive
        # This does not contain the last item in the range
        x_range = range(centre_point[0]-1, centre_point[0]+2) 
        y_range = range(centre_point[1]-1, centre_point[1]+2)
       
        if (current_point[0] in x_range) and (current_point[1] in y_range):
            return centre_point

    return None

def get_centre_points():
    return [(1, 1), (4, 1), (7, 1), (1, 4), (4, 4), (7, 4), (1, 7), (4, 7), (7, 7)]

def get_current_column(sudoku_board, current_point):
    column = []
    for row in sudoku_board:
        column.append(row[current_point[1]])
    return column

def get_current_row(sudoku_board, current_point):
    return sudoku_board[current_point[0]]

def find_empty_points(sudoku_board):
    empty_points = []
    for x_position in range(len(sudoku_board)):
        for y_position in range(len(sudoku_board[x_position])):
            value_at_point = sudoku_board[x_position][y_position]
            if is_empty(value_at_point):
                empty_points.append((x_position, y_position))
    return empty_points

def is_empty(value):
    return value == 0

def value_is_out_of_range(value):
    return (value <= 0) or (value >= 10)


def create_square_around_point(sudoku_board, centre_point):
    square = []

    directions = get_directions()

    for direction in directions:
        x_position = centre_point[0] + direction[0]
        y_position = centre_point[1] + direction[1]
        square.append(sudoku_board[x_position][y_position])

    return square


def get_directions():
    return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

def value_is_out_of_range_excluding_0(value):
    return (value < 0) or (value >= 10)

def is_row_column_square_valid(row_column_square):
    numbers_present = set()
    row_or_column_is_complete = True

    for value in row_column_square:
        if value_is_out_of_range_excluding_0(value) or (value > 0 and value in numbers_present):
            return False
        else:
            # Currently adding 0 to the set many times but not checking it
            numbers_present.add(value)

    return row_or_column_is_complete

valid_input = [
[1, 0, 3, 0, 0, 0, 7, 8, 9], 
[4, 5, 6, 7, 0, 9, 1, 2, 0], 
[7, 0, 9, 1, 0, 3, 4, 5, 0], 
[2, 0, 4, 5, 6, 7, 8, 0, 0], 
[5, 6, 0, 0, 9, 1, 2, 3, 4], 
[8, 9, 1, 0, 3, 0, 5, 6, 0], 
[3, 0, 0, 6, 0, 8, 0, 1, 2],  
[6, 7, 8, 9, 0, 2, 3, 0, 5], 
[9, 0, 2, 0, 4, 5, 6, 7, 0]]

zero_input = [
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0],  
[0, 0, 0, 0, 0, 0, 0, 0, 0]]

sudoku_solver(zero_input)


