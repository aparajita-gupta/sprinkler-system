from machine import Pin
import time

pin4 = Pin(4, Pin.OUT)
pin5 = Pin(5, Pin.OUT)
pin13 = Pin(13, Pin.IN)
for i in range(4000):    
    
    if (pin13.value() ==1):
       #pin5.off()
       pin13.value(0)
       #print(pin13.value())
       pin5.on()
       pin4.off()
       time.sleep(0.5)
       pin5.off()
       pin4.on()
       time.sleep(0.5)
        
    else:
       pin5.off()
       pin4.off()
       time.sleep(0.01)
        #print(pin13.value())
        #testing3
    
    print(i)

pin4.off()