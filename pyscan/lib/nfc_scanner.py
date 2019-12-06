"""
Pyscan NFC scanner using the "Simple Pyscan NFC / MiFare Classic Example"
If a card is detected it will read the UID and compare it to self.valid_cards
RGB LED is BLUE while waiting for card,
GREEN if card is valid, RED if card is invalid
"""

from pyscan import Pyscan
from MFRC630 import MFRC630
from LIS2HH12 import LIS2HH12
from LTR329ALS01 import LTR329ALS01

import binascii
import time
import pycom
import _thread
import urequests
import network

RGB_BRIGHTNESS = 0x8

RGB_RED = RGB_BRIGHTNESS << 16
RGB_GREEN = RGB_BRIGHTNESS << 8
RGB_BLUE = RGB_BRIGHTNESS


class Scanner:
    def __init__(self, debug, valid_cards):
        # Make sure heartbeat is disabled before setting RGB LED
        pycom.heartbeat(False)

        self.debug = debug
        self.valid_cards = valid_cards

        # Define the default attributes
        self.py = Pyscan()
        self.nfc = MFRC630(self.py)
        self.lt = LTR329ALS01(self.py)
        self.li = LIS2HH12(self.py)

        # Initialise the MFRC630 with some settings
        self.nfc.mfrc630_cmd_init()

        # This is the start of our main execution... start the thread
        _thread.start_new_thread(self.discovery_loop, (self.nfc, 0))
        _thread.start_new_thread(self.send_sensor_data, ("Thread 2", 10))

    def check_uid(self, uid, len):
        return self.valid_cards.count(uid[:len])

    def print_debug(self, msg):
        if self.debug:
            print(msg)

    def send_sensor_data(self, name, timeout):
        while True:
            #  print(self.lt.light())
            #  print(self.li.acceleration())
            time.sleep(timeout)

    def discovery_loop(self, nfc, id):
        while True:
            # Send REQA for ISO14443A card type
            #  self.print_debug("Sending REQA for ISO14443A card type...")
            atqa = nfc.mfrc630_iso14443a_WUPA_REQA(nfc.MFRC630_ISO14443_CMD_REQA)
            #  self.print_debug("Response: {}".format(atqa))
            if atqa != 0:
                # A card has been detected, read UID
                self.on_card_read(nfc, id)
            else:
                # No card detected
                #  self.print_debug("Did not detect any card...")
                pycom.rgbled(RGB_BLUE)
                nfc.mfrc630_cmd_reset()
                #  time.sleep(0.5)
                nfc.mfrc630_cmd_init()

    def on_card_read(self, nfc, id):
        self.print_debug("A card has been detected, read UID...")
        uid = bytearray(10)
        uid_len = nfc.mfrc630_iso14443a_select(uid)
        self.print_debug("UID has length: {}".format(uid_len))
        if uid_len > 0:
            self.print_debug(
                "Checking if card with UID: [{:s}] is listed in self.valid_cards...".format(
                    binascii.hexlify(uid[:uid_len], " ").upper()
                )
            )
            if (self.check_uid(list(uid), uid_len)) > 0:
                self.print_debug("Card is listed, turn LED green")
                pycom.rgbled(RGB_GREEN)
                if self.check_network_connection():
                    url = "http://mambo150.pythonanywhere.com/users/"
                    response = urequests.get(url)  # response object
                    print("HTTP status code:{}".format(response.status_code))
                    res = response.json()
                    print(res)
            else:
                self.print_debug("Card is not listed, turn LED red")
                pycom.rgbled(RGB_RED)

    @staticmethod
    def check_network_connection():
        print("checking network connection...")
        station = network.WLAN(mode=network.WLAN.STA)
        while not station.isconnected():
            print("waiting for connection...")
            time.sleep(1)
        ip = station.ifconfig()[0]
        print("Device IP address on network:", ip)
        return True
