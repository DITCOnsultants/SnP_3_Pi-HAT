#!/bin/sh
iw wlan0 set power_save off
apt update
apt install python3-pip pigpio python3-smbus
pip3 install bme280pi RPi.gpio pigpio requests
