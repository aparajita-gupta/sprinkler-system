from machine import Pin
import time

pinR = Pin(16, Pin.OUT)
pinB = Pin(5, Pin.OUT)
pinG = Pin(4, Pin.OUT)
pinW = Pin(0, Pin.OUT) 

for i in range(2000):
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
