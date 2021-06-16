import socket


def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(("192.168.4.1", 13326))

    while True:
        msg = input("Please input sth: ")
        s.send(msg.encode("utf-8"))
        reply = s.recv(128)

        if reply == b'quit':
            print("Disconnect")
            s.close()
            break

        print(str(reply))
