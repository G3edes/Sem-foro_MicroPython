from machine import Pin
from utime import sleep

red_light  = Pin(17, Pin.OUT)
yellow_light  = Pin(18, Pin.OUT)
green_light  = Pin(19, Pin.OUT)

while True:
    red_light.on()
    print("STOP!")
    sleep(7)
    red_light.off()
    yellow_light.on()
    print("ATTENTION!")
    sleep(10)
    yellow_light.off()
    green_light.on()
    print("GO!")
    sleep(20)
    green_light.off()