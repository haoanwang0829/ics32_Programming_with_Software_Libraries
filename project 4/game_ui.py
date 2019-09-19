import tkinter
import game_class

DEFAULT_FONT = ('Helvetica', 14)

class GameMenu:
    def __init__(self):
        self._menu_window = tkinter.Tk()
        self._menu_window.title('Othello Menu')
        self._game_input = {'row':tkinter.IntVar(),
                           'col':tkinter.IntVar(),
                            'turn':tkinter.IntVar(value ='1'),
                           'rule': tkinter.StringVar(value ='>')}
        self._set_widgets()


#this function is to set all the widgets in the input menu
    def _set_widgets(self) -> None:

        label = tkinter.Label(
            master = self._menu_window, text = 'The inputs of starting othello game',
            font = DEFAULT_FONT).grid(
            row = 0, column = 0, columnspan = 3, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        row_label = tkinter.Label(
            master = self._menu_window, text = 'Row:',
            font = DEFAULT_FONT).grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_info = tkinter.Label(
            master = self._menu_window, text = 'Input should be an even integer, between 3 and 15',
            font = DEFAULT_FONT).grid(
            row = 1, column = 1, padx = 10, pady = 10)

        row_input = tkinter.Entry(
            master = self._menu_window, textvariable = self._game_input['row'], width = 5, font = DEFAULT_FONT).grid(
            row = 1, column = 2, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        col_label = tkinter.Label(
            master = self._menu_window, text = 'Column:',
            font = DEFAULT_FONT).grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        col_info = tkinter.Label(
            master = self._menu_window, text = 'Input should be an even integer, between 3 and 15',
            font = DEFAULT_FONT).grid(
            row = 2, column = 1, padx = 10, pady = 10)

        col_input = tkinter.Entry(
            master = self._menu_window, textvariable = self._game_input['col'], width = 5, font = DEFAULT_FONT).grid(
            row = 2, column = 2, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        first_player_label = tkinter.Label(
            master = self._menu_window, text = 'Which first:',
            font = DEFAULT_FONT).grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        first_player_botton1 = tkinter.Radiobutton(
            master = self._menu_window, text = 'BLACK',
            variable = self._game_input['turn'], value = '1').grid(
            row = 3, column = 1, padx = 10, pady = 10, sticky = tkinter.W)

        first_player_botton2 = tkinter.Radiobutton(
            master = self._menu_window, text = 'WHITE',
            variable = self._game_input['turn'], value = '2').grid(
            row = 3, column = 2, padx = 10, pady = 10, sticky = tkinter.W)

        game_rule_label = tkinter.Label(
            master = self._menu_window, text = 'Game winning rule:',
            font = DEFAULT_FONT).grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        game_rule_botton1 = tkinter.Radiobutton(
            master = self._menu_window, text = 'Greater wins',
            variable = self._game_input['rule'], value = '>').grid(
            row = 4, column = 1, padx = 10, pady = 10, sticky = tkinter.W)

        game_rule_botton2 = tkinter.Radiobutton(
            master = self._menu_window, text = 'Less wins',
            variable = self._game_input['rule'], value = '<').grid(
            row = 4, column = 2, padx = 10, pady = 10, sticky = tkinter.W)

        menu_end_botton = tkinter.Button(master = self._menu_window, text = 'finish',
            command = self._get_input).grid(
            row = 5, column = 0, padx = 10, pady = 10,)

    # this function is to get all the valid input from input menu
    def _get_input(self) -> None:
        if self._game_input['row'].get() < 4 or self._game_input['row'].get() > 16 or self._game_input['col'].get() > 16 or self._game_input['col'].get() < 4 or self._game_input['row'].get() % 2 == 1 or self._game_input['col'].get() % 2 == 1:
            self.message = tkinter.Toplevel()
            self.message.title('ERROR')
            msg = tkinter.Message(master = self.message, text = 'WRONG INPUT', width = 500, padx = 10, pady = 10, font = DEFAULT_FONT).pack()
            ok_botton = tkinter.Button(master = self.message, text = 'OK', command = self.message.destroy).pack()
            self.message.grab_set()
            self.message.wait_window()
        else:
            self._menu_window.destroy()
            valid_input = (self._game_input['row'].get(),
            self._game_input['col'].get(),
            self._game_input['turn'].get(),
            self._game_input['rule'].get())
            game = Gameboard(valid_input)
            game.start()

    # start this menu
    def start(self) -> None:
        self._menu_window.mainloop()


class Gameboard:

    def __init__(self, valid_input: tuple):
        self.rows, self.cols, self.first_turn, self.rule = valid_input
        game_class.BOARD_ROWS = self.rows
        game_class.BOARD_COLUMNS = self.cols
        game_class.TURN = self.first_turn
        game_class.WINNING_RULE = self.rule
        self.turn_display = 'Black'
        self.board_input = []
        for row_num in range(self.rows):
            row = []
            for col_num in range(self.cols):
                row.append(0)
            self.board_input.append(row)

    # this function is to start the game board window.
    def start(self) -> None:
        self._set_board()
        self._board_window.mainloop()

    # this function is to set the board.
    def _set_board(self) -> None:
        self._board_window = tkinter.Tk()
        self._board_window.title('Othello')
        self._set_widgets()

    # this function is to set the widgets.
    def _set_widgets(self) -> None:


        game_label = tkinter.Label(
            master = self._board_window, text = 'FULL Version', 
            font = ('Helvetica', 30)).grid(
            row = 0, column = 0)

        self._instruction = tkinter.StringVar(value = 'Set tiles\
\nOne click for Black\
\nTwo clicks for White\
\nThree clicks to remove')

        game_msg = tkinter.Message(
            master = self._board_window, textvariable = self._instruction,
            width = 400, justify = 'center').grid(
            row = 1, column = 0)

        self._score_text = tkinter.StringVar(value = 'Black: 0 White: 0')
        game_score = tkinter.Label(
            master = self._board_window, textvariable = self._score_text,
            font = DEFAULT_FONT).grid(
            row = 2, column = 0)

        self._canvas = tkinter.Canvas(
            master = self._board_window, width = int(self.cols) * 40, height = int(self.rows) * 40, 
            background = '#006000')
        self._canvas.grid(row = 3, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        if self.first_turn == 1:
            self.turn_display = 'Black'
        else:
            self.turn_display = 'White'
        self._turn_text = tkinter.StringVar(value = 'Turn: {}'.format(self.turn_display))
        game_turn = tkinter.Label(
            master = self._board_window, textvariable = self._turn_text,
            font = DEFAULT_FONT).grid(
            row = 4, column = 0)

        self._set_button = tkinter.Button(master = self._board_window, text = 'Start game',
                                      command = self._start_game).grid(row = 5,column = 0)


        self.set_button_quit = tkinter.Button(master = self._board_window, text = 'Cancel',
                                        command = self.quit).grid(row = 6, column = 0)



        self._board_window.rowconfigure(3, weight = 1)
        self._board_window.columnconfigure(0, weight = 1)
        self._draw_grid()

        self._canvas.bind('<Button-1>',self._set_tiles)
        self._canvas.bind('<Configure>',self._draw_the_board2)

    # draw grid
    def _draw_grid(self) -> None:
        self._canvas.update()
        d_col = self._canvas.winfo_width()/self.cols
        d_row = self._canvas.winfo_height()/self.rows

        for x in range(self.cols):
            for y in range(self.rows):
                 x0 = x * d_col
                 y0 = y * d_row
                 self._canvas.create_rectangle(x0, y0,
                                                x0+d_col, y0+d_row,
                                                outline = 'yellow')
    # set dics on board
    def _set_tiles(self, event) -> None:
        row,col = self._get_rowcol(event)
        if self.board_input[row][col] == game_class.NONE:
           self.board_input[row][col] = game_class.BLACK
           self._draw_dics(row, col, game_class.BLACK)
        elif self.board_input[row][col] == game_class.BLACK:
            self.board_input[row][col] = game_class.WHITE
            self._draw_dics(row, col, game_class.WHITE)
        else:
            self.board_input[row][col] = game_class.NONE
            self._draw_dics(row, col, game_class.NONE)

    # get the row and col of click point
    def _get_rowcol(self, event) -> None:
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        click_point = from_pixel(event.x, event.y, width ,height)
        frac_x, frac_y = click_point.frac()
        row = int(frac_y*self.rows)
        col = int(frac_x*self.cols)
        return row,col

    # draw the dics on board
    def _draw_dics(self, row: int, col: int, color: int) -> None:
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        top_y  = (height/self.rows) * row + 10
        top_x = (width/self.cols) * col + 10
        bottom_y = (height/self.rows) * (row + 1) - 10
        bottom_x = (width/self.cols) * (col + 1) - 10
        if color == game_class.NONE:
            self._canvas.create_oval(top_x, top_y, bottom_x, bottom_y, fill = '#006000', outline = '#006000')
        elif color == game_class.BLACK:
            self._canvas.create_oval(top_x, top_y, bottom_x, bottom_y, fill = 'black', outline = 'black')
        else:
            self._canvas.create_oval(top_x, top_y, bottom_x, bottom_y, fill = 'white', outline = 'white')


    # to start the game
    def _start_game(self) -> None:
        self._set_button = tkinter.Button(master = self._board_window, text = 'New game',
                                      command = self._start_new_game).grid(row = 5,column = 0)
        game_class.BOARD_INPUT = self.board_input
        self.Game = game_class.game()
        self._canvas.bind('<Configure>',self._draw_the_board)
        self._update_info()
        if self.Game.game_over():
            self._end_game()
        else:
            self._canvas.bind('<Button-1>',self._make_move)
    
    # when game is finished, end the game  
    def _end_game(self) -> None:
        winner = self.Game.get_winner()
        if winner == game_class.BLACK:
            self._instruction.set('Game Over!')
            self._turn_text.set('Black wins!')
        elif winner == game_class.WHITE:
            self._instruction.set('Game Over!')
            self._turn_text.set('White wins!')
        else:
            self._instruction.set('Game Over!')
            self._turn_text.set('No Winner!')

    # update all the information
    def _update_info(self) -> None:
        if self.Game.turn == 1:
            self.turn_display = 'Black'
        else:
            self.turn_display = 'White'
        self._instruction.set('Click to move')
        self._score_text.set('Black: {} White: {}'.format(self.Game.black, self.Game.white))
        self._turn_text.set('Turn: {}'.format(self.turn_display))


    # to make move when player click the board
    def _make_move(self, event) -> None:
        row, col = self._get_rowcol(event)
        try:
            self.Game.place(row, col)
            self._draw_the_board(event)
            self._update_info()
        except:
            pass
        finally:
            if self.Game.game_over():
                self._end_game()
            
            
    # redraw the board
    def _draw_the_board(self, event) -> None:
        self._canvas.delete(tkinter.ALL)
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.Game.board[row][col]
                self._draw_dics(row, col, color)
        self._draw_grid()

    # redraw the board when game is not started
    def _draw_the_board2(self,event) -> None:
        self._canvas.delete(tkinter.ALL)
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.board_input[row][col]
                self._draw_dics(row, col, color)
        self._draw_grid()

    # start a new game   
    def _start_new_game(self) -> None:
        self.quit()
        GAME = GameMenu()
        GAME.start()

    # to quit  
    def quit(self) -> None:
        self._board_window.destroy()

class Point:
    def __init__(self, frac_x: float, frac_y:float):
        self._frac_x = frac_x
        self._frac_y = frac_y
    
    def frac(self) -> (float,float):
        return (self._frac_x, self._frac_y)

    def pixel(self, pixel_width: float, pixel_height: float)-> (float,float):
        pixel_x = pixel_width * self._frac_x
        pixel_y = pixel_height * self._frac_y
        return (pixel_x,pixel_y)

def from_frac(frac_x:float, frac_y:float)-> Point:
    return Point(frac_x,frac_y)

def from_pixel(pixel_x: float, pixel_y:float,
               pixel_width: float, pixel_height:float) -> Point:
    frac_x = pixel_x/pixel_width
    frac_y = pixel_y/pixel_height
    return Point(frac_x, frac_y)

        
                
            






   





    


if __name__ == '__main__':
    GAME = GameMenu()
    GAME.start()

        
