from adafruit_pn532.i2c import PN532_I2C
import busio
import board
from digitalio import DigitalInOut
import os
class NFC():
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        reset_pin = DigitalInOut(board.D6)
        req_pin = DigitalInOut(board.D12)
        pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)
        ic, ver, rev, support = pn532.firmware_version
        print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
    def nfcRun(self):
        nfcOpne = os.popen("nfc-poll")
        nfcRead = nfcOpne.read()
        print(nfcRead)
        return nfcRead