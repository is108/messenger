import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients_addresses = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

Quit = False
print("[Server Started]")

while not Quit:
    try:
        value, address = sock.recvfrom(1024)

        if address not in clients_addresses:
            clients_addresses.append(address)

        current_time = time.strftime("%Y-%m-%d:%H.%M.%S", time.localtime())

        print("[" + address[0] + "][" + str(address[1]) + "][" + current_time + "] => ", end = "")
        print(value.decode("utf-8"))

        for client in clients_addresses:
            if address != client:
                sock.sendto(value, client)

    except:
        print("\n[Server Stopped]")
        Quit = True

sock.close()
