import game_class
class InputError(Exception):
    pass
#this function is to get the board infomation
def get_board() -> (int, int, list,int, str):
    board_input = []
    try:
        row_num = int(input().strip())
        col_num = int(input().strip())
        turn = input().strip()
        winning_rule = input()
        if 4 <= row_num <= 16 and 4 <= col_num <= 16:
            if turn == 'B' or turn == 'W':
                if winning_rule == '<' or winning_rule == '>':
                    for row in range(row_num):
                        row_input = input().split(' ')
                        board_input.append(row_input)
                    if turn == 'B':
                        turn_num = 1
                    if turn == 'W':
                        turn_num = 2
                    return (row_num, col_num, board_input, turn_num, winning_rule)
                else:
                    raise InputError
            else:
                raise InputError
        else:
            raise InputError
    except:
        raise InputError




#this function is to get move on each turn
def get_move() -> int:
    while True:
        try:
            move_input = input().split(' ')
            move_row = int(move_input[0]) - 1
            move_col = int(move_input[1]) - 1
            if 0 <= move_row < game_class.BOARD_ROWS and 0 <= move_col < game_class.BOARD_COLUMNS:
                return move_row, move_col
            else:
                raise InputError
        except:
            raise InputError

#this function is to run the place and flip functions
def game_progress(Game) -> None:
    while True:
        try:
            place_row, place_col = get_move()
            Game.place(place_row, place_col)
            print("VALID")
            break
        except game_class.InvalidMoveError:
            print("INVALID")

# this function is to runthe user interface           
def run_user_interface() -> None:
    print('FULL')
    
    (game_class.BOARD_COLUMNS, 
    game_class.BOARD_ROWS, 
    game_class.BOARD_INPUT,
    game_class.TURN,
    game_class.WINNING_RULE) = get_board()
    Game = game_class.game()
    while not Game.game_over():
        Game.print_count()
        Game.print_board()
        Game.print_turn()
        game_progress(Game)
    Game.get_winner()




if __name__ == '__main__':
    run_user_interface()
