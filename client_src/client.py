import socket
from machine import Pin
from time import sleep_ms


def start():
    led = Pin(2, Pin.OUT, value=1)
    sw_led = Pin(0, Pin.IN, Pin.PULL_UP)
    sw_bye = Pin(12, Pin.IN, Pin.PULL_UP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(("192.168.4.1", 13326))

    while True:
        print("Press any button")
        while sw_led.value() and sw_bye.value():
            pass
        if not sw_led.value():
            msg = "led change"
            while not sw_led.value():
                pass
        if not sw_bye.value():
            msg = "bye"
            while not sw_bye.value():
                pass

        s.send(msg.encode("utf-8"))
        reply = s.recv(128)

        if reply == b'quit':
            print("Disconnect")
            s.close()
            break

        print(str(reply))
