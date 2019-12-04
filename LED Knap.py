from gpiozero import LED, Button

ledr = LED(21) #Nr alt efter placering af trafiklys (Lysdiode GND + NR)
button2 = Button(17) #Knap Placering
ledy = LED(20) #Nr alt efter placering af trafiklys (Lysdiode GND + NR)
button3 = Button(27) #Knap Placering
ledg = LED(16) #Nr alt efter placering af trafiklys (Lysdiode GND + NR)
button4 = Button(22) #Knap Placering




while True: #Husk at rykke ind under
    button2.when_pressed = ledr.on
    button2.when_released = ledr.off

    button3.when_pressed = ledy.on
    button3.when_released = ledy.off

    button4.when_pressed = ledg.on
    button4.when_released = ledg.off

