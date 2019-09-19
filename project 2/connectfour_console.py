import connectfour
import connectfour_game


#This function is to start the game locally.
def startgame() -> None:
	game_state = connectfour.new_game()
	connectfour_game.print_board(game_state)
	while connectfour.winner(game_state) == 0:
		connectfour_game.print_turn(game_state)
		move = connectfour_game.drop_or_pop()
		column_number = connectfour_game.ask_column()
		game_state = connectfour_game.game_progress(game_state,move,column_number)
		connectfour_game.print_board(game_state)
	if connectfour.winner(game_state) == 1:
		print('RED WINS!')
	elif connectfour.winner(game_state) == 2:
		print('YELLOW WINS!')



if __name__ == '__main__':
	startgame()
