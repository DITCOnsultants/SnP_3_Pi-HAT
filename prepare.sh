#!/bin/sh
iw wlan0 set power_save off
apt update
apt install python3-pip pigpio python3-smbus i2c-tools
pip3 install bme280pi RPi.gpio pigpio requests
. raspi-config nonint
do_i2c 1
