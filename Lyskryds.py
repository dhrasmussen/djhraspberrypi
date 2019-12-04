from gpiozero import LED
from time import sleep

green = LED(16)
green2 = LED(17)
yellow = LED(20)
yellow2 = LED(27)
red = LED(21)
red2 = LED(22)



delay = 3
delay2 = 1

while True:
    red.on()
    red2.on()
    sleep(delay)
    red2.off()
    yellow2.on()
    sleep(delay2)
    yellow2.off()
    green2.on()
    sleep(delay)
    
    green2.off()
    yellow2.on()
    red2.on()
    sleep(delay2)
    yellow2.off()
       
    red.on()
    sleep(delay)
    red.off()
    yellow.on()
    sleep(delay2)
    yellow.off()
    green.on()
    sleep(delay)
    
    green.off()
    yellow.on()
    red.on()
    sleep(delay2)
    yellow.off()