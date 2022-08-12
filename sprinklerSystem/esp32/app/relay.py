from machine import Pin
import time


class Relay:


    zone1 = Pin(4, Pin.OUT)    #D4
    zone2 = Pin(18, Pin.OUT)   #D18
    zone3 = Pin(19, Pin.OUT)   #D19
    zone4 = Pin(22, Pin.OUT)   #D22
    bLed1 = Pin(2, Pin.OUT)    #bled

    def __init__(self):

        self.zone1.on()
        self.zone2.on()
        self.zone3.on()
        self.zone4.on()
        self.bLed1.off()

    def setBoardLed1(self, v=1):
        self.bLed1.value(v)

    def setRelay1(self, v=1):
        self.zone1.value(v)

    def getValueofRelay1(self):
        return self.zone1.value()

    def setRelay2(self, v=1):
        self.zone2.value(v)

    def getValueofRelay2(self):
        return self.zone2.value()

    def setRelay3(self, v=1):
        self.zone3.value(v)

    def getValueofRelay3(self):
        return self.zone3.value()

    def setRelay4(self, v=1):
        self.zone4.value(v)

    def getValueofRelay4(self):
        return self.zone4.value()

    #time.sleep(0.2)
