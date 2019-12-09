import pycom
import time
from machine import Pin
import urequests

class ToiletOccupation:
    def __init__(self):
        self.pin_in = Pin('P19', mode=Pin.IN)
        self.pin_out = Pin('P14', mode=Pin.OUT)

        self.url = 'http://mambo150.pythonanywhere.com/usage/'

        while True:
            if self.pin_in() == 1:
                self.pin_out.value(1)
                print("pushed")
            else:
                self.pin_out(False)