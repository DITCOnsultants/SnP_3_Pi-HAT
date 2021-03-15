#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

schakelaar = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(schakelaar, GPIO.IN)

print("Waiting until switch is pressed...")
while GPIO.input(schakelaar) == 0:
    time.sleep(0.1)

print("Switch is pressed!")