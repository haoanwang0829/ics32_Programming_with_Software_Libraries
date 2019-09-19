
BOARD_COLUMNS = 0
BOARD_ROWS = 0
TURN = 0
NONE = 0
BLACK = 1
WHITE = 2
WINNING_RULE = ''
BOARD_INPUT = []

class InvalidMoveError(Exception):
    pass



class game:

    def __init__(self) -> None:
        self.columns = BOARD_COLUMNS
        self.rows = BOARD_ROWS
        self.turn = TURN
        self.opposite = self._opposite_turn()
        self.board = self._new_board()
        self.black, self.white = self._count_disc()

    def _opposite_turn(self) -> int:
        if self.turn == BLACK:
            return WHITE
        if self.turn ==WHITE:
            return BLACK

    def _new_board(self) -> list:
        for row in BOARD_INPUT:
            for col, disc in enumerate(row):
                if disc == '.':
                    row[col] = NONE
                elif disc == 'B':
                    row[col] = BLACK
                elif disc == 'W':
                    row[col] = WHITE
        return BOARD_INPUT

    def _count_disc(self) -> (int,int):
        count_black = 0
        count_white = 0
        for column in self.board:
            for element in column:
                if element == BLACK:
                    count_black += 1
                elif element == WHITE:
                    count_white +=1
        return count_black, count_white

    def print_count(self) -> None:
        count_black, count_white = self._count_disc()
        print('B: {}  W: {}'.format(count_black,count_white))

    def print_turn(self) -> None:
        if self.turn == 1:
            print('TURN: B')
        if self.turn == 2:
            print('TURN: W')

    def _switch_turn(self) -> None:
        if self.turn == BLACK:
            self.turn = WHITE
            self.opposite = BLACK
        elif self.turn == WHITE:
            self.turn = BLACK
            self.opposite = WHITE

    def print_board(self) -> None:
        board_show = []
        for i,row in enumerate(self.board):
            row_list = []
            for disc in row:
                if disc == NONE:
                    row_list.append('.')
                elif disc == BLACK:
                    row_list.append('B')
                elif disc == WHITE:
                    row_list.append('W')
            board_show.append(row_list)
        for row in board_show:
            print(*row)


### place the cell and the flip
    def place(self, place_row: int, place_col: int) -> None:
        flip_list = self._search_cell_to_flip(place_row, place_col)
        if flip_list != []:
            if self._empty_space(place_row,place_col):
                self.board[place_row][place_col] = self.turn
                self.flip(place_row, place_col)
                self._switch_turn()
                self.black, self.white = self._count_disc()
            else:
                InvalidMoveError
        else:
            raise InvalidMoveError
        


        
    def _empty_space(self, row: int, col: int) -> bool:
        space = self.board[row][col]
        if space == NONE:
            return True
        else:
            return False

    def _search_cell_to_flip(self, place_row: int, place_col: int) -> list:
        search_result= []
        for x in range(-1,2):
            for y in range(-1,2):
                if x == 0 and y == 0:
                    continue
                row_x = place_row + x
                col_y = place_col + y
                while 0 <= row_x < self.rows and 0 <= col_y < self.columns and self.board[row_x][col_y] == self.opposite:
                    row_x += x
                    col_y += y
                    if 0 <= row_x < self.rows and 0 <= col_y < self.columns and self.board[row_x][col_y] == self.turn:
                        search_result.append([row_x,col_y])
        return search_result


    def flip(self, place_row: int, place_col: int) -> None:
        flip_list = self._search_cell_to_flip(place_row, place_col)
        for cell in flip_list:
            target_row = cell[0]
            target_col = cell[1]
            dx = target_row - place_row
            dy = target_col - place_col
            if dx != 0  and dy != 0:
                x = 1
                y = 1
            if dx == 0:
                x = 0
                y = 1
            elif dy == 0:
                x = 1
                y = 0
            if dx < 0:
                x = -x
            if dy < 0:
                y = -y
            row_x = place_row + x
            col_y = place_col + y
            while self.board[row_x][col_y] == self.opposite:
                self.board[row_x][col_y] = self.turn
                row_x += x
                col_y += y

    def game_over(self) -> bool:
        game_over = 0
        for i,row in enumerate(self.board):
            for j,dics in enumerate(row):
                if self._empty_space(i,j):
                    if self._search_cell_to_flip(i,j) != []:
                        game_over += 1
        if game_over == 0:
            return True

    def get_winner(self) -> None:
        count_black, count_white =self._count_disc()
        if WINNING_RULE == '>':
            if count_black > count_white:
                return BLACK
            elif count_white > count_black:
                return WHITE
            else:
                return NONE

        else:
            if count_black < count_white:
                return BLACK
            elif count_white < count_black:
                return WHITE
            else:
                return NONE







