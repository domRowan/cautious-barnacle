# Many MANY assumptions on 9x9
def sudoku_checker(sudoku_board):

    game_complete = check_if_game_complete(sudoku_board)

    if game_complete:
        print("Game is complete")
    else:
        print("Game is not complete")

    game_successful = check_if_game_successful(sudoku_board)

    if game_successful:
        print("Game is successful")
    else:
        print("Game is not successful")

    return game_successful

    
def print_board(sudoku_board):
    for row in sudoku_board:
        print(row)


def check_if_game_complete(sudoku_board):
    game_is_complete = True

    for row in sudoku_board:
        for value in row:
            if value_is_out_of_range(value):
                game_is_complete = False
    
    return game_is_complete


def value_is_out_of_range(value):
    return (value <= 0) or (value >= 10)


def check_if_game_successful(sudoku_board):
    game_is_successful = True
    game_is_successful = check_if_rows_and_colums_successful(sudoku_board)
    game_is_successful = check_if_squares_successful(sudoku_board)
    return game_is_successful
    
    
def check_if_rows_and_colums_successful(sudoku_board):
    rows_and_columns_successful = True

    rows = create_rows_from_board(sudoku_board)
    columns = create_columns_from_rows(rows)
    
    rows_and_columns_successful = validate_rows_columns_or_squares(rows)
    rows_and_columns_successful = validate_rows_columns_or_squares(columns)

    return rows_and_columns_successful


def create_rows_from_board(sudoku_board):
    rows = []
    for row in sudoku_board:
        rows.append(row)
    return rows


def create_columns_from_rows(rows):
    columns = []
    for i in range(len(rows)):
        column = []
        for row in rows:
            column.append(row[i])
        columns.append(column)
    return columns


def create_squares_from_board(sudoku_board):
    squares = []

    centre_points = [(1, 1), (4, 1), (7, 1), (1, 4), (4, 4), (7, 4), (7, 1), (7, 4), (7, 7)]

    for centre_point in centre_points:
        squares.append(create_square_around_point(sudoku_board, centre_point))

    return squares


def check_if_squares_successful(sudoku_board):
    squares_successful = True
    squares = create_squares_from_board(sudoku_board)

    squares_successful = validate_rows_columns_or_squares(squares)

    return squares_successful
    


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


def validate_rows_columns_or_squares(rows_or_columns):
    game_is_successful = True
    for row_or_column in rows_or_columns:
        game_is_successful =  is_row_column_or_square_complete(row_or_column)
        if not game_is_successful:
            return False
    
    return game_is_successful


def is_row_column_or_square_complete(row_or_column):
    numbers_present = set()
    row_or_column_is_complete = True

    for value in row_or_column:
        if value_is_out_of_range(value) or value in numbers_present:
            return False
        else:
            numbers_present.add(value)
    return row_or_column_is_complete


invalid_input = [
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[1, 2, 3, 4, 5, 6, 7, 8, 9]]

invalid_input_rows_correct = [
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[2, 3, 4, 5, 6, 7, 8, 9, 1], 
[3, 4, 5, 6, 7, 8, 9, 1, 2], 
[4, 5, 6, 7, 8, 9, 1, 2, 3], 
[5, 6, 7, 8, 9, 1, 2, 3, 4], 
[6, 7, 8, 9, 1, 2, 3, 4, 5], 
[7, 8, 9, 1, 2, 3, 4, 5, 6], 
[8, 9, 1, 2, 3, 4, 5, 6, 7], 
[9, 1, 2, 3, 4, 5, 6, 7, 8]]

invalid_input_one_duplicate = [
[1, 1, 3, 4, 5, 6, 7, 8, 9], 
[4, 5, 6, 7, 8, 9, 1, 2, 3], 
[7, 8, 9, 1, 2, 3, 4, 5, 6], 
[2, 3, 4, 5, 6, 7, 8, 9, 1], 
[5, 6, 7, 8, 9, 1, 2, 3, 4], 
[8, 9, 1, 2, 3, 4, 5, 6, 7], 
[3, 4, 5, 6, 7, 8, 9, 1, 2],  
[6, 7, 8, 9, 1, 2, 3, 4, 5], 
[9, 1, 2, 3, 4, 5, 6, 7, 8]]

valid_input = [
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[4, 5, 6, 7, 8, 9, 1, 2, 3], 
[7, 8, 9, 1, 2, 3, 4, 5, 6], 
[2, 3, 4, 5, 6, 7, 8, 9, 1], 
[5, 6, 7, 8, 9, 1, 2, 3, 4], 
[8, 9, 1, 2, 3, 4, 5, 6, 7], 
[3, 4, 5, 6, 7, 8, 9, 1, 2],  
[6, 7, 8, 9, 1, 2, 3, 4, 5], 
[9, 1, 2, 3, 4, 5, 6, 7, 8]]

# sudoku_checker(invalid_input_one_duplicate)