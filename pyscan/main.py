import network
import urequests
import time

from nfc_scanner import Scanner

DEBUG = True  # change to True to see debug messages

VALID_CARDS = []


def check_network_connection():
    station = network.WLAN(mode=network.WLAN.STA)
    while not station.isconnected():
        time.sleep(1)
    ip = station.ifconfig()[0]
    return True


def get_valid_cards():
    global VALID_CARDS

    if check_network_connection():
        url = "http://mambo150.pythonanywhere.com/tag/"
        response = urequests.get(url).json()["results"]
        for card in response:
            hex_card = [int(x, 16) for x in card["uid"].split()]
            VALID_CARDS.append(hex_card)


if __name__ == "__main__":
    get_valid_cards()
    Scanner(DEBUG, VALID_CARDS)
