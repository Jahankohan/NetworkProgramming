import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345
server_address = (host, port)

try:
    sock.connect(server_address)
    print("Connection Established.......")
    message = "This is an echo message"

    sock.send(message.encode('ascii'))
    recv_message = sock.recv(1024)
    print("Recieved message from server: %s" % recv_message)

except exception as e:
    print(str(e))

finally:
    sock.close()
