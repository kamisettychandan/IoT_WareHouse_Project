import paho.mqtt.client as mqtt
import requests
import json

MQTT_BROKER = "mqtt.eclipseprojects.io"
MQTT_TOPIC = "warehouse/temperature"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    # Assuming message payload is JSON with 'sensor' and 'temperature'
    data = json.loads(msg.payload)
    sensor_name = data['sensor']
    temperature = data['temperature']

    # Make a POST request to store data in Django
    requests.post('http://localhost:8000/api/sensors/data', json={
        'sensor': sensor_name,
        'temperature': temperature
    })

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.loop_forever()
