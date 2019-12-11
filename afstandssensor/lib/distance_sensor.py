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

        self.url = "http://mambo150.pythonanywhere.com/toilet/1/"

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
            time.sleep(60)

    def measurement(self):
        self.trigger(0)
        utime.sleep_us(2)
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
        # to transform the time it took to recieve the echo to the distance, we have to multiply it by .017
        self.distance = utime.ticks_diff(start, end) * 0.017
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
        print("Device IP address on network:", ip)
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