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
        
        self.url = "http://school-smart-city.karanjaddoe.nl/toilet/1/"
        # self.url = "http://mambo150.pythonanywhere.com/toilet/1/"

        while True:
            distance = self.measurement()
            self.get_toilet()
            amountOfToiletRolls = round(
                (
                    self.maxAmountOfToiletRolls
                    - ((distance - self.extraDistance) / self.toiletRollSize)
                ),
                2,
            )
            print("Toilet rolls: ", amountOfToiletRolls)
            self.toilet_put(amountOfToiletRolls)
            time.sleep(6)

    def measurement(self):
        self.trigger(0)
        utime.sleep_us(2)
        self.trigger(1)
        utime.sleep_us(5)
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
        meters = (difference * 343) / 2
        self.distance = meters * 100
        print("Distance: ", self.distance)

        # minimal time in between, to not lagg the entire lopy
        utime.sleep_ms(20)

        # return the distance
        return self.distance

    @staticmethod
    def wait_for_networking():
        print("checking network connection...")
        station = network.WLAN(mode=network.WLAN.STA)
        while not station.isconnected():
            print("waiting for connection...")
            time.sleep(1)
        ip = station.ifconfig()[0]
        return True

    def get_toilet(self):
        if self.wait_for_networking():
            res = urequests.get(self.url).json()
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
        urequests.put(self.url, json=json)