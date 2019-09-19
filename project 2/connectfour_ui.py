import connectfour_game
import connectfour_socket
import connectfour

#This function is to read the host when user inputs the host.
def _read_host() -> str:
    while True:
        host = input('Host: ').strip()
        if host == '':
            print('Please specify a host (either a name or an IP address)')
        else:
            return host


#This function is to read the port when user inputs the port.
def _read_port() -> int:
    while True:
        try:
            port = int(input('Port: ').strip())
            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port
        except ValueError:
            print('Ports must be an integer between 0 and 65535')


#This function is simply print the welcome sentences.
def _show_welcome() -> None:
    print()
    print('Connected!')
    print('Welcome to the Connectfour Client!')
    print()
    print('Please login with your username.')
    print()


#This function is to ask the username of the user.
def _ask_username() -> str:
    while True:
        username = input('Username: ').strip()
        if ' ' not in username and len(username) > 0:
            return username
        else:
            print('Username must not be empty and contain any whitespace')


#This function is to connect the host and the port. If connecting failed, the user needs
#to specify the host and the port again, until connecting is successful.
def _connect_server() -> connectfour_socket.ConnectfourConnection:
    while True:
        connectfour_host = _read_host()
        connectfour_port = _read_port()
        print('Connecting to {} (port {})...'.format(connectfour_host,connectfour_port))
        try:
            connection = connectfour_socket.connect(connectfour_host,connectfour_port)
            _show_welcome()
            return connection
        except:
            print('Failed to connect, please retry')


#This function is to send username to the server, just like login. If the login succeeds,
#the server will send back the welcome.
def _user_login(connection: connectfour_socket.ConnectfourConnection) -> None:
    while True:
        username = _ask_username()
        response = connectfour_socket.hello(connection,username)
        if response == True:
            print('Welcome {}!'.format(username))
            print()
            break
        else:
            continue


#This function is to ask user whether it is ready to start the game.
#When the user inputs ready, the server will send back ready.
def _ask_startcommand(connection: connectfour_socket.ConnectfourConnection) -> None:
    while True:
        startcommand = input('Type "Ready" to start connectfour game: ').strip()
        if startcommand == 'Ready':
            connectfour_socket.startgame_command(connection)
            print('Start game!')
            break
        else:
            ('pleas type Ready to start the game')


#This function is to take action on gamestate, when it is the user turn.
#And send the move to the server, receiving the ai's action.
def _player_turn(connection: connectfour_socket.ConnectfourConnection, game_state: connectfour.GameState) -> (connectfour.GameState, str):
    move = connectfour_game.drop_or_pop()
    column_number = connectfour_game.ask_column()
    game_state = connectfour_game.game_progress(game_state, move, column_number)
    connectfour_game.print_board(game_state)
    response = connectfour_socket.message_to_AI(connection, move, column_number)
    return game_state, response


#This function is to take action on gamestate, when it is the AI turn.
def _AI_turn(connection: connectfour_socket.ConnectfourConnection, game_state: connectfour.GameState) -> connectfour.GameState:
    move, column_number = connectfour_socket.read_move(connection)
    game_state = connectfour_game.game_progress(game_state, move, column_number)
    connectfour_game.print_board(game_state)
    return game_state

#This function is to start game between user and the Ai when everything is ready
#and end game when there is a winner
def _start_game(connection: connectfour_socket.ConnectfourConnection) -> None:
    game_state = connectfour.new_game()
    connectfour_game.print_board(game_state)
    while connectfour.winner(game_state) == 0:
        if connectfour_socket.AI_ready(connection):
            connectfour_game.print_turn(game_state)
            game_state, response= _player_turn(connection, game_state)
            if response == 'OKAY':
                connectfour_game.print_turn(game_state)
                game_state = _AI_turn(connection,game_state)
    if connectfour.winner(game_state) == 1:
        print('RED wins!')
    elif connectfour.winner(game_state) == 2:
        print('YELLOW wins!')



#This function is to run the user interface
def run_user_interface() -> None:
    connection = _connect_server()
    _user_login(connection)
    _ask_startcommand(connection)
    _start_game(connection)
    connectfour_socket.close(connection)   



if __name__ == '__main__':
    run_user_interface()








