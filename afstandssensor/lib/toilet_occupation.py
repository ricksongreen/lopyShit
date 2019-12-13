import pycom
import network
import time
import _thread
from machine import Pin
import urequests as request
import gc


BASE_URL = "http://school-smart-city.karanjaddoe.nl"

class ToiletOccupation:
    def __init__(self):
        global BASE_URL
        self.pin_in = Pin("P19", mode=Pin.IN)
        self.pin_out = Pin("P23", mode=Pin.OUT)
        self.toggle = False

        # self.url = "http://school-smart-city.karanjaddoe.nl/usage/"
        self.url = "http://school-smart-city.karanjaddoe.nl"

        # self.url = "http://mambo150.pythonanywhere.com/usage/"

        while True:
            if self.pin_in() == 1:
                if self.toggle == False:
                    self.pin_out.value(1)
                    self.on_button_press()
                    print("This button is pressed")
                    self.toggle = True
            else:
                self.pin_out(False)
                self.toggle = False

    @staticmethod
    def retrieve_url(url):
        gc.collect() 
        resp = None
        try:
            resp = request.get(url)
            value = resp.json()
        except Exception as e: # Here it catches any error.
            if isinstance(e, OSError) and resp: # If the error is an OSError the socket has to be closed.
                resp.close()
            value = {"error": e}
        gc.collect()
        return value

    @staticmethod
    def post_url(url, data):
        gc.collect() 
        resp = None
        try:
            headers = {
                "Content-Type": "application/json",
            }
            resp = request.post(url, headers=headers, json=data)
            value = resp.json()
        except Exception as e: # Here it catches any error.
            if isinstance(e, OSError) and resp: # If the error is an OSError the socket has to be closed.
                resp.close()
            value = {"error": e}
        gc.collect()
        return value

    def on_button_press(self):
        global BASE_URL
        data = {
            "toilet": 1
        }
        res = self.post_url(BASE_URL + "/usage/", data)
        return res

    @staticmethod
    def wait_for_networking():
        print('checking network connection...')
        station = network.WLAN(mode=network.WLAN.STA)
        while not station.isconnected():
            print('waiting for connection...')
            time.sleep(1)
        ip = station.ifconfig()[0]
        print('Device IP address on network:', ip)
        return True