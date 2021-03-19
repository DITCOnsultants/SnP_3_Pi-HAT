from flask import Response, Flask, request
import bme280pi

app = Flask(__name__)

sensor = bme280pi.Sensor()    
    
@app.route("/")
def print_sensordata():
    global sensor
    sensordata = sensor.get_data()
    pagina = "<html><head><title>Sensor data</title></head>"
    pagina += "<body>"
    pagina += "<h1>Temperatuur</h1>"
    pagina += str(sensordata['temperature'])
    pagina += "<h1>Luchtdruk</h1>"
    pagina += str(sensordata['pressure'])
    pagina += "<h1>Luchtvochtigheid</h1>"
    pagina += str(sensordata['humidity'])
    pagina += "</body></html>"

    return Response(pagina, mimetype="text/html")


app.run(debug=False, port=8080, host='0.0.0.0')
