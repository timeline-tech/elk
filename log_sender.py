import socket
def read_log_file(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def connect_to_ec2(instance_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((instance_ip, port))
        print(f"Connected to {instance_ip} on port {port}")
        return sock
    except Exception as e:
        print(f"Connection failed: {e}")
        return None


def send_logs(sock, log_contents):
    try:
        sock.sendall(log_contents.encode('utf-8'))  # Encode log contents to bytes
        print("Logs sent successfully.")
    except Exception as e:
        print(f"Error sending logs: {e}")

def main():
    instance_ip = ''  # Replace with your EC2 instance IP
    port = 88  # Replace with your desired port number
    log_file_path = ''  # Path to your log file

    # Read logs
    log_contents = read_log_file(log_file_path)
    if log_contents is not None:
        # Connect to EC2
        sock = connect_to_ec2(instance_ip, port)
        if sock:
            # Next steps will go here
            send_logs(sock, log_contents)
            sock.close()

if __name__ == "__main__":
    main()
