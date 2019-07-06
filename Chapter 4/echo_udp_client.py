import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "localhost"
port = 44444
server_address = (host, port)
message = "This is an echo message."

try:
    print("Sending message: " + message)
    sent = sock.sendto(message.encode('ascii'), server_address)
    print("waiting for server ....")
    data, server = sock.recvfrom(1024)
    print(data)

finally:
    sock.close()
