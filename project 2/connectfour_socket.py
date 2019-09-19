import connectfour
import socket
from collections import namedtuple

ConnectfourConnection = namedtuple('ConnectfourConnection','socket,input,output')

class ConnectfourprotocolError(Exception):
    pass


#This function is to connect the server, using the host and port which are input of user.
def connect(host: str, post: int) -> ConnectfourConnection:
    connectfour_socket = socket.socket()
    connectfour_socket.connect((host,post))
    connectfour_input = connectfour_socket.makefile('r')
    connectfour_output = connectfour_socket.makefile('w')

    return ConnectfourConnection(connectfour_socket,connectfour_input,connectfour_output)


#This function is to send the username to the server, 
#and receive the welcome.
def hello(connection: ConnectfourConnection, username: str) -> bool:
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    response = _read_line(connection)
    if response == 'WELCOME ' + username:
        return True
    else:
        raise ConnectfourprotocolError


#This function is to send AI_Game command to the server,
#so that the server will send back ready.
def startgame_command(connection: ConnectfourConnection):
    _write_line(connection, 'AI_GAME')


#This function is to receive the ready from server
#and return True so that we can start the game.
def AI_ready(connection: ConnectfourConnection) -> bool:
    response = _read_line(connection)
    if response == 'READY':
        return True

#This function is to send the user's action to the server and receive the ''OKAY'
#from the AI
def message_to_AI(connection: ConnectfourConnection, move: 'function', column_number: int) -> str:
    if move == connectfour.drop:
        _write_line(connection, 'DROP ' + str(column_number + 1))
    elif move == connectfour.pop:
        _write_line(connection, 'POP ' + str(column_number + 1))
    response = _read_line(connection)
    return response

#This function is to read the move of AI, when user receive AI's move.
def read_move(connection: ConnectfourConnection) -> ('function', int):
    AI_command = _read_line(connection).split()
    if AI_command[0] == 'DROP':
        print('AI drops into column  ' + AI_command[1])
        return connectfour.drop, int(AI_command[1]) - 1
    elif AI_command[0] == 'POP':
        print('AI pops out column ' + AI_command[1])
        return connectfour.pop, int(AI_command[1]) - 1


#This function is to read line from server.
def _read_line(connection) -> str:
    line = connection.input.readline().strip()
    return line


#This function is to write line to server.
def _write_line(connection,line) -> None:
    connection.output.write(line + '\r\n')
    connection.output.flush()

#This function is to close the connection.
def close(connection: ConnectfourConnection) -> None:
    connection.input.close()
    connection.output.close()
    connection.socket.close()





