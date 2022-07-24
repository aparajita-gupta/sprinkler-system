from machine import Pin
import time


def runLeds(run = True):
    if run == False:
        return
    pinR = Pin(16, Pin.OUT)
    pinB = Pin(5, Pin.OUT)
    pinG = Pin(2, Pin.OUT)
    pinW = Pin(0, Pin.OUT)
    pin4 = Pin(4, Pin.IN)
    pinR.off()
    pinB.off()
    pinG.off()
    pinW.off()

    time.sleep(0.2)
    if pin4.value() == 1:
       print ("1 value is {}".format(pin4.value()))
    else:
       print ("2 value is {} ".format(pin4.value()))
       pinR.off()
       time.sleep(0.2)
       pinR.on()
       time.sleep(0.2)
       pinR.off()
       time.sleep(0.2)
       pinB.on()
       time.sleep(0.2)
       pinB.off()
       time.sleep(0.2)
       pinG.on()
       time.sleep(0.2)
       pinG.off()
       time.sleep(0.2)
       pinW.on()
       time.sleep(0.2)
       pinW.off()
