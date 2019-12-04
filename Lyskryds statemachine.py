from random import random
from time import sleep
from gpiozero import LED


nred = LED(21)
nyellow = LED(20)
ngreen = LED(16)

vred = LED(22)
vyellow = LED(27)
vgreen = LED(17)

delay1 = 0.5
delay2 = 1
delay3 = 2

def state0():
    nyellow.off()
    nred.on()
    vred.on()
    sleep(delay3)
    return state1

def state1():
    vred.off()
    vyellow.on()
    sleep(delay1)
    vyellow.off()
    vgreen.on()
    sleep(delay2)
    return state2

def state2():
    vgreen.off()
    vyellow.on()
    sleep(delay1)
    vred.on()
    sleep(delay2)
    vyellow.off()
    return state3

def state3():
    vred.on()
    nred.off()
    nyellow.on()
    sleep(delay1)  
    return state4
    
def state4():
    nyellow.off()
    ngreen.on()
    sleep(delay2)
    return state5
    
def state5():
    ngreen.off()
    nyellow.on()
    sleep(delay1)
    nred.on()
    sleep(delay2)
    return state0
    
        
state=state0 #initial state
while state: state=state() #launch statemachine
print("Done with state")