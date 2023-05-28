import time
import board
import adafruit_dht
import requests
import signal
import random

# IP address of the Flask server
IPADDRESS = '192.168.178.81'

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

count = 0

def handler(signum, frame):
    print("Packets transmitted:", count)
    exit(0)

signal.signal(signal.SIGINT, handler)

old_temp = 0
old_hum = 0

while True:
    try:
        # Read temperature and humidity from DHT22 sensor
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity 

        # Optional: Generate random temperature data
        # temperature_c = random.uniform(20, 30)
        # humidity = random.uniform(20, 30)


        # Send the data to the Flask server
        url = 'http://{0}:5000/data'.format(IPADDRESS)
        data = {'temperature': temperature_c, 'humidity': humidity, 'timestamp': time.time()*1000}
        headers = {'content-type': 'application/json'}

        print(data)

        response = requests.post(url, json=data, headers=headers)

        # Proxy test

        # response = requests.post(url, json=data, headers=headers, proxies={'http': 'http://192.168.178.75:8080'})

        # Print the server response for debugging purposes
        #print(response.content)

        if response.status_code == 200 and response.json()["success"]:
            count += 1

            url_T = 'http://{0}:5000/eventT'.format(IPADDRESS)
            url_H = 'http://{0}:5000/eventH'.format(IPADDRESS)
            headers = {'content-type': 'application/json'}
            message = {'eventT': "Initial"}
            messageH = {'eventH': "Initial"}

            if old_temp == 0:
                print(message)
                requests.post(url_T, json=message, headers=headers)
                old_temp = temperature_c
            elif old_temp == temperature_c:
                message['eventT'] = "Still Temp"
                print(message)
                requests.post(url_T, json=message, headers=headers)
                old_temp = temperature_c
            elif old_temp > temperature_c:
                message['eventT'] = "Got Colder"
                print(message)
                requests.post(url_T, json=message, headers=headers)
                old_temp = temperature_c
            elif old_temp < temperature_c:        
                message['eventT'] = "Got Warmer"
                print(message)
                requests.post(url_T, json=message, headers=headers)
                old_temp = temperature_c


            if old_hum == 0:
                print(messageH)
                requests.post(url_H, json=messageH, headers=headers)
                old_hum = humidity
            elif old_hum == humidity:
                messageH['eventH'] = "Still Hum"
                print(messageH)
                requests.post(url_H, json=messageH, headers=headers)
                old_hum = humidity
            elif  old_hum > humidity:
                messageH['eventH'] = "Got Dryer"
                print(messageH)
                requests.post(url_H, json=messageH, headers=headers)
                old_hum = humidity
            elif old_hum < humidity:
                messageH['eventH'] = "Got Wetter"
                print(messageH)
                requests.post(url_H, json=messageH, headers=headers)
                old_hum = humidity

        # Wait for 1 second before reading the sensor data again
        time.sleep(1.0)
        # time.sleep(0.3)
    except Exception as e:
        print(e)
        time.sleep(2.0)
