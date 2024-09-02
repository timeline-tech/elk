import socket
import os

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))  # Bind to all interfaces
    server_socket.listen(1)  # Listen for one connection
    print(f"Server listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        data = client_socket.recv(4096)  # Adjust buffer size as needed
        if data:
            log_message = data.decode('utf-8')  # Decode received logs
            print("Received logs:")
            print(log_message)

            # Write logs to a file in the same directory as this script
            log_file_path = os.path.join(os.path.dirname(__file__), 'received_logs.txt')
            with open(log_file_path, 'a') as log_file:  # Open in append mode
                log_file.write(log_message + '\n')  # Write logs with a newline
            print(f"Logs written to {log_file_path}")
        client_socket.close()

if __name__ == "__main__":
    port = 88  # Match the port with your client script
    start_server(port)
