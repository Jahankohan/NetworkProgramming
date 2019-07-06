import socket

# Create socket Object
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
host = socket.gethostname()
port = 12345
server_address = (host, port)

server_sock.bind(server_address)
print("server socket object: %s %s " % server_address)

server_sock.listen(5)

while True:
    client_sock, addr = server_sock.accept()
    print("Accepted connection from: %s" % str(addr))
    try:
        message = client_sock.recv(1024)
        # Process
        string = "Dear Client: " + str(addr) + " Your message is: "
        message = string.encode('ascii') + message 
        client_sock.sendall(message)

    except exception as e:
        client_sock.sendall(str(e))

    finally:
        client_sock.close()
