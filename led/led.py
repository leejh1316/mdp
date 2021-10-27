import RPi.GPIO as GPIO

class Arduino_NeoPixel():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setwarnings(False)
    def neoOn(self):
        GPIO.output(25,GPIO.HIGH)
    def neoOff(self):
        GPIO.output(25,GPIO.LOW)



