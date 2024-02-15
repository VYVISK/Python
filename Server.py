import socket
import threading

# Define host and port
HOST = '192.168.20.55'  # Standard loopback interface address (localhost)
PORT = 1500        # Port to listen on (non-privileged ports are > 1023)

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data from {client_address}: {data.decode('utf-8')}")
            client_socket.sendall(data)

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()