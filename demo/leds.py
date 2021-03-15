#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

led_groen = 35
led_geel = 36
led_rood = 38
led_blauw = 37

GPIO.setmode(GPIO.BOARD)
for i in [led_groen, led_geel, led_rood, led_blauw]:
    GPIO.setup(i, GPIO.OUT)

try:
    while (True):
        GPIO.output(led_blauw,0)
        GPIO.output(led_groen,1)
        time.sleep(1)
        GPIO.output(led_groen,0)
        GPIO.output(led_geel,1)
        time.sleep(1)
        GPIO.output(led_geel,0)
        GPIO.output(led_rood,1)
        time.sleep(1)
        GPIO.output(led_rood,0)
        GPIO.output(led_blauw,1)
        time.sleep(1)
except:
    GPIO.cleanup()
