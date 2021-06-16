import socket
import gc

gc.collect()

def start():
    HOST = "192.168.4.1"
    PORT = 13326

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print("{} server in {} port is on!".format(HOST, PORT))
    client, addr = s.accept()
    print("Client: {}, Port: {}".format(addr[0], addr[1]))

    while True:
        msg = client.recv(128).decode("utf-8")

        print("Receive message:", msg)
        reply = ''

        if msg == "hey":
            reply = b"Hello"
        elif msg == "bye":
            client.send(b"quit")
            break
        else:
            reply = b"what??"

        client.send(reply)

    client.close()
