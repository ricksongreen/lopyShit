import _thread
import gc
import machine
import network
import pycom
import time
import urequests
import utime
from machine import Pin

class DistanceSensor:
    # declaration of the pins
    def __init__(self):
        self.echo = Pin("P21", mode=Pin.IN)
        self.trigger = Pin("P20", mode=Pin.OUT)
        self.trigger(0)
        
        self.url = "http://school-smart-city.karanjaddoe.nl/toilet/1/"
        # self.url = "http://mambo150.pythonanywhere.com/toilet/1/"

        self.get_toilet()

        while True:
            amountOfToiletRolls = round(
                ( self.maxAmountOfToiletRolls
                    - ((self.measurement() - self.extraDistance) / self.toiletRollSize)),
                2,
            )
            print("Toilet rolls: ", amountOfToiletRolls)
            self.toilet_put(amountOfToiletRolls)
            time.sleep(60)

    @staticmethod
    def retrieve_url(url):
        gc.collect() 
        resp = None
        try:
            resp = urequests.get(url)
            value = resp.json()
        except Exception as e: # Here it catches any error.
            if isinstance(e, OSError) and resp: # If the error is an OSError the socket has to be closed.
                resp.close()
            value = {"error": e}
        gc.collect()
        return value

    @staticmethod
    def put_url(url, data):
        gc.collect() 
        resp = None
        try:
            resp = urequests.put(url, json=data)
            value = resp.json()
        except Exception as e: # Here it catches any error.
            if isinstance(e, OSError) and resp: # If the error is an OSError the socket has to be closed.
                resp.close()
            value = {"error": e}
        gc.collect()
        return value

    def measurement(self):
        self.trigger(1)
        utime.sleep_us(10)
        self.trigger(0)

        # we have to wait until the echo gets something back
        while self.echo() == 0:
            pass
        start = utime.ticks_us()
        while self.echo() == 1:
            pass
        end = utime.ticks_us()
        # Given: ticks in microseconds. Needed: centimeters.
        # Calc: ticks / 1*10^6 = seconds. Seconds x speed of sound (343 m/s).
        # This then has to be divided by 2, since the sounds goes towards the object and back.
        # And multiply with 100 to change the meters given to centimeters
        difference = utime.ticks_diff(start, end) / 1000000
        self.distance = ((difference * 343) / 2) * 100
        print("Distance: ", self.distance)
    
        # return the distance
        return self.distance

    def get_toilet(self):
        res = self.retrieve_url(self.url)
        self.maxAmountOfToiletRolls = res["maxAmountOfToiletRolls"]
        self.toiletRollSize = res["toiletRollSize"]
        self.extraDistance = res["extraDistance"]
        self.place = res["place"]

    def toilet_put(self, amount):
        json = {
            "id": 1,
            "place": self.place,
            # 'place' : 'WF 1ste Etage',
            "toiletPaper": amount,
            "maxAmountOfToiletRolls": self.maxAmountOfToiletRolls,
            # 'maxAmountOfToiletRolls' : 8,
            "toiletRollSize": self.toiletRollSize,
            # 'toiletRollSize' : 12,
            "extraDistance": self.extraDistance
            # 'extraDistance' : 4
        }
        res = self.put_url(self.url, json)
        print(res)