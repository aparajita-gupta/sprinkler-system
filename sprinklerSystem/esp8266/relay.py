from machine import Pin
import time


class Relay:
    bLed1 = Pin(16, Pin.OUT) #D0 board LED
    bLed2 = Pin(2, Pin.OUT)  #D4 board LED
    zone1 = Pin(5, Pin.OUT)  #D1
    zone2 = Pin(4, Pin.OUT)  #D2
    zone3 = Pin(0, Pin.OUT) #D3
    zone4 = Pin(14, Pin.OUT) #D5

        #pin4 = Pin(4, Pin.IN)   #D6
    def __init__(self):

        self.zone1.on()
        self.zone2.on()
        self.zone3.on()
        self.zone4.on()
        self.bLed1.off()
        self.bLed2.off()

    def setBoardLed1(self, v=1):
        self.bLed1.value(v)
    def setBoardLed2(self, v=1):
        self.bLed2.value(v)

    def setRelay1(self, v=1):
        self.zone1.value(v)

    def getValueofRelay1(self):
        return self.zone1.value()

    def setRelay2(self, v=0):
        self.zone2.value(v)

    def getValueofRelay2(self):
        return self.zone2.value()

    def setRelay3(self, v=0):
        self.zone3.value(v)

    def getValueofRelay3(self):
        return self.zone3.value()

    def setRelay4(self, v=0):
        self.zone4.value(v)

    def getValueofRelay4(self):
        return self.zone4.value()

    #time.sleep(0.2)
