import connectfour


#This function is to get the drop or pop command.
#The user needs to type drop or pop to specify the method to move,
def drop_or_pop() -> 'function':
    while True:
        move_input = input('Type drop for drop, pop to pop up: ')
        if move_input == 'drop':
            return connectfour.drop
        elif move_input == 'pop':
            return connectfour.pop
        else:
            print('Wrong move')


#This function is to get the column number.
#The user needs to input an integer to specify which column 
#he wants to take action on.
def ask_column() -> int:
    while True:
        try:
            column_number = int(input('Which column: ')) - 1
            if column_number < 0 or column_number > int(connectfour.BOARD_COLUMNS) - 1:
                print('Column number must between 1 and {}'.format(connectfour.BOARD_COLUMNS))
            else:
                return column_number
        except ValueError:
            print('Column number must be an integer')
    

#This function is to take action in one turn.
#The imports are user's instruction and the gamestate.
def game_progress(game_state: connectfour.GameState, move, column_number: int) -> connectfour.GameState:
    while True:
        try:
            game_state = move(game_state,column_number)
        except connectfour.InvalidMoveError:
            print('Invalid move! Try again')
        finally:
            return game_state


#This function is to print the board of the gamestate.
#Including switch the columns and rows in the right order。
def print_board(game_state: connectfour.GameState) -> None:
    game_board = game_state.board
    new_board = []
    for row in range(connectfour.BOARD_ROWS):
        new_board.append([])
    for column in game_board:
        for row, element in enumerate(column):
            if element == 0:
                new_board[row].append('.')
            elif element == 1:
                new_board[row].append('R')
            elif element == 2:
                new_board[row].append('Y')
    print(*list(range(1,connectfour.BOARD_COLUMNS + 1)))
    for column in new_board:
        print(*column)
    print()


#This simple function is to print the turn of the current gamestate.
def print_turn(game_state: connectfour.GameState) -> None:
    turn = game_state.turn
    if turn == 1:
        print('RED turn')
    elif turn == 2:
        print('YELLOW turn')
 



