#!/bin/sh
TERM=ansi
whiptail --infobox "WiFi powersave disabling..." 10 50
iw wlan0 set power_save off 1> /dev/null
whiptail --infobox "Updating APT" 10 50
apt update 1> /dev/null
whiptail --infobox "Installing APT packages" 10 50
apt install python3-pip pigpio python3-smbus i2c-tools 1> /dev/null
whiptail --infobox "Installing python3 packages" 10 50
pip3 install bme280pi RPi.gpio pigpio requests 1> /dev/null
whiptail --infobox "Enabling i2c" 10 50
raspi-config nonint do_i2c 0 1> /dev/null
echo "Done"
