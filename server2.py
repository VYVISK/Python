import socket
import threading
import authentication

# Define host and port
HOST = '10.113.19.118'
PORT = 1500

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    
    # Ask for username
    client_socket.sendall(b"Enter your username: ")
    username = client_socket.recv(1024).decode('utf-8').strip()

    # Ask for password
    client_socket.sendall(b"Enter your password: ")
    password = client_socket.recv(1024).decode('utf-8').strip()

    # authentication.results = authentication.import_user_password_table()

    print(username,password)

    # Simple authentication logic (you should replace this with a secure authentication method)
    result = authentication.check_username_password(username,password)
    
    
    if result:
        client_socket.sendall(b"Login successful!\n")
    else:
        client_socket.sendall(b"Login failed. Disconnecting.\n")
        client_socket.close()
        return

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
