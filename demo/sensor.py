#!/usr/bin/env python3
import bme280pi

try:
    print("Retrieving sensor data...")
    sensor = bme280pi.Sensor()
    sensordata = sensor.get_data()
    print(sensordata)
except:
    raise Exception('Error retrieving sensor data')