import requests
import time
import json

import adafruit_dht
import board

# Sensor Data connected to GPIO 4
sensor = adafruit_dht.DHT11(board.D4)

State = "Active"
CurrentData = {"Temp": 0, "Humidity": 0}

# Define the functions

def CheckSensor():
    temp = sensor.temperature
    humid = sensor.humidity
    CurrentData["Temp"] = temp
    CurrentData["Humidity"] = humid
    print()
    print("Temp: " + str(temp))
    print("Humidity: " + str(humid))

while True:
    time.sleep(2) # Update Loop runs every 2 seconds
    requests.post("http://127.0.0.1:3000/heartbeat",json.dumps(CurrentData))
    # Check Sensor Data
    CheckSensor()
    if State == "Stop":
        exit("Got command to stop")
        break

