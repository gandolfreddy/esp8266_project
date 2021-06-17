import esp
esp.osdebug(None)
import gc

import webrepl
webrepl.start()
gc.collect()

def connect_ap(ssid, pwd):
    import network

    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, pwd)
        while not wlan.isconnected():
            pass

    print("network config:", wlan.ifconfig())


connect_ap("MicroPython-2163a5", "micropythoN")
