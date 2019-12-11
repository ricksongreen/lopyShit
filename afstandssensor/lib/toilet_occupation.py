import pycom
import network
import time
from machine import Pin
import urequests


class ToiletOccupation:
    def __init__(self):
        self.pin_in = Pin("P19", mode=Pin.IN)
        self.pin_out = Pin("P12", mode=Pin.OUT)
        self.toggle = False

        self.url = "http://mambo150.pythonanywhere.com/usage/"
        self.json = { "toilet" : 1 }

        while True:
            if self.pin_in() == 1:
                self.pin_out.value(1)
                if self.toggle == False:
                    self.wait_for_networking()
                    urequests.post(self.url, json=self.json)
                    print("This button is pressed")
                    self.toggle = True
            else:
                self.pin_out(False)
                self.toggle = False

    @staticmethod
    def wait_for_networking():
        print('checking network connection...')
        station = network.WLAN(mode=network.WLAN.STA)
        while not station.isconnected():
            print('waiting for connection...')
            time.sleep(1)
        ip = station.ifconfig()[0]
        print('Device IP address on network:', ip)
        return ip