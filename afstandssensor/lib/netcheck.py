import network
import time


def wait_for_networking():
    station = network.WLAN(mode=network.WLAN.STA)
    while not station.isconnected():
        print('waiting for network...')
        time.sleep(1)
    ip = station.ifconfig()[0]
    print('Device IP address on network:', ip)
    return ip