#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time, os

schakelaar = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(schakelaar, GPIO.IN)

led_groen = 35
led_geel = 36
led_rood = 38
led_blauw = 37

GPIO.setmode(GPIO.BOARD)
for i in [led_groen, led_geel, led_rood, led_blauw]:
    GPIO.setup(i, GPIO.OUT)


def do_poweroff_sequence(channel):
    print("Going for shutdown...")
    nu = time.time()

    while ((time.time() < nu+5) and (GPIO.input(schakelaar) == 1)):
        time.sleep(1)
        if time.time() - nu > 1:
            GPIO.output(led_groen,1)
        if time.time() - nu > 2:
            GPIO.output(led_geel,1)
        if time.time() - nu > 3:
            GPIO.output(led_rood,1)
        if time.time() - nu > 4:
            GPIO.output(led_blauw,1)
        print(GPIO.input(schakelaar))
    if time.time() > nu+5:
        print("Died")
        os.system('sudo poweroff')
    GPIO.output(led_groen,0)
    GPIO.output(led_geel,0)
    GPIO.output(led_rood,0)
    GPIO.output(led_blauw,0)


GPIO.add_event_detect(schakelaar, GPIO.RISING, callback=do_poweroff_sequence, bouncetime=300)
while(True):
    time.sleep(1)