#This script requires special setup please see the documentation:
# ~ documentation to be posed soon ~

import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time
import socket

#set up gpio pins
def gpioSetup():
    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)


#only exe if connect sucessfull

def connectionStatus(client, userdata, flags, rc):
    mqttClient.subscribe("rpi/gpio")

def messageDecoder(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8')

# deal with sending the commands to the server

#door 1/4

    if message == "op 23":
        gpio.output(23, gpio.LOW)
        time.sleep(.2)
        gpio.output(23, gpio.HIGH)
        print("door #1 is opened/closed")

            
# door 2/4
# my door number 2 required this modified pulse
    elif message == "op 24":
        gpio.output(24, gpio.HIGH)
        time.sleep(.2)
        gpio.output(24, gpio.LOW)
        print("door #2 is opened/closed")


# door 3/4            

    elif message == "op 27":
        gpio.output(27, gpio.LOW)
        time.sleep(.2)
        gpio.output(27, gpio.HIGH)
        print("door #3 is opened/closed")
    
    # door 4/4            

    elif message == "op 22":
        gpio.output(22, gpio.LOW)
        time.sleep(.2)
        gpio.output(22, gpio.HIGH)
        print("door #4 is opened/closed")

            
        #should never reach else case
    else:
            print("Data recived is not a command")


    
gpioSetup()

clientName = "GaragePi"

#set the mqtt sever address

#automatically get IP of device (not my code)
#source: https://stackoverflow.com/questions/166506
#/finding-local-ip-addresses-using-pythons-stdlib

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
serverAddress = (s.getsockname()[0])
s.close()


mqttClient = mqtt.Client(clientName)

mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

mqttClient.connect(serverAddress)

mqttClient.loop_forever()
