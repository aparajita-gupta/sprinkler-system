
num = input("Enter a number from 0-15: ")
num = int(num)

pinR = 0
pinB = 0
pinG = 0
pinW = 0

bit = 1

while(1):
    rem = num % 2
    quo = num//2
    
    if(bit == 1):
        pinW = rem
    if(bit == 2):
        pinG = rem
    if(bit == 3):
        pinB = rem
        
    if(quo == 0):
        break
    
    if(quo == 1):
        if(bit == 1):
            pinG = 1
            break
        if(bit == 2):
            pinG = rem
        if(bit == 3):
            pinR = rem
        
    bit = bit + 1
    num = quo

print(pinR, pinB, pinG, pinW)  
    
    
    