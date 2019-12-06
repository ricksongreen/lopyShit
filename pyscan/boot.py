# boot.py -- run on boot-up

import pycom

# recommended: https://docs.pycom.io/firmwareapi/micropython/micropython/
import micropython

micropython.alloc_emergency_exception_buf(100)

USE_WIFI = True  # connect to Wifi (True) or not (False)

RGB_BRIGHTNESS = 0x8

RGB_RED = RGB_BRIGHTNESS << 16
RGB_GREEN = RGB_BRIGHTNESS << 8
RGB_BLUE = RGB_BRIGHTNESS

if USE_WIFI:
    from wifimanager import WifiManager

    try:
        pycom.heartbeat(False)  # turn off heartbeat
        wificonfig_file = "config/wificonfig_wf.json"
        print("Start to connect to Wifi...({})".format(wificonfig_file))
        wifi = WifiManager(wificonfig_file)
        print("Device MAC-adres: {}".format(wifi.mac))

        pycom.rgbled(RGB_RED)
        ip = wifi.connect()  # connect device to wifi, returns IP
        pycom.rgbled(RGB_GREEN)

        print("Device is connected to Wifi: {}".format(wifi.isconnected))
        print("\tIP = {}".format(ip))

    except OSError as err:
        print("OSError: file not found...{}".format(err))

    except KeyboardInterrupt:
        print("User interrupted.")

    except Exception as ex:
        print("Exception...")
        print(ex)

    finally:
        print("Finally .. heartbeat back")
        pycom.heartbeat(True)  # turn on heartbeat
