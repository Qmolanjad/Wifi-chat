import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = 'localhost'
port = 12345
client_socket.connect((host, port))

while True:

    message = input("You: ")
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    if not response:
        break
    print(f"Server: {response}")

client_socket.close()
