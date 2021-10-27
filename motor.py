import RPi.GPIO as GPIO
import time

class motorRun():
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
    def cRun(self, chipCnt):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(chipCnt*2.33)
        GPIO.output(23, GPIO.LOW)
        GPIO.cleanup(23)
    def pRun(self, peperoCnt):
        GPIO.output(24, GPIO.HIGH)
        time.sleep(peperoCnt*2.33)
        GPIO.output(24, GPIO.LOW)
        GPIO.cleanup(24)
