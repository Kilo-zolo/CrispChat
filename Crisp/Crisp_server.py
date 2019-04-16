import socket
import select
### We use 'select' to give us operating system io which means the code will run the same wether on mac, linux or windows ###

HEADER = 10
IP = "127.0.0.1"
### Make sure to config to your IP address ###
PORT = 8080
### PORTS should be same on client and server ###

server_socket = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
server_socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

server_socket.bind(( IP , PORT ))

server_socket.listen()

sockets_list = [ server_socket ]
### for now there is only the server present but as clients increase you may add the to the 'sockets_list' ###

clients = {}
### this can be used as a client dictionary which allows clients username to be shown instead of port and ip ###

def recieve_message(client_socket):
                    try:
                        message_header = client_socket.recv( HEADER_LENGTH )
                        if not len(message_header):
                            return False

                        message_length = int(message_header.decode('utf-8').strip())
                        return{ "header": message_header , "data": client_socket.recv(message_length) }


                    except:
                        return False


while True:
    read_sockets , _, exception_sockets = select.select( sockets_list, [] , sockets_list )
### 'sockets_list' is used for the sockets whose messages we want to read. '[]' is used for the messages we want to type to the sockets. 'sockets_list' is used again if any of the sockets had gone through an error. ###

for notified_socket in read_sockets:
    if notified_socket == server_socket:
        client_socket, client_address = server_socket.accept()

user = recieve_message( client_socket )
if user is False:
 continue

sockets_list.append( client_socket )

clients[ client_socket ] = user
print(f" New Crisp found astray from { client_address[0] }:{ client_address[1] } username { user['data'].decode('utf-8') } ")

else: 
     message = recieve_message( notified_socket )

if message is False:
                    print(f" Crisp { clients[notified_socket]['data'].decode('utf-8') } found eaten alive  ")
                    sockets_list.remove(notified_socket)
            del clients[notified_socket]
            continue

                    user = clients[ notified_socket ]
                    print(f" Crisp { user ['data'].decode('utf-8') } has asked for your acquaitance: { message['data'].decode('utf-8') } ")

                    for client_socket in clients:
                        if client_socket != notified_socket:
                            client_socket.send( user['header'] + user ['data'] + message['header'] + message['data'] )

                   for notified_socket in exception_sockets:
                       sockets_list.remove(notified_socket)
                       del clients[notified_socket]

### simple note to begginers TWO BLANK LINES AFTER A FUNCTION DEFINITION IS MANDATORY ###
