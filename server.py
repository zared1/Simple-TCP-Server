import socket
import threading

server_address = ('localhost', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen()

def handle_client(conn, address):
    data = conn.recv(4096)
    data = data.decode()
    print(f'Received {data} from {address}')


def handle_incoming_connections():
    while True:
        conn, address = sock.accept()
        print(f'Accepted connection from {address}')

        thread = threading.Thread(target=handle_client, args=(conn, address))
        thread.start()

thread = threading.Thread(target=handle_incoming_connections)
thread.start()

while True:
    message = input('Enter a message to send: ')
    for conn, address in connected_clients:
        conn.send(message.encode())
