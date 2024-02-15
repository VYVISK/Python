import socket

# Define host and port
HOST = '192.168.20.55'  # Standard loopback interface address (localhost)
PORT = 6969        # Port to listen on (non-privileged ports are > 1023)

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
        
        with client_socket:
            print(f"Connection from {client_address}")
            
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break  # Break the loop if no data is received
            
            # Process received data (for demonstration, just echo it back)
            print(f"Received data: {data.decode('utf-8')}")
            client_socket.sendall(data)  # Echo back the received data to the client