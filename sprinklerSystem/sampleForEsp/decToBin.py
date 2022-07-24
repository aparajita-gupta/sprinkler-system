from machine import Pin

num = input("Enter a number from 0-15: ")
num = int(num)

pinR = Pin(16, Pin.OUT)
pinB = Pin(5, Pin.OUT)
pinG = Pin(4, Pin.OUT)
pinW = Pin(2, Pin.OUT) 

pinR.value(0)
pinB.value(0)
pinG.value(0)
pinW.value(0)

bit = 1

while(1):
    rem = num % 2
    quo = num//2
    
    if(bit == 1):
        pinW.value(rem)
    if(bit == 2):
        pinG.value(rem)
    if(bit == 3):
        pinB.value(rem)
        
    if(quo == 0):
        pinR.value(rem)
        break
    
    if(quo == 1):
        if(bit == 1):
            pinG.value(1)
            break
        if(bit == 2):
            pinB.value(rem)
        if(bit == 3):
            pinR.value(rem)
        
    bit = bit + 1
    num = quo

print(pinR.value(), pinB.value(), pinG.value(), pinW.value())  
    
    
    