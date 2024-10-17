import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [

    board.IO21, 
    board.IO26, # type: ignore  
    board.IO47, 
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48, 
    board.IO35, 
    board.IO36, 
    board.IO37, 
    board.IO38, 
    board.IO39  

    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

volume_prev=0 #initializing the previous volume to 0
i=0           #initializing i to 0

# main loop
while True:
    
    
    volume = microphone.value
    
    diff=volume-volume_prev #calculates the difference between current volume and previously read volume 
    print(diff)

    
    
    if abs(diff)>1400:       #when the difference in the volume is greater than a certain threshold (I have set it to 1400 based on the readings in my environment)
        leds[i].value = True #It depicts the fact that there has been an increase in volume and hence turns on more leds as the change is detected
        i+=1            
        if i>10:              #Ensures that we don't go out of bounds when indexing the list "leds" (since we have 0-10 indices)
            i=10
        
    
    else:                      #when the volume is decreased the change is usually gradually read and hence it is not a drastic fall as big as my threshold value
        leds[i].value = False  #hence it decreases the number of leds turned on one at a time
        i-=1
        if i<0:
            i=0                 #this line ensures we don't index negatively
    
    
    volume_prev=microphone.value
    
    sleep(0.2)

    
 
