from gpiozero import LED
from time import sleep

green = LED(16)
green2 = LED(17)
yellow = LED(20)
yellow2 = LED(27)
red = LED(21)
red2 = LED(22)



delay = 1

while True:
    red.on()
    red2.on()
    print("LED set to on")
    sleep(delay)
    red.off()
    red2.off()
    print("LED set to off")
    sleep(delay)
    
    yellow.on()
    yellow2.on()
    print("LED set to on")
    sleep(delay)
    yellow.off()
    yellow2.off()
    print("LED set to off")
    sleep(delay)
    
    green.on()
    green2.on()
    print("LED set to on")
    sleep(delay)
    green.off()
    green2.off()
    print("LED set to off")
    sleep(delay)
    
    yellow.on()
    yellow2.on()
    red.on()
    red2.on()
    print("LED set to on")
    sleep(delay)
    yellow.off()
    yellow2.off()
    print("LED set to off")
    sleep(delay)
    
    red.off()
    red2.off()
    

    