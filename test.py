import RPi.GPIO as GPIO
import time
import os
import random as x
from PyQt5.QtCore import QThread
import threading
from _rpi_ws281x import *
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25,GPIO.LOW)

#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(24, GPIO.OUT)
# GPIO.output(23, GPIO.HIGH)
# time.sleep(2.1)
# GPIO.output(23, GPIO.LOW)
# GPIO.output(24, GPIO.HIGH)
# time.sleep(2.1)
# GPIO.output(24, GPIO.LOW)
# GPIO.cleanup()
#
# class tChipMotorStart():
#     def __init__(self, chipCnt):
#         super().__init__()
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(23, GPIO.OUT)
#         self.chipCnt = chipCnt
#     def run(self):
#         GPIO.output(23, GPIO.HIGH)
#         time.sleep(self.chipCnt*2.2)
#         GPIO.output(23, GPIO.LOW)
#         GPIO.cleanup(23)
# class tPeperoMotorStart():
#     def __init__(self, peperoCnt):
#         super().__init__()
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(24, GPIO.OUT)
#         self.peperoCnt = peperoCnt
#     def run(self):
#         GPIO.output(24, GPIO.HIGH)
#         time.sleep(self.peperoCnt*2.2)
#         GPIO.output(24, GPIO.LOW)
#         GPIO.cleanup(24)
# t1 = tChipMotorStart(1)
# t2 = tPeperoMotorStart(2)
# t1.run()
# t2.run()
# #
# class tAudioStart(QThread):
#     def __init__(self):
#         super().__init__()
#         self.sList = ["omxplayer Sound/AnGiMoRing.mp3", "omxplayer Sound/YinGimoti.mp3", "omxplayer Sound/YiYingGMR.mp3"]
#     def run(self):
#         os.system(x.choice(self.sList))
# ad = tAudioStart()
# ad.start()


#sList = ["omxplayer Sound/AnGiMoRing.mp3", "omxplayer Sound/YinGimoti.mp3", "omxplayer Sound/YiYingGMR.mp3"]
#os.system(x.choice(sList))

# import random as x
# sList = ["omxplayer Sound/AnGiMoRing.mp3", "omxplayer Sound/YinGimoti.mp3", "omxplayer Sound/YiYingGMR.mp3"]
#
# class motor(threading.Thread):
#     def __init__(self,chipCnt):
#         threading.Thread.__init__(self)
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(23, GPIO.OUT)
#         GPIO.setup(24, GPIO.OUT)
#         self.chipCnt=chipCnt
#     def run(self):
#         GPIO.output(23, GPIO.HIGH)
#         time.sleep(2.2)
#         GPIO.output(23, GPIO.LOW)
#     def peperoStart(self, peperoCnt):
#         for i in range(0,peperoCnt):
#             GPIO.output(24, GPIO.HIGH)
#             time.sleep(2.2)
#             GPIO.output(24, GPIO.LOW)
# def osAudio():
#     os.system(x.choice(sList))
# chipcounter=2
# peperocounter=2
# # tChip = motor(chipcounter)
# tPepero = threading.Thread(target=motor.peperoStart, args=(peperocounter))
# tAudio = threading.Thread(target=osAudio)
#
# tAudio.start()
#
# GPIO.cleanup()

# import neopixel
# import board
# pixel = neopixel.NeoPixel(board.D18,120)
# pixel.fill((255,255,255))
# pixel.show()
# pixel.fill((0,0,0))
#
# #dddd
# # os.system("sudo python3 rpi_ws281x/python/examples/neopixelclock.py")
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMessageBox
#
# class mainwindow(QDialog):
#     def __init__(self):
#         super().__init__()
#     def closeEvent(self, event):
#         print("123")
#
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#
#     a = mainwindow()
#     a.show()
#     sys.exit(app.exec_())
