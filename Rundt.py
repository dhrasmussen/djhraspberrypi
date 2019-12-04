from gpiozero import LED
from time import sleep

ledg = LED(16)
ledy = LED(20)
ledr = LED(21)
ledG = LED(17)
ledY = LED(27)
ledR = LED(22)

delay1 = 0.2

while True:
    ledr.on()
    sleep(delay1)
    ledr.off()
    ledy.on()
    sleep(delay1)
    ledy.off()
    ledg.on()
    sleep(delay1)
    ledg.off()
    ledG.on()
    sleep(delay1)
    ledG.off()
    ledY.on()
    sleep(delay1)
    ledY.off()
    ledR.on()
    sleep(delay1)
    ledR.off()
    