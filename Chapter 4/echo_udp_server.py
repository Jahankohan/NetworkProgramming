import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "localhost"
port = 44444

server_address = (host, port)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(1024)
    print("Recieved %s bytes from %s" % (len(data), address))
    print(data)

    if(data):
        message = "Dear client: " + str(address) + " Your message is:" + data.decode("ascii")
        sent = sock.sendto(message.encode('ascii'), address)
        print("send %s bytes back to the client %s" % (sent, address))
