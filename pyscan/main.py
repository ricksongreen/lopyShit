from nfc_scanner import Scanner

DEBUG = True  # change to True to see debug messages

VALID_CARDS = [
    [0xA5, 0x50, 0xDC, 0x47],  # OV chipkaart karan
    [0x97, 0x0B, 0xAA, 0x70],  # OV chipkaart Rick
    [0x57, 0xE9, 0xFD, 0xD0],  # OV chipkaart Swen
    [0x41, 0xB3, 0xFD, 0x07],  # OV chipkaart Cas
]

if __name__ == "__main__":
    Scanner(DEBUG, VALID_CARDS)
