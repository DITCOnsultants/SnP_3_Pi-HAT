import bme280pi

locatie = "te-lui-om-aan-te-passen"
naam = "change-me"



try:
    print("Retrieving sensor data...")
    sensor = bme280pi.Sensor()

    sensordata = sensor.get_data()

    humidity = sensordata['humidity']
    temperature = sensordata['temperature']
    pressure = sensordata['pressure']

except:
    raise Exception('Error retrieving sensor data')

from influxdb import InfluxDBClient
db = InfluxDBClient('influx.cloud.frotmail.nl',8086,database='grafana', ssl=True, username='snp3', password='---')
jso = [ {"measurement": "environment", "tags":{"locatie": locatie, "naam": naam }, "fields": { "temperature": temperature, "humidity": humidity, "pressure": pressure } }]
db.write_points(jso)