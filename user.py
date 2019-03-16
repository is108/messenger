import socket, threading, time

key = 8194

shutdown = False
join = False

def receving (name, sock):
    while not shutdown:
        try:
            while True:
                value, address = sock.recvfrom(1024)

                decrypt = ""
                k = False

                for i in value.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i)^key)
                print(decrypt)

                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = (socket.gethostbyname(socket.gethostname()), 9090)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
sock.setblocking(0)

username = input("Your name: ")

rT = threading.Thread(target = receving, args = ("RecvThread", sock))
rT.start()

while shutdown == False:
    if join == False:
        sock.sendto((username + " connected to the chat").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()

            crypt = ""
            for i in message:
                crypt += chr(ord(i)^key)
            message = crypt

            if message != "":
                sock.sendto((username + ": " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            sock.sendto((username + " disconnected from chat").encode("utf-8"), server)
            shutdown = True

rT.join()
sock.close()
