BOARD_COLUMNS = 8
BOARD_ROWS = 6
NONE = 0
BLACK = 1
WHITE = 2
class game:

    def __init__(self):
        self.columns = BOARD_COLUMNS
        self.rows = BOARD_ROWS
        self.board = self._get_board()

    def _get_board(self):
        board = []

        for col in range(self.columns):
            board.append([])
            for row in range(self.rows):
                board[-1].append(NONE)

        return board

    def _print_out(self):
        print(self.board)



Game = game()
Game._print_out()       