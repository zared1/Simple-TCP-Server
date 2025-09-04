# Simple TCP Server

This is a basic Python TCP server that accepts incoming connections and handles each client in a separate thread. It prints messages received from clients and allows the server operator to send messages back to all connected clients.

## Features

* Handles multiple clients using threading
* Prints received messages from clients
* Lets the server send messages to all connected clients (note: you’ll need to add the list of clients yourself)

## How to Run

1. Clone or download the repo.
2. Run the server script:

```bash
python server.py
```

3. Connect with a client like `nc` (netcat):

```bash
nc localhost 10000
```

4. Type messages in the client to send to the server.
5. Type messages in the server console to send to all clients (requires managing connected clients list).

## Notes

* The code currently receives only one message per client connection.
* The `connected_clients` list is referenced but not implemented; you’ll need to add it to keep track of clients to broadcast messages properly.
* You can improve the server by looping in `handle_client` to receive multiple messages and properly managing client connections.
