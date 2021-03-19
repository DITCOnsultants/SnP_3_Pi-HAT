import bme280pi, time
from influxdb import InfluxDBClient

locatie = "Home"
naam = "Home"

sensor = bme280pi.Sensor()
db = InfluxDBClient('localhost',8086,database='grafana', ssl=False, username='myadminuser', password='veryverysecret')

while True:
    try:
        print("Retrieving sensor data...")
        sensordata = sensor.get_data()
        humidity = sensordata['humidity']
        temperature = sensordata['temperature']
        pressure = sensordata['pressure']

    except:
        raise Exception('Error retrieving sensor data')

    jso = [ {"measurement": "environment", "tags":{"locatie": locatie, "naam": naam }, "fields": { "temperature": temperature, "humidity": humidity, "pressure": pressure } }]
    db.write_points(jso)
    print("Sleeping...")
    time.sleep(30)
