from PyQt5.QtCore import  QThread
import os
import random as x
class Audio(QThread):
    def __init__(self):
        super().__init__()
        self.sList = ["omxplayer Sound/AnGiMoRing.mp3", "omxplayer Sound/YinGimoti.mp3", "omxplayer Sound/YiYingGMR.mp3"]
    def run(self):
        os.system(x.choice(self.sList))